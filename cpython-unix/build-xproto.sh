#!/usr/bin/env bash
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

set -ex

ROOT=`pwd`

pkg-config --version

export PATH=${TOOLS_PATH}/${TOOLCHAIN}/bin:${TOOLS_PATH}/host/bin:$PATH
export PKG_CONFIG_PATH=${TOOLS_PATH}/deps/share/pkgconfig

tar -xf xproto-${XPROTO_VERSION}.tar.gz
pushd xproto-${XPROTO_VERSION}

# xproto does not support musl targets so we pretend it is gnu
CFLAGS="${EXTRA_TARGET_CFLAGS} -fPIC" CPPFLAGS="${EXTRA_TARGET_CFLAGS} -fPIC" LDFLAGS="${EXTRA_TARGET_LDFLAGS}" ./configure \
    --build=${BUILD_TRIPLE} \
    --host="${TARGET_TRIPLE/-musl/-gnu}" \
    --prefix=/tools/deps \
    ac_cv_prog_cc_works=yes \
    ac_cv_prog_cxx_works=yes \
    ac_cv_func_malloc_0_nonnull=yes \
    ac_cv_func_memset=yes \
    ac_cv_func_calloc=yes \
    ac_cv_func_realloc=yes \
    ac_cv_func_memcpy=yes \
    ac_cv_func_strchr=yes \
    ac_cv_func_strrchr=yes \
    ac_cv_func_strcmp=yes \
    ac_cv_func_strncpy=yes \
    ac_cv_func_strlen=yes \
    --disable-option-checking

make -j ${NUM_CPUS}
make -j ${NUM_CPUS} install DESTDIR=${ROOT}/out
