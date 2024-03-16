# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

DOWNLOADS = {
    "autoconf": {
        "url": "https://ftp.gnu.org/gnu/autoconf/autoconf-2.71.tar.gz",
        "size": 2003781,
        "sha256": "431075ad0bf529ef13cb41e9042c542381103e80015686222b8a9d4abef42a1c",
        "version": "2.71",
    },
    # 6.0.19 is the last version licensed under the Sleepycat license.
    "bdb": {
        "url": "https://ftp.osuosl.org/pub/blfs/conglomeration/db/db-6.0.19.tar.gz",
        "size": 36541923,
        "sha256": "2917c28f60903908c2ca4587ded1363b812c4e830a5326aaa77c9879d13ae18e",
        "version": "6.0.19",
        "library_names": ["db"],
        "licenses": ["Sleepycat"],
        "license_file": "LICENSE.bdb.txt",
    },
    "binutils": {
        "url": "https://ftp.gnu.org/gnu/binutils/binutils-2.42.tar.xz",
        "size": 27567160,
        "sha256": "f6e4d41fd5fc778b06b7891457b3620da5ecea1006c6a4a41ae998109f85a800",
        "version": "2.42",
    },
    "bzip2": {
        "url": "https://sourceware.org/pub/bzip2/bzip2-1.0.8.tar.gz",
        "size": 810029,
        "sha256": "ab5a03176ee106d3f0fa90e381da478ddae405918153cca248e682cd0c4a2269",
        "version": "1.0.8",
        "library_names": ["bz2"],
        "licenses": ["bzip2-1.0.6"],
        "license_file": "LICENSE.bzip2.txt",
    },
    "cpython-3.8": {
        "url": "https://www.python.org/ftp/python/3.8.18/Python-3.8.18.tar.xz",
        "size": 20696952,
        "sha256": "3ffb71cd349a326ba7b2fadc7e7df86ba577dd9c4917e52a8401adbda7405e3f",
        "version": "3.8.18",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp38",
    },
    "cpython-3.9": {
        "url": "https://www.python.org/ftp/python/3.9.18/Python-3.9.18.tar.xz",
        "size": 19673928,
        "sha256": "01597db0132c1cf7b331eff68ae09b5a235a3c3caa9c944c29cac7d1c4c4c00a",
        "version": "3.9.18",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp39",
    },
    "cpython-3.10": {
        "url": "https://www.python.org/ftp/python/3.10.13/Python-3.10.13.tar.xz",
        "size": 19663088,
        "sha256": "5c88848668640d3e152b35b4536ef1c23b2ca4bd2c957ef1ecbb053f571dd3f6",
        "version": "3.10.13",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp310",
    },
    "cpython-3.11": {
        "url": "https://www.python.org/ftp/python/3.11.8/Python-3.11.8.tar.xz",
        "size": 20041256,
        "sha256": "9e06008c8901924395bc1da303eac567a729ae012baa182ab39269f650383bb3",
        "version": "3.11.8",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp311",
    },
    "cpython-3.12": {
        "url": "https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tar.xz",
        "size": 20591308,
        "sha256": "be28112dac813d2053545c14bf13a16401a21877f1a69eb6ea5d84c4a0f3d870",
        "version": "3.12.2",
        "licenses": ["Python-2.0", "CNRI-Python"],
        "license_file": "LICENSE.cpython.txt",
        "python_tag": "cp312",
    },
    "expat": {
        "url": "https://github.com/libexpat/libexpat/releases/download/R_2_5_0/expat-2.5.0.tar.xz",
        "size": 460560,
        "sha256": "ef2420f0232c087801abf705e89ae65f6257df6b7931d37846a193ef2e8cdcbe",
        "version": "2.5.0",
        "library_names": ["expat"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.expat.txt",
    },
    "inputproto": {
        "url": "https://www.x.org/archive/individual/proto/inputproto-2.3.2.tar.gz",
        "size": 244334,
        "sha256": "10eaadd531f38f7c92ab59ef0708ca195caf3164a75c4ed99f0c04f2913f6ef3",
        "version": "2.3.2",
    },
    "jom-windows-bin": {
        "url": "http://download.qt.io/official_releases/jom/jom_1_1_3.zip",
        "size": 1213852,
        "sha256": "128fdd846fe24f8594eed37d1d8929a0ea78df563537c0c1b1861a635013fff8",
        "version": "1.1.3",
    },
    "kbproto": {
        "url": "https://www.x.org/archive/individual/proto/kbproto-1.0.7.tar.gz",
        "size": 325858,
        "sha256": "828cb275b91268b1a3ea950d5c0c5eb076c678fdf005d517411f89cc8c3bb416",
        "version": "1.0.7",
    },
    # 20221009-3.1 fails to build on musl due to an includes issue.
    "libedit": {
        "url": "https://thrysoee.dk/editline/libedit-20210910-3.1.tar.gz",
        "size": 524722,
        "sha256": "6792a6a992050762edcca28ff3318cdb7de37dccf7bc30db59fcd7017eed13c5",
        "version": "20210910-3.1",
        "library_names": ["edit"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libedit.txt",
    },
    "libffi-3.3": {
        "url": "https://github.com/libffi/libffi/releases/download/v3.3/libffi-3.3.tar.gz",
        "size": 1305466,
        "sha256": "72fba7922703ddfa7a028d513ac15a85c8d54c8d67f55fa5a4802885dc652056",
        "version": "3.3",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libffi": {
        "url": "https://github.com/libffi/libffi/releases/download/v3.4.4/libffi-3.4.4.tar.gz",
        "size": 1362394,
        "sha256": "d66c56ad259a82cf2a9dfc408b32bf5da52371500b84745f7fb8b645712df676",
        "version": "3.4.4",
        "library_names": ["ffi"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libffi.txt",
    },
    "libpthread-stubs": {
        "url": "https://www.x.org/archive/individual/lib/libpthread-stubs-0.5.tar.gz",
        "size": 74938,
        "sha256": "593196cc746173d1e25cb54a93a87fd749952df68699aab7e02c085530e87747",
        "version": "0.5",
    },
    "libX11": {
        "url": "https://www.x.org/archive/individual/lib/libX11-1.6.12.tar.gz",
        "size": 3168158,
        "sha256": "0fce5fc0a24a3dc728174eccd0cb8d6a1b37a2ec1654bd5628c84e5bc200d594",
        "version": "1.6.12",
        "library_names": ["X11", "X11-xcb"],
        "licenses": ["MIT", "X11"],
        "license_file": "LICENSE.libX11.txt",
    },
    "libXau": {
        "url": "https://www.x.org/releases/individual/lib/libXau-1.0.11.tar.gz",
        "size": 404973,
        "sha256": "3a321aaceb803577a4776a5efe78836eb095a9e44bbc7a465d29463e1a14f189",
        "version": "1.0.11",
        "library_names": ["Xau"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libXau.txt",
    },
    # Newer versions of libxcb require a modern Python to build. We can take this
    # dependency once we feel like doing the work.
    "libxcb": {
        "url": "https://xcb.freedesktop.org/dist/libxcb-1.14.tar.gz",
        "size": 640322,
        "sha256": "2c7fcddd1da34d9b238c9caeda20d3bd7486456fc50b3cc6567185dbd5b0ad02",
        "version": "1.14",
        "library_names": ["xcb"],
        "licenses": ["MIT"],
        "license_file": "LICENSE.libxcb.txt",
    },
    "llvm-14-x86_64-linux": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20220508/llvm-14.0.3+20220508-gnu_only-x86_64-unknown-linux-gnu.tar.zst",
        "size": 158614671,
        "sha256": "04cb77c660f09df017a57738ae9635ef23a506024789f2f18da1304b45af2023",
        "version": "14.0.3+20220508",
    },
    "llvm-18-x86_64-linux": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20240316/llvm-18.1.1+20240316-gnu_only-x86_64-unknown-linux-gnu.tar.zst",
        "size": 238434975,
        "sha256": "4c4f5cefc71241836557c5e9977b664652e4aa8365c23c5cd1875c8a629ee2c7",
        "version": "18.1.1+20240316",
    },
    "llvm-aarch64-macos": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20240316/llvm-18.1.1+20240316-aarch64-apple-darwin.tar.zst",
        "size": 136631296,
        "sha256": "ff3b55710ee3b1165a0c29947ee16f4373d85758a08452df1db22ad9691fd4c7",
        "version": "18.1.1+20240316",
    },
    "llvm-x86_64-macos": {
        "url": "https://github.com/indygreg/toolchain-tools/releases/download/toolchain-bootstrap%2F20240316/llvm-18.1.1+20240316-x86_64-apple-darwin.tar.zst",
        "size": 136620757,
        "sha256": "6d49f4933b15a7535ec9d0a5f9cdc65a45c38b03ec96203bdea153cbf38ff8c6",
        "version": "18.1.1+20240316",
    },
    "m4": {
        "url": "https://ftp.gnu.org/gnu/m4/m4-1.4.19.tar.xz",
        "size": 1654908,
        "sha256": "63aede5c6d33b6d9b13511cd0be2cac046f2e70fd0a07aa9573a04a82783af96",
        "version": "1.4.19",
    },
    "mpdecimal": {
        "url": "https://www.bytereef.org/software/mpdecimal/releases/mpdecimal-2.5.1.tar.gz",
        "size": 2584021,
        "sha256": "9f9cd4c041f99b5c49ffb7b59d9f12d95b683d88585608aa56a6307667b2b21f",
        "version": "2.5.1",
        "library_names": ["mpdec"],
        "licenses": ["BSD-2-Clause"],
        "license_file": "LICENSE.mpdecimal.txt",
    },
    "musl": {
        "url": "https://musl.libc.org/releases/musl-1.2.5.tar.gz",
        "size": 1080786,
        "sha256": "a9a118bbe84d8764da0ea0d28b3ab3fae8477fc7e4085d90102b8596fc7c75e4",
        "version": "1.2.5",
    },
    "ncurses": {
        "url": "https://ftp.gnu.org/pub/gnu/ncurses/ncurses-6.4.tar.gz",
        "size": 3612591,
        "sha256": "6931283d9ac87c5073f30b6290c4c75f21632bb4fc3603ac8100812bed248159",
        "version": "6.4",
        "library_names": ["ncurses", "ncursesw", "panel", "panelw"],
        "licenses": ["X11"],
        "license_file": "LICENSE.ncurses.txt",
    },
    # Remember to update OPENSSL_VERSION_INFO in verify_distribution.py whenever upgrading.
    "openssl-1.1": {
        "url": "https://www.openssl.org/source/openssl-1.1.1w.tar.gz",
        "size": 9893384,
        "sha256": "cf3098950cb4d853ad95c0841f1f9c6d3dc102dccfcacd521d93925208b76ac8",
        "version": "1.1.1w",
        "library_names": ["crypto", "ssl"],
        "licenses": ["OpenSSL"],
        "license_file": "LICENSE.openssl-1.1.txt",
    },
    # We use OpenSSL 3.0 because it is an LTS release and has a longer support
    # window. If CPython ends up gaining support for 3.1+ releases, we can consider
    # using the latest available.
    # Remember to update OPENSSL_VERSION_INFO in verify_distribution.py whenever upgrading.
    "openssl-3.0": {
        "url": "https://www.openssl.org/source/openssl-3.0.13.tar.gz",
        "size": 15294843,
        "sha256": "88525753f79d3bec27d2fa7c66aa0b92b3aa9498dafd93d7cfa4b3780cdae313",
        "version": "3.0.13",
        "library_names": ["crypto", "ssl"],
        "licenses": ["Apache-2.0"],
        "license_file": "LICENSE.openssl-3.txt",
    },
    "nasm-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/nasm-2.11.06.tar.gz",
        "size": 384826,
        "sha256": "8af0ae5ceed63fa8a2ded611d44cc341027a91df22aaaa071efedc81437412a5",
        "version": "2.11.06",
    },
    "patchelf": {
        "url": "https://github.com/NixOS/patchelf/releases/download/0.18.0/patchelf-0.18.0.tar.bz2",
        "size": 423290,
        "sha256": "1952b2a782ba576279c211ee942e341748fdb44997f704dd53def46cd055470b",
        "version": "0.18.0",
    },
    "pip": {
        "url": "https://files.pythonhosted.org/packages/8a/6a/19e9fe04fca059ccf770861c7d5721ab4c2aebc539889e97c7977528a53b/pip-24.0-py3-none-any.whl",
        "size": 2110226,
        "sha256": "ba0d021a166865d2265246961bec0152ff124de910c5cc39f1156ce3fa7c69dc",
        "version": "24.0",
    },
    "readline": {
        "url": "https://ftp.gnu.org/gnu/readline/readline-8.2.tar.gz",
        "size": 3043952,
        "sha256": "3feb7171f16a84ee82ca18a36d7b9be109a52c04f492a053331d7d1095007c35",
        "version": "8.2",
        "library_names": ["readline"],
        "licenses": ["GPL-3.0-only"],
        "license_file": "LICENSE.readline.txt",
    },
    "setuptools": {
        "url": "https://files.pythonhosted.org/packages/bb/0a/203797141ec9727344c7649f6d5f6cf71b89a6c28f8f55d4f18de7a1d352/setuptools-69.1.0-py3-none-any.whl",
        "size": 819310,
        "sha256": "c054629b81b946d63a9c6e732bc8b2513a7c3ea645f11d0139a2191d735c60c6",
        "version": "69.1.0",
    },
    # Remember to update verify_distribution.py when version changed.
    "sqlite": {
        "url": "https://www.sqlite.org/2024/sqlite-autoconf-3450100.tar.gz",
        "size": 3232682,
        "sha256": "cd9c27841b7a5932c9897651e20b86c701dd740556989b01ca596fcfa3d49a0a",
        "version": "3450100",
        "actual_version": "3.45.1.0",
        "library_names": ["sqlite3"],
        "licenses": [],
        "license_file": "LICENSE.sqlite.txt",
        "license_public_domain": True,
    },
    "strawberryperl": {
        "url": "http://strawberryperl.com/download/5.28.1.1/strawberry-perl-5.28.1.1-32bit-portable.zip",
        "size": 143242779,
        "sha256": "8b15c7c9574989568254a7859e473b7d5f68a1145d2e4418036600a81b13805c",
        "version": "5.28.1.1",
    },
    "tcl": {
        "url": "https://prdownloads.sourceforge.net/tcl/tcl8.6.12-src.tar.gz",
        "size": 10353486,
        "sha256": "26c995dd0f167e48b11961d891ee555f680c175f7173ff8cb829f4ebcde4c1a6",
        "version": "8.6.12",
        "library_names": ["tcl8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tix": {
        "url": "https://github.com/python/cpython-source-deps/archive/tix-8.4.3.6.tar.gz",
        "size": 1836451,
        "sha256": "f7b21d115867a41ae5fd7c635a4c234d3ca25126c3661eb36028c6e25601f85e",
        "version": "8.4.3.6",
        "licenses": ["TCL"],
        "license_file": "LICENSE.tix.txt",
    },
    "tk": {
        "url": "https://prdownloads.sourceforge.net/tcl/tk8.6.12-src.tar.gz",
        "size": 4515393,
        "sha256": "12395c1f3fcb6bed2938689f797ea3cdf41ed5cb6c4766eec8ac949560310630",
        "version": "8.6.12",
        "library_names": ["tk8.6"],
        "licenses": ["TCL"],
        "license_file": "LICENSE.tcl.txt",
    },
    "tk-windows-bin": {
        "url": "https://github.com/python/cpython-bin-deps/archive/e3c3e9a2856124aa32b608632a52742d479eb7a9.tar.gz",
        "size": 6787654,
        "sha256": "01ad9c663659224e075d487cbc33ea2fed7a225593965b79bed92ca7f79b676f",
        "version": "8.6.12",
        "git_commit": "e3c3e9a2856124aa32b608632a52742d479eb7a9",
    },
    "uuid": {
        "url": "https://sourceforge.net/projects/libuuid/files/libuuid-1.0.3.tar.gz",
        "size": 318256,
        "sha256": "46af3275291091009ad7f1b899de3d0cea0252737550e7919d17237997db5644",
        "version": "1.0.3",
        "library_names": ["uuid"],
        "licenses": ["BSD-3-Clause"],
        "license_file": "LICENSE.libuuid.txt",
    },
    "x11-util-macros": {
        "url": "https://www.x.org/archive/individual/util/util-macros-1.20.0.tar.gz",
        "size": 104931,
        "sha256": "8daf36913d551a90fd1013cb078401375dabae021cb4713b9b256a70f00eeb74",
        "version": "1.20.0",
    },
    "xcb-proto": {
        "url": "https://www.x.org/archive/individual/proto/xcb-proto-1.14.1.tar.gz",
        "size": 194674,
        "sha256": "85cd21e9d9fbc341d0dbf11eace98d55d7db89fda724b0e598855fcddf0944fd",
        "version": "1.14.1",
    },
    "xextproto": {
        "url": "https://www.x.org/archive/individual/proto/xextproto-7.3.0.tar.gz",
        "size": 290814,
        "sha256": "1b1bcdf91221e78c6c33738667a57bd9aaa63d5953174ad8ed9929296741c9f5",
        "version": "7.3.0",
    },
    # Newer versions from at least 2023 have build failures for reasons we haven't
    # fully investigated.
    "xorgproto": {
        "url": "https://www.x.org/archive/individual/proto/xorgproto-2019.1.tar.gz",
        "size": 1119813,
        "sha256": "38ad1d8316515785d53c5162b4b7022918e03c11d72a5bd9df0a176607f42bca",
        "version": "2019.1",
    },
    "xproto": {
        "url": "https://www.x.org/archive/individual/proto/xproto-7.0.31.tar.gz",
        "size": 367979,
        "sha256": "6d755eaae27b45c5cc75529a12855fed5de5969b367ed05003944cf901ed43c7",
        "version": "7.0.31",
    },
    "xtrans": {
        "url": "https://www.x.org/archive/individual/lib/xtrans-1.5.0.tar.gz",
        "size": 230197,
        "sha256": "a806f8a92f879dcd0146f3f1153fdffe845f2fc0df9b1a26c19312b7b0a29c86",
        "version": "1.5.0",
    },
    # TODO upgrade to 5.6+.
    "xz": {
        "url": "https://tukaani.org/xz/xz-5.2.12.tar.gz",
        "size": 2190541,
        "sha256": "61bda930767dcb170a5328a895ec74cab0f5aac4558cdda561c83559db582a13",
        "version": "5.2.12",
        "library_names": ["lzma"],
        # liblzma is in the public domain. Other parts of code have licenses. But
        # we only use liblzma.
        "licenses": [],
        "license_file": "LICENSE.liblzma.txt",
        "license_public_domain": True,
    },
    "zlib": {
        "url": "https://github.com/madler/zlib/releases/download/v1.2.13/zlib-1.2.13.tar.gz",
        "size": 1497445,
        "sha256": "b3a24de97a8fdbc835b9833169501030b8977031bcb54b3b3ac13740f846ab30",
        "version": "1.2.13",
        "library_names": ["z"],
        "licenses": ["Zlib"],
        "license_file": "LICENSE.zlib.txt",
    },
}
