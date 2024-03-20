# Debian Jessie.
FROM debian@sha256:32ad5050caffb2c7e969dac873bce2c370015c2256ff984b70c1c08b3a2816a0
MAINTAINER Gregory Szorc <gregory.szorc@gmail.com>

RUN groupadd -g 1000 build && \
    useradd -u 1000 -g 1000 -d /build -s /bin/bash -m build && \
    mkdir /tools && \
    chown -R build:build /build /tools

ENV HOME=/build \
    SHELL=/bin/bash \
    USER=build \
    LOGNAME=build \
    HOSTNAME=builder \
    DEBIAN_FRONTEND=noninteractive

CMD ["/bin/bash", "--login"]
WORKDIR '/build'

# Jessie's signing keys expired in late 2022. So need to add [trusted=yes] to force trust.
# Jessie stopped publishing snapshots in March 2023.
RUN for s in debian_jessie debian_jessie-updates debian-security_jessie/updates; do \
      echo "deb [trusted=yes] http://snapshot.debian.org/archive/${s%_*}/20230322T152120Z/ ${s#*_} main"; \
    done > /etc/apt/sources.list && \
    ( echo 'Debug::Acquire::http "true";'; \
      echo 'Debug::pkgAcquire::Worker "true";'; \
      echo 'APT::Get::Assume-Yes "true";'; \
      echo 'APT::Install-Recommends "false";'; \
      echo 'Acquire::Check-Valid-Until "false";'; \
      echo 'Acquire::Retries "5";'; \
    ) > /etc/apt/apt.conf.d/99cpython-portable

RUN ( echo 'amd64'; \
      echo 'i386'; \
    ) > /var/lib/dpkg/arch

RUN apt-get update
