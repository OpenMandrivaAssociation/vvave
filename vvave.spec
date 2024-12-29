#define snapshot 20220107

Name:		vvave
Summary:	Vvave Media Player
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}2
Group:		Graphical desktop/KDE
License:	GPLv2
Url:		https://vvave.kde.org/
Source0:	https://invent.kde.org/maui/vvave/-/archive/%{?snapshot:master/vvave-master.tar.bz2#/vvave-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/vvave-v%{version}.tar.bz2}
Patch0:   https://invent.kde.org/maui/vvave/-/merge_requests/25.patch
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Multimedia)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6WebView)
BuildRequires:	cmake(Qt6WebChannel)
BuildRequires:	cmake(Qt6WebEngineCore)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6WebEngineWidgets)
BuildRequires:	cmake(Qt6WebSockets)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(Taglib)
BuildRequires:	pkgconfig(taglib)
BuildRequires:	cmake(MauiKit4)
BuildRequires:  cmake(MauiKitAccounts4)
BuildRequires:	cmake(MauiKitFileBrowsing4)

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

%find_lang vvave

%files -f vvave.lang
%doc README.md
%{_bindir}/%{name}
%{_iconsdir}/hicolor/*/apps/*.svg
%{_datadir}/applications/org.kde.vvave.desktop
%{_datadir}/metainfo/org.kde.vvave.appdata.xml
