#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
Name     : qt6quicktimeline
Version  : 6.7.1
Release  : 16
URL      : https://download.qt.io/official_releases/qt/6.7/6.7.1/submodules/qtquicktimeline-everywhere-src-6.7.1.zip
Source0  : https://download.qt.io/official_releases/qt/6.7/6.7.1/submodules/qtquicktimeline-everywhere-src-6.7.1.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-3.0
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
%setup -q -n qtquicktimeline-everywhere-src-6.7.1
cd %{_builddir}/qtquicktimeline-everywhere-src-6.7.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716949516
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
export SOURCE_DATE_EPOCH=1716949516
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qt6quicktimeline
cp %{_builddir}/qtquicktimeline-everywhere-src-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/qt6quicktimeline/79453f55fa8ee32d7b95581473edcbfd043e088f || :
cp %{_builddir}/qtquicktimeline-everywhere-src-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/qt6quicktimeline/7713a1753ce88f2c7e6b054ecc8e4c786df76300 || :
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

%files dev
%defattr(-,root,root,-)
/usr/include/QtQuickTimeline/6.7.1/QtQuickTimeline/private/qquickkeyframe_p.h
/usr/include/QtQuickTimeline/6.7.1/QtQuickTimeline/private/qquickkeyframedatautils_p.h
/usr/include/QtQuickTimeline/6.7.1/QtQuickTimeline/private/qquicktimeline_p.h
/usr/include/QtQuickTimeline/6.7.1/QtQuickTimeline/private/qquicktimelineanimation_p.h
/usr/include/QtQuickTimeline/6.7.1/QtQuickTimeline/private/qtquicktimelineexports_p.h
/usr/include/QtQuickTimeline/6.7.1/QtQuickTimeline/private/qtquicktimelineglobal_p.h
/usr/include/QtQuickTimeline/QtQuickTimeline
/usr/include/QtQuickTimeline/QtQuickTimelineDepends
/usr/include/QtQuickTimeline/QtQuickTimelineVersion
/usr/include/QtQuickTimeline/qtquicktimelineexports.h
/usr/include/QtQuickTimeline/qtquicktimelineglobal.h
/usr/include/QtQuickTimeline/qtquicktimelineversion.h
/usr/include/QtQuickTimelineBlendTrees/6.7.1/QtQuickTimelineBlendTrees/private/qblendanimationnode_p.h
/usr/include/QtQuickTimelineBlendTrees/6.7.1/QtQuickTimelineBlendTrees/private/qblendtreenode_p.h
/usr/include/QtQuickTimelineBlendTrees/6.7.1/QtQuickTimelineBlendTrees/private/qtimelineanimationnode_p.h
/usr/include/QtQuickTimelineBlendTrees/6.7.1/QtQuickTimelineBlendTrees/private/qtquicktimelineblendtreesexports_p.h
/usr/include/QtQuickTimelineBlendTrees/6.7.1/QtQuickTimelineBlendTrees/private/qtquicktimelineblendtreesglobal_p.h
/usr/include/QtQuickTimelineBlendTrees/QtQuickTimelineBlendTrees
/usr/include/QtQuickTimelineBlendTrees/QtQuickTimelineBlendTreesDepends
/usr/include/QtQuickTimelineBlendTrees/QtQuickTimelineBlendTreesVersion
/usr/include/QtQuickTimelineBlendTrees/qtquicktimelineblendtreesexports.h
/usr/include/QtQuickTimelineBlendTrees/qtquicktimelineblendtreesglobal.h
/usr/include/QtQuickTimelineBlendTrees/qtquicktimelineblendtreesversion.h
/usr/lib64/cmake/Qt6BuildInternals/StandaloneTests/QtQuickTimelineTestsConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelineblendtreespluginAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelineblendtreespluginConfig.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelineblendtreespluginConfigVersion.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelineblendtreespluginConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelineblendtreespluginTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6Qml/QmlPlugins/Qt6qtquicktimelineblendtreespluginTargets.cmake
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
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesAdditionalTargetInfo.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesConfig.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesConfigVersion.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesConfigVersionImpl.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesDependencies.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesTargets.cmake
/usr/lib64/cmake/Qt6QuickTimelineBlendTrees/Qt6QuickTimelineBlendTreesVersionlessTargets.cmake
/usr/lib64/libQt6QuickTimeline.prl
/usr/lib64/libQt6QuickTimeline.so
/usr/lib64/libQt6QuickTimelineBlendTrees.prl
/usr/lib64/libQt6QuickTimelineBlendTrees.so
/usr/lib64/pkgconfig/Qt6QuickTimeline.pc
/usr/lib64/pkgconfig/Qt6QuickTimelineBlendTrees.pc
/usr/lib64/qt6/mkspecs/modules/qt_lib_quicktimeline.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quicktimeline_private.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quicktimelineblendtrees.pri
/usr/lib64/qt6/mkspecs/modules/qt_lib_quicktimelineblendtrees_private.pri

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libQt6QuickTimeline.so.6.7.1
/V3/usr/lib64/libQt6QuickTimelineBlendTrees.so.6.7.1
/V3/usr/lib64/qt6/qml/QtQuick/Timeline/BlendTrees/libqtquicktimelineblendtreesplugin.so
/V3/usr/lib64/qt6/qml/QtQuick/Timeline/libqtquicktimelineplugin.so
/usr/lib64/libQt6QuickTimeline.so.6
/usr/lib64/libQt6QuickTimeline.so.6.7.1
/usr/lib64/libQt6QuickTimelineBlendTrees.so.6
/usr/lib64/libQt6QuickTimelineBlendTrees.so.6.7.1
/usr/lib64/qt6/metatypes/qt6quicktimeline_relwithdebinfo_metatypes.json
/usr/lib64/qt6/metatypes/qt6quicktimelineblendtrees_relwithdebinfo_metatypes.json
/usr/lib64/qt6/modules/QuickTimeline.json
/usr/lib64/qt6/modules/QuickTimelineBlendTrees.json
/usr/lib64/qt6/qml/QtQuick/Timeline/BlendTrees/libqtquicktimelineblendtreesplugin.so
/usr/lib64/qt6/qml/QtQuick/Timeline/BlendTrees/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/Timeline/BlendTrees/qmldir
/usr/lib64/qt6/qml/QtQuick/Timeline/libqtquicktimelineplugin.so
/usr/lib64/qt6/qml/QtQuick/Timeline/plugins.qmltypes
/usr/lib64/qt6/qml/QtQuick/Timeline/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qt6quicktimeline/7713a1753ce88f2c7e6b054ecc8e4c786df76300
/usr/share/package-licenses/qt6quicktimeline/79453f55fa8ee32d7b95581473edcbfd043e088f
