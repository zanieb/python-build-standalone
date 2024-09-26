#!/usr/bin/env bash
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

set -e

cd /build

export PATH=/tools/${TOOLCHAIN}/bin:/tools/host/bin:$PATH
export CC=clang
export CFLAGS="-fPIC"

tar -xf musl-${MUSL_VERSION}.tar.gz

pushd musl-${MUSL_VERSION}

# Debian as of at least bullseye ships musl 1.2.1. musl 1.2.2
# added reallocarray(), which gets used by at least OpenSSL.
# Here, we disable this single function so as to not introduce
# symbol dependencies on clients using an older musl version.
patch -p1 <<EOF
diff --git a/include/stdlib.h b/include/stdlib.h
index b507ca3..8259e27 100644
--- a/include/stdlib.h
+++ b/include/stdlib.h
@@ -147,7 +147,6 @@ int getloadavg(double *, int);
 int clearenv(void);
 #define WCOREDUMP(s) ((s) & 0x80)
 #define WIFCONTINUED(s) ((s) == 0xffff)
-void *reallocarray (void *, size_t, size_t);
 void qsort_r (void *, size_t, size_t, int (*)(const void *, const void *, void *), void *);
 #endif
 
diff --git a/src/malloc/reallocarray.c b/src/malloc/reallocarray.c
deleted file mode 100644
index 4a6ebe4..0000000
--- a/src/malloc/reallocarray.c
+++ /dev/null
@@ -1,13 +0,0 @@
-#define _BSD_SOURCE
-#include <errno.h>
-#include <stdlib.h>
-
-void *reallocarray(void *ptr, size_t m, size_t n)
-{
-	if (n && m > -1 / n) {
-		errno = ENOMEM;
-		return 0;
-	}
-
-	return realloc(ptr, m * n);
-}
EOF

./configure \
    --prefix=/tools/host \
    --disable-shared

make -j `nproc`
make -j `nproc` install DESTDIR=/build/out

popd
