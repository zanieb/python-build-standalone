# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "packaging",
#     "pyyaml",
# ]
# ///
import argparse
import json
from packaging import version
from typing import Any, Dict, List, Optional, Set

import yaml


CI_TARGETS_YAML = "ci-targets.yaml"


def get_os_name(platform: str) -> str:
    os_mapping = {
        "darwin": "macos-latest",
        "linux": "ubuntu-latest",
        "windows": "windows-latest",
    }
    return os_mapping[platform]


def meets_conditional_version(python_version: str, min_version: str) -> bool:
    return version.Version(python_version) >= version.Version(min_version)


def parse_labels(labels: Optional[str]) -> Dict[str, Set[str]]:
    """Parse GitHub labels into a dict of category filters."""
    if not labels:
        return {}

    result: Dict[str, Set[str]] = {
        "platform": set(),
        "python": set(),
        "build": set(),
        "arch": set(),
        "libc": set(),
    }

    for label in labels.split(","):
        label = label.strip()
        if not label or ":" not in label:
            continue
        category, value = label.split(":", 1)
        if category in result:
            result[category].add(value)

    return result


def should_include_entry(entry: Dict[str, str], filters: Dict[str, Set[str]]) -> bool:
    """Check if an entry matches the label filters."""
    # If no filters in a category, include all entries
    # If filters exist, entry must match at least one

    if filters.get("platform") and entry["platform"] not in filters["platform"]:
        return False

    if filters.get("python") and entry["python"] not in filters["python"]:
        return False

    if filters.get("arch") and entry["arch"] not in filters["arch"]:
        return False

    if filters.get("libc") and entry.get("libc") not in filters["libc"]:
        return False

    if filters.get("build"):
        # Special handling for build options to match prefixes
        build_option = entry["build_option"]
        if not any(build_option.startswith(f) for f in filters["build"]):
            return False

    return True


def generate_matrix_entries(
    config: Dict[str, Any],
    platform_filter: Optional[str] = None,
    label_filters: Optional[Dict[str, Set[str]]] = None,
) -> List[Dict[str, str]]:
    matrix_entries = []

    for platform, platform_config in config.items():
        if platform_filter and platform != platform_filter:
            continue

        os_name = get_os_name(platform)

        for target_triple, target_config in platform_config.items():
            process_config(
                matrix_entries,
                os_name,
                target_triple,
                target_config,
                platform,
            )

    # Apply label filters if present
    if label_filters:
        matrix_entries = [
            entry
            for entry in matrix_entries
            if should_include_entry(entry, label_filters)
        ]

    return matrix_entries


def process_config(
    matrix_entries: List[Dict[str, str]],
    os_name: str,
    target_triple: str,
    config: Dict[str, Any],
    platform: str,
) -> None:
    python_versions = config["python_versions"]
    build_options = config["build_options"]
    arch = config["arch"]

    # Create base entry that will be used for all variants
    base_entry = {
        "os": os_name,
        "arch": arch,
        "target_triple": target_triple,
        "platform": platform,
    }

    # Add optional fields if they exist
    if "arch_variant" in config:
        base_entry["arch_variant"] = config["arch_variant"]
    if "libc" in config:
        base_entry["libc"] = config["libc"]
    if "vcvars" in config:
        base_entry["vcvars"] = config["vcvars"]
    if "run" in config:
        base_entry["run"] = str(config["run"]).lower()

    # Process regular build options
    for python_version in python_versions:
        for build_option in build_options:
            entry = base_entry.copy()
            entry.update(
                {
                    "python": python_version,
                    "build_option": build_option,
                }
            )
            matrix_entries.append(entry)

    # Process conditional build options (e.g., freethreaded)
    if "build_options_conditional" in config:
        for conditional in config["build_options_conditional"]:
            min_version = conditional["minimum-python-version"]
            for python_version in python_versions:
                if meets_conditional_version(python_version, min_version):
                    for build_option in conditional["options"]:
                        entry = base_entry.copy()
                        entry.update(
                            {
                                "python": python_version,
                                "build_option": build_option,
                            }
                        )
                        matrix_entries.append(entry)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate GitHub Actions matrix for building"
    )
    parser.add_argument(
        "--platform",
        choices=["darwin", "linux", "windows"],
        help="Filter matrix entries by platform",
    )
    parser.add_argument(
        "--labels",
        help="Comma-separated list of GitHub labels (e.g., 'platform:darwin,python:3.13,build:debug')",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    label_filters = parse_labels(args.labels)

    with open(CI_TARGETS_YAML, "r") as f:
        config = yaml.safe_load(f)

    matrix = {
        "include": generate_matrix_entries(
            config,
            args.platform,
            label_filters,
        )
    }

    # Print the JSON matrix to stdout
    print(json.dumps(matrix))


if __name__ == "__main__":
    main()
