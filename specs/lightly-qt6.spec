%global kf6_version 6.2.0
%define qt6_version 6.6.0
%define kf5_version 5.102.0
%define qt5_version 5.15.2
%define dev Bali10050
%define style Lightly
%define _style lightly
%define version 0.5.9

Name:           %{_style}-qt6
Version:        %{version}
Release:        0
Summary:        A modern style for qt applications
License:        GPL-3.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/%{dev}/%{style}
Source0:        https://github.com/%{dev}/%{style}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  cmake >= 3.16
BuildRequires:  fdupes
BuildRequires:  gettext

BuildRequires:  extra-cmake-modules >= %{kf6_version}
BuildRequires:  kf5-rpm-macros
BuildRequires:  kf6-rpm-macros

#lightly5 dependencies
BuildRequires:  cmake(KF5Config) >= %{kf5_version}
BuildRequires:  cmake(KF5ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5FrameworkIntegration) >= %{kf5_version}
BuildRequires:  cmake(KF5GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF5I18n) >= %{kf5_version}
BuildRequires:  cmake(KF5IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF5Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt5Widgets) >= %{qt5_version}

#lightly6 dependencies
BuildRequires:  cmake(KF6ColorScheme) >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6FrameworkIntegration) >= %{kf6_version}
BuildRequires:  cmake(KF6GuiAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6KCMUtils) >= %{kf6_version}
BuildRequires:  cmake(KF6KirigamiPlatform) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_version}
BuildRequires:  cmake(Qt6Quick) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}

BuildRequires:  cmake(KDecoration2)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

BuildRequires:  kwin-devel
BuildRequires:  libepoxy-devel
BuildRequires:  kf6-kpackage-devel >= %{kf6_version}


%description
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release -DBUILD_TESTING=OFF -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%cmake_build

%install
%cmake_install


%fdupes %{buildroot}/%{_prefix}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.md

%{_libdir}/lib%{_style}common5.so.*
%{_libdir}/lib%{_style}common6.so.*
%{_datadir}/applications/%{_style}styleconfig.desktop
%{_datadir}/applications/kcm_%{_style}decoration.desktop
%{_datadir}/kservices6/%{_style}decorationconfig.desktop
%dir %{_kf6_qtplugindir}
%dir %{_kf6_qtplugindir}/org.kde.kdecoration2.kcm
%{_kf6_qtplugindir}/org.kde.kdecoration2.kcm/kcm_%{_style}decoration.so
%dir %{_kf6_qtplugindir}/org.kde.kdecoration2/
%{_kf6_qtplugindir}/org.kde.kdecoration2/org.kde.%{_style}.so
%dir %{_kf6_qtplugindir}/kstyle_config
%{_kf6_qtplugindir}/kstyle_config/%{_style}styleconfig.so
%dir %{_kf5_qtplugindir}/styles
%{_kf5_qtplugindir}/styles/%{_style}5.so
%dir %{_kf6_qtplugindir}/styles
%{_kf6_qtplugindir}/styles/%{_style}6.so
%dir %{_datadir}/kstyle
%dir %{_datadir}/kstyle/themes
%{_datadir}/kstyle/themes/%{_style}.themerc
%{_bindir}/%{_style}-settings6
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_datadir}/icons/hicolor/scalable/apps/%{_style}-settings.svgz
%dir %{_datadir}/color-schemes/
%{_datadir}/color-schemes/%{style}.colors
%{_libdir}/cmake/%{style}/

%changelog
%autochangelog

