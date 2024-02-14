#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: da8b975
#
Name     : qt6quicktimeline
Version  : 6.6.2
Release  : 8
URL      : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtquicktimeline-everywhere-src-6.6.2.tar.xz
Source0  : https://download.qt.io/official_releases/qt/6.6/6.6.2/submodules/qtquicktimeline-everywhere-src-6.6.2.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.3 GPL-3.0
Requires: qt6quicktimeline-lib = %{version}-%{release}
Requires: qt6quicktimeline-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : qt6base-dev
BuildRequires : qt6declarative-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description


%package dev
Summary: dev components for the qt6quicktimeline package.
Group: Development
Requires: qt6quicktimeline-lib = %{version}-%{release}
Provides: qt6quicktimeline-devel = %{version}-%{release}
Requires: qt6quicktimeline = %{version}-%{release}

%description dev
dev components for the qt6quicktimeline package.


%package lib
Summary: lib components for the qt6quicktimeline package.
Group: Libraries
Requires: qt6quicktimeline-license = %{version}-%{release}

%description lib
lib components for the qt6quicktimeline package.


%package license
Summary: license components for the qt6quicktimeline package.
Group: Default

%description license
license components for the qt6quicktimeline package.


%prep
%setup -q -n qtquicktimeline-everywhere-src-6.6.2
cd %{_builddir}/qtquicktimeline-everywhere-src-6.6.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707942909
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1707942909
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6quicktimeline
cp %{_builddir}/qtquicktimeline-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6quicktimeline/b073f11f0c81a95ab5e32aa6b5d23a5955a95274 || :
cp %{_builddir}/qtquicktimeline-everywhere-src-%{version}/LICENSES/GFDL-1.3-no-invariants-only.txt %{buildroot}/usr/share/package-licenses/qt6quicktimeline/715f995f11805ee85601834220c43b082f457ea3 || :
cp %{_builddir}/qtquicktimeline-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6quicktimeline/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/qt6/metatypes/qt6quicktimeline_relwithdebinfo_metatypes.json
/usr/lib64/qt6/mkspecs/modules/qt_lib_quicktimeline.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quicktimeline_private.pri
/usr/lib64/qt6/modules/QuickTimeline.json
/usr/lib64/qt6/qml/QtQuick/Timeline/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/Timeline/qmldir

%files dev
%defattr(-,root,root,-)
/usr/include/QtQuickTimeline/6.6.2/QtQuickTimeline/private/qquickkeyframe_p.h
/usr/include/QtQuickTimeline/6.6.2/QtQuickTimeline/private/qquickkeyframedatautils_p.h
/usr/include/QtQuickTimeline/6.6.2/QtQuickTimeline/private/qquicktimeline_p.h
/usr/include/QtQuickTimeline/6.6.2/QtQuickTimeline/private/qquicktimelineanimation_p.h
/usr/include/QtQuickTimeline/6.6.2/QtQuickTimeline/private/qtquicktimelineexports_p.h
/usr/include/QtQuickTimeline/6.6.2/QtQuickTimeline/private/qtquicktimelineglobal_p.h
/usr/include/QtQuickTimeline/QtQuickTimeline
/usr/include/QtQuickTimeline/QtQuickTimelineDepends
/usr/include/QtQuickTimeline/QtQuickTimelineVersion
/usr/include/QtQuickTimeline/qtquicktimelineexports.h
/usr/include/QtQuickTimeline/qtquicktimelineglobal.h
/usr/include/QtQuickTimeline/qtquicktimelineversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtQuickTimelineTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelinepluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelinepluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelinepluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelinepluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelinepluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelinepluginTargets.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineConfig.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineConfigVersion.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineDependencies.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineTargets.cmake
/usr/lib64/cmake/Qt6QuickTimeline/Qt6QuickTimelineVersionlessTargets.cmake
/usr/lib64/libQt6QuickTimeline.prl
/usr/lib64/libQt6QuickTimeline.so
/usr/lib64/pkgconfig/Qt6QuickTimeline.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6QuickTimeline.so.6.6.2
/V3/usr/lib64/qt6/qml/QtQuick/Timeline/libqtquicktimelineplugin.so
/usr/lib64/libQt6QuickTimeline.so.6
/usr/lib64/libQt6QuickTimeline.so.6.6.2
/usr/lib64/qt6/qml/QtQuick/Timeline/libqtquicktimelineplugin.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6quicktimeline/715f995f11805ee85601834220c43b082f457ea3
/usr/share/package-licenses/qt6quicktimeline/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/qt6quicktimeline/b073f11f0c81a95ab5e32aa6b5d23a5955a95274
