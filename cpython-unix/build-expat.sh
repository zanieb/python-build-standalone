#!/usr/bin/env bash
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

set -ex

ROOT=`pwd`

export PATH=${TOOLS_PATH}/${TOOLCHAIN}/bin:${TOOLS_PATH}/host/bin:$PATH

tar -xf expat-${EXPAT_VERSION}.tar.xz

pushd expat-${EXPAT_VERSION}

# xmlwf isn't needed by CPython.
# Disable -fexceptions because we don't need it and it adds a dependency on libgcc_s, which
# is softly undesirable.
CFLAGS="${EXTRA_TARGET_CFLAGS} -fPIC" CPPFLAGS="${EXTRA_TARGET_CFLAGS} -fPIC" ./configure \
    --build=${BUILD_TRIPLE} \
    --host=${TARGET_TRIPLE} \
    --prefix=/tools/deps \
    --disable-shared \
    --without-examples \
    --without-tests \
    --without-xmlwf \
    ax_cv_check_cflags___fexceptions=no \
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
