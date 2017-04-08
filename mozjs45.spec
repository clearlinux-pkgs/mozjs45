#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mozjs45
Version  : 45.0.2
Release  : 8
URL      : https://people-mozilla.org/~sfink/mozjs-45.0.2.tar.bz2
Source0  : https://people-mozilla.org/~sfink/mozjs-45.0.2.tar.bz2
Summary  : A small but fast and easy to use stand-alone template engine written in pure python.
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause BSD-3-Clause-Clear GPL-2.0 LGPL-2.0 LGPL-2.1 MIT MPL-2.0 MPL-2.0-no-copyleft-exception Python-2.0 ZPL-2.1
Requires: mozjs45-bin
Requires: Babel
Requires: Jinja2
Requires: Sphinx
Requires: argparse
Requires: functools32
Requires: jsonschema
Requires: psutil
Requires: py
Requires: pyOpenSSL
Requires: pyasn1
Requires: pytest
Requires: pytest-cov
Requires: python-dateutil
Requires: repoze.lru
Requires: requests
Requires: setuptools
Requires: simplejson
Requires: tox
Requires: webcolors
Requires: wheel
BuildRequires : Jinja2
BuildRequires : argparse
BuildRequires : icu4c-dev
BuildRequires : nspr-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libffi)
BuildRequires : pkgconfig(x11)
BuildRequires : psutil
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : zlib-dev
Patch1: bug1329272.patch
Patch2: install-copy-files.patch
Patch3: link-mozglue.patch
Patch4: pytest.patch

%description
NSPR provides platform independence for non-GUI operating system
facilities. These facilities include threads, thread synchronization,
normal file and network I/O, interval timing and calendar time, basic
memory management (malloc and free) and shared library linking. 

See: http://www.mozilla.org/projects/nspr/about-nspr.html

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

%package bin
Summary: bin components for the mozjs45 package.
Group: Binaries

%description bin
bin components for the mozjs45 package.


%package dev
Summary: dev components for the mozjs45 package.
Group: Development
Requires: mozjs45-bin
Provides: mozjs45-devel

%description dev
dev components for the mozjs45 package.


%prep
%setup -q -n mozjs-45.0.2
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1491680445
pushd js/src
%configure --disable-static --with-x \
--with-system-zlib \
--enable-system-ffi \
--without-system-nspr \
--without-system-icu \
--without-intl-api \
--program-suffix=45
make V=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1491680445
rm -rf %{buildroot}
pushd js/src
%make_install
popd
## make_install_append content
mv %{buildroot}/usr/bin/js %{buildroot}/usr/bin/js45
mv %{buildroot}/usr/bin/js-config %{buildroot}/usr/bin/js45-config
mv %{buildroot}/usr/lib64/pkgconfig/js.pc %{buildroot}/usr/lib64/pkgconfig/mozjs45.pc
## make_install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/libjs_static.ajs

%files bin
%defattr(-,root,root,-)
/usr/bin/js45
/usr/bin/js45-config

