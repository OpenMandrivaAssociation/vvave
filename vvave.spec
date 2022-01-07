%define snapshot 20220107

Name:		vvave
Summary:	Vvave Media Player
Version:	2.1.1
Release:	%{?snapshot:0.%{snapshot}.}1
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://vvave.kde.org/
Source0:	https://invent.kde.org/maui/vvave/-/archive/%{?snapshot:master/vvave-master.tar.bz2#/vvave-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/vvave-v%{version}.tar.bz2}
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Multimedia)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5WebView)
BuildRequires:	cmake(Qt5WebChannel)
BuildRequires:	cmake(Qt5WebEngineCore)
BuildRequires:	cmake(Qt5PrintSupport)
BuildRequires:	cmake(Qt5WebEngineWidgets)
BuildRequires:	cmake(Qt5WebSockets)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(Taglib)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(MauiKit)
BuildRequires:  cmake(MauiKitAccounts)

Requires: gstreamer1.0-plugins-base
Requires: gstreamer1.0-plugins-good
Requires: gstreamer1.0-plugins-bad
Requires: gstreamer1.0-plugins-ugly
Requires: gstreamer1.0-libav

%description
Vvave will handle your whole music collection
by retreaving semantic information from the web.

Just relax, enjoy and discover your new music 

%prep
%autosetup -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}} -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%doc README.md
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/applications/org.kde.vvave.desktop
%{_datadir}/metainfo/org.kde.vvave.appdata.xml
