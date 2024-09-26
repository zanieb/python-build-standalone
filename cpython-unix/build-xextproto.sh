#!/usr/bin/env bash
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

set -ex

ROOT=`pwd`

pkg-config --version

export PATH=/tools/${TOOLCHAIN}/bin:/tools/host/bin:$PATH
export PKG_CONFIG_PATH=/tools/deps/share/pkgconfig

tar -xf xextproto-${XEXTPROTO_VERSION}.tar.gz
pushd xextproto-${XEXTPROTO_VERSION}

# xextproto does not support musl targets so we pretend it is gnu
CFLAGS="${EXTRA_TARGET_CFLAGS} -fPIC" CPPFLAGS="${EXTRA_TARGET_CFLAGS} -fPIC" LDFLAGS="${EXTRA_TARGET_LDFLAGS}" ./configure \
    --build=${BUILD_TRIPLE} \
    --host="${TARGET_TRIPLE/-musl/-gnu}" \
    --prefix=/tools/deps

make -j `nproc`
make -j `nproc` install DESTDIR=${ROOT}/out
