# Credits: hazel-bunny (https://github.com/hazel-bunny)

%define style Lightly
%define _style lightly
%define dev Bali10050
%define _qt_major_version 6
%define _qt5_major_version 5
%define qt5_version 5.15.2
%define kf5_version 5.102.0
%define release_tag 0.5.11

Name:           %{_style}-qt%{_qt_major_version}
Version:        %{release_tag}
Release:        1%{?dist}
Summary:        A modern style for qt applications
License:        GPL-2.0-or-later
Group:          System/GUI/KDE

URL:            https://github.com/%{dev}/%{style}
Source0:        https://github.com/%{dev}/%{style}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.240.0
BuildRequires:  fdupes
BuildRequires:  gettext

# kf5
BuildRequires:  kf%{_qt5_major_version}-rpm-macros

BuildRequires:  kf%{_qt_major_version}-rpm-macros
BuildRequires:  kf%{_qt_major_version}-filesystem

BuildRequires:  cmake(Qt%{_qt_major_version}Core)
BuildRequires:  cmake(Qt%{_qt_major_version}DBus)
BuildRequires:  cmake(Qt%{_qt_major_version}Gui)
BuildRequires:  cmake(Qt%{_qt_major_version}Quick)
BuildRequires:  cmake(Qt%{_qt_major_version}UiTools)
BuildRequires:  cmake(Qt%{_qt_major_version}Widgets)

BuildRequires:  cmake(KF%{_qt_major_version}CoreAddons)
BuildRequires:  cmake(KF%{_qt_major_version}Config)
BuildRequires:  cmake(KF%{_qt_major_version}ConfigWidgets)
BuildRequires:  cmake(KF%{_qt_major_version}Crash)
BuildRequires:  cmake(KF%{_qt_major_version}FrameworkIntegration)
BuildRequires:  cmake(KF%{_qt_major_version}GuiAddons)
BuildRequires:  cmake(KF%{_qt_major_version}GlobalAccel)
BuildRequires:  cmake(KF%{_qt_major_version}I18n)
BuildRequires:  cmake(KF%{_qt_major_version}IconThemes)
BuildRequires:  cmake(KF%{_qt_major_version}KCMUtils)
BuildRequires:  cmake(KF%{_qt_major_version}KIO)
BuildRequires:  cmake(KF%{_qt_major_version}Kirigami2)
BuildRequires:  cmake(KF%{_qt_major_version}Notifications)
BuildRequires:  cmake(KF%{_qt_major_version}Package)
BuildRequires:  cmake(KF%{_qt_major_version}WindowSystem)

#lightly5 dependencies
BuildRequires:  cmake(KF%{_qt5_major_version}KCMUtils)
BuildRequires:  cmake(KF%{_qt5_major_version}Config) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}ConfigWidgets) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}CoreAddons) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}FrameworkIntegration) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}GuiAddons) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}I18n) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}IconThemes) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}Kirigami2) >= %{kf5_version}
BuildRequires:  cmake(KF%{_qt5_major_version}WindowSystem) >= %{kf5_version}
BuildRequires:  cmake(Qt%{_qt5_major_version}DBus) >= %{qt5_version}
BuildRequires:  cmake(Qt%{_qt5_major_version}Quick) >= %{qt5_version}
BuildRequires:  cmake(Qt%{_qt5_major_version}Widgets) >= %{qt5_version}

BuildRequires:  cmake(KDecoration2)
BuildRequires:  cmake(KWayland)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Plasma5Support)

BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb)

BuildRequires:  kwin-devel
BuildRequires:  libepoxy-devel
BuildRequires:  kf%{_qt_major_version}-kpackage-devel

Obsoletes:      %{_style} <= %{version}

%description
Lightly is a fork of breeze theme style that aims to be visually modern and minimalistic.

%prep
%autosetup -n %{style}-%{version} -p1

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

%{_bindir}/lightly-settings%{_qt_major_version}

%{_libdir}/cmake/%{style}/
%{_libdir}/lib%{_style}common%{_qt_major_version}.so.*
%{_libdir}/lib%{_style}common%{_qt5_major_version}.so.*

%{_qt6_plugindir}/kstyle_config/%{_style}styleconfig.so
%{_qt6_plugindir}/org.kde.kdecoration2/org.kde.%{_style}.so
%{_qt6_plugindir}/org.kde.kdecoration2.kcm/kcm_%{_style}decoration.so
%{_qt6_plugindir}/styles/%{_style}%{_qt_major_version}.so
%dir %{_kf5_qtplugindir}/styles
%{_kf5_qtplugindir}/styles/%{_style}%{_qt5_major_version}.so

%{_datadir}/applications/kcm_%{_style}decoration.desktop
%{_datadir}/applications/%{_style}styleconfig.desktop
%{_datadir}/color-schemes/%{style}.colors
%{_datadir}/icons/hicolor/scalable/apps/%{_style}-settings.svgz
%{_datadir}/kservices%{_qt_major_version}/%{_style}decorationconfig.desktop
%{_datadir}/kstyle/themes/%{_style}.themerc

%changelog
%autochangelog