%files dev
%defattr(-,root,root,-)
/usr/include/mozjs-45/jemalloc_types.h
/usr/include/mozjs-45/js-config.h
/usr/include/mozjs-45/js.msg
/usr/include/mozjs-45/js/CallArgs.h
/usr/include/mozjs-45/js/CallNonGenericMethod.h
/usr/include/mozjs-45/js/CharacterEncoding.h
/usr/include/mozjs-45/js/Class.h
/usr/include/mozjs-45/js/Conversions.h
/usr/include/mozjs-45/js/Date.h
/usr/include/mozjs-45/js/Debug.h
/usr/include/mozjs-45/js/GCAPI.h
/usr/include/mozjs-45/js/GCHashTable.h
/usr/include/mozjs-45/js/HashTable.h
/usr/include/mozjs-45/js/HeapAPI.h
/usr/include/mozjs-45/js/Id.h
/usr/include/mozjs-45/js/Initialization.h
/usr/include/mozjs-45/js/LegacyIntTypes.h
/usr/include/mozjs-45/js/MemoryMetrics.h
/usr/include/mozjs-45/js/Principals.h
/usr/include/mozjs-45/js/ProfilingFrameIterator.h
/usr/include/mozjs-45/js/ProfilingStack.h
/usr/include/mozjs-45/js/Proxy.h
/usr/include/mozjs-45/js/RequiredDefines.h
/usr/include/mozjs-45/js/RootingAPI.h
/usr/include/mozjs-45/js/SliceBudget.h
/usr/include/mozjs-45/js/StructuredClone.h
/usr/include/mozjs-45/js/TraceKind.h
/usr/include/mozjs-45/js/TraceableVector.h
/usr/include/mozjs-45/js/TracingAPI.h
/usr/include/mozjs-45/js/TrackedOptimizationInfo.h
/usr/include/mozjs-45/js/TypeDecls.h
/usr/include/mozjs-45/js/UbiNode.h
/usr/include/mozjs-45/js/UbiNodeBreadthFirst.h
/usr/include/mozjs-45/js/UbiNodeCensus.h
/usr/include/mozjs-45/js/UbiNodeDominatorTree.h
/usr/include/mozjs-45/js/UbiNodePostOrder.h
/usr/include/mozjs-45/js/Utility.h
/usr/include/mozjs-45/js/Value.h
/usr/include/mozjs-45/js/Vector.h
/usr/include/mozjs-45/js/WeakMapPtr.h
/usr/include/mozjs-45/jsalloc.h
/usr/include/mozjs-45/jsapi.h
/usr/include/mozjs-45/jsbytecode.h
/usr/include/mozjs-45/jsclist.h
/usr/include/mozjs-45/jscpucfg.h
/usr/include/mozjs-45/jsfriendapi.h
/usr/include/mozjs-45/jsperf.h
/usr/include/mozjs-45/jsprf.h
/usr/include/mozjs-45/jsprototypes.h
/usr/include/mozjs-45/jspubtd.h
/usr/include/mozjs-45/jstypes.h
/usr/include/mozjs-45/jsversion.h
/usr/include/mozjs-45/jswrapper.h
/usr/include/mozjs-45/mozilla/Alignment.h
/usr/include/mozjs-45/mozilla/AllocPolicy.h
/usr/include/mozjs-45/mozilla/AlreadyAddRefed.h
/usr/include/mozjs-45/mozilla/Array.h
/usr/include/mozjs-45/mozilla/ArrayUtils.h
/usr/include/mozjs-45/mozilla/Assertions.h
/usr/include/mozjs-45/mozilla/Atomics.h
/usr/include/mozjs-45/mozilla/Attributes.h
/usr/include/mozjs-45/mozilla/BinarySearch.h
/usr/include/mozjs-45/mozilla/BloomFilter.h
/usr/include/mozjs-45/mozilla/Casting.h
/usr/include/mozjs-45/mozilla/ChaosMode.h
/usr/include/mozjs-45/mozilla/Char16.h
/usr/include/mozjs-45/mozilla/CheckedInt.h
/usr/include/mozjs-45/mozilla/Compiler.h
/usr/include/mozjs-45/mozilla/Compression.h
/usr/include/mozjs-45/mozilla/DebugOnly.h
/usr/include/mozjs-45/mozilla/Decimal.h
/usr/include/mozjs-45/mozilla/Endian.h
/usr/include/mozjs-45/mozilla/EnumSet.h
/usr/include/mozjs-45/mozilla/EnumeratedArray.h
/usr/include/mozjs-45/mozilla/EnumeratedRange.h
/usr/include/mozjs-45/mozilla/FastBernoulliTrial.h
/usr/include/mozjs-45/mozilla/FloatingPoint.h
/usr/include/mozjs-45/mozilla/Function.h
/usr/include/mozjs-45/mozilla/GuardObjects.h
/usr/include/mozjs-45/mozilla/HashFunctions.h
/usr/include/mozjs-45/mozilla/IndexSequence.h
/usr/include/mozjs-45/mozilla/IntegerPrintfMacros.h
/usr/include/mozjs-45/mozilla/IntegerRange.h
/usr/include/mozjs-45/mozilla/IntegerTypeTraits.h
/usr/include/mozjs-45/mozilla/JSONWriter.h
/usr/include/mozjs-45/mozilla/Likely.h
/usr/include/mozjs-45/mozilla/LinkedList.h
/usr/include/mozjs-45/mozilla/LinuxSignal.h
/usr/include/mozjs-45/mozilla/MacroArgs.h
/usr/include/mozjs-45/mozilla/MacroForEach.h
/usr/include/mozjs-45/mozilla/MathAlgorithms.h
/usr/include/mozjs-45/mozilla/Maybe.h
/usr/include/mozjs-45/mozilla/MaybeOneOf.h
/usr/include/mozjs-45/mozilla/MemoryChecking.h
/usr/include/mozjs-45/mozilla/MemoryReporting.h
/usr/include/mozjs-45/mozilla/Move.h
/usr/include/mozjs-45/mozilla/NullPtr.h
/usr/include/mozjs-45/mozilla/NumericLimits.h
/usr/include/mozjs-45/mozilla/Opaque.h
/usr/include/mozjs-45/mozilla/Pair.h
/usr/include/mozjs-45/mozilla/PodOperations.h
/usr/include/mozjs-45/mozilla/Poison.h
/usr/include/mozjs-45/mozilla/Range.h
/usr/include/mozjs-45/mozilla/RangedArray.h
/usr/include/mozjs-45/mozilla/RangedPtr.h
/usr/include/mozjs-45/mozilla/ReentrancyGuard.h
/usr/include/mozjs-45/mozilla/RefCountType.h
/usr/include/mozjs-45/mozilla/RefCounted.h
/usr/include/mozjs-45/mozilla/RefPtr.h
/usr/include/mozjs-45/mozilla/ReverseIterator.h
/usr/include/mozjs-45/mozilla/RollingMean.h
/usr/include/mozjs-45/mozilla/SHA1.h
/usr/include/mozjs-45/mozilla/ScopeExit.h
/usr/include/mozjs-45/mozilla/Scoped.h
/usr/include/mozjs-45/mozilla/SegmentedVector.h
/usr/include/mozjs-45/mozilla/SizePrintfMacros.h
/usr/include/mozjs-45/mozilla/Snprintf.h
/usr/include/mozjs-45/mozilla/SplayTree.h
/usr/include/mozjs-45/mozilla/StackWalk.h
/usr/include/mozjs-45/mozilla/TaggedAnonymousMemory.h
/usr/include/mozjs-45/mozilla/TemplateLib.h
/usr/include/mozjs-45/mozilla/ThreadLocal.h
/usr/include/mozjs-45/mozilla/TimeStamp.h
/usr/include/mozjs-45/mozilla/ToString.h
/usr/include/mozjs-45/mozilla/Tuple.h
/usr/include/mozjs-45/mozilla/TypeTraits.h
/usr/include/mozjs-45/mozilla/TypedEnumBits.h
/usr/include/mozjs-45/mozilla/Types.h
/usr/include/mozjs-45/mozilla/UniquePtr.h
/usr/include/mozjs-45/mozilla/UniquePtrExtensions.h
/usr/include/mozjs-45/mozilla/Variant.h
/usr/include/mozjs-45/mozilla/Vector.h
/usr/include/mozjs-45/mozilla/WeakPtr.h
/usr/include/mozjs-45/mozilla/XorShift128PlusRNG.h
/usr/include/mozjs-45/mozilla/double-conversion.h
/usr/include/mozjs-45/mozilla/fallible.h
/usr/include/mozjs-45/mozilla/mozalloc.h
/usr/include/mozjs-45/mozilla/mozalloc_abort.h
/usr/include/mozjs-45/mozilla/mozalloc_oom.h
/usr/include/mozjs-45/mozilla/unused.h
/usr/include/mozjs-45/mozilla/utils.h
/usr/include/mozjs-45/mozmemory.h
/usr/include/mozjs-45/mozmemory_wrap.h
/usr/lib64/libmozjs-45.so
/usr/lib64/pkgconfig/mozjs45.pc
