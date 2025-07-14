#
# Conditional build:
%bcond_with	gnome2		# build with support for GNOME2 wm-properties
#
Summary:	Enlightenment Window Manager
Summary(pl.UTF-8):	Zarządca okien X - Enlightenment
Summary(de.UTF-8):	Enlightenment ist ein Window Manager für X
Name:		e16
Version:	0.16.8.2
Release:	0.1
License:	BSD
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	03c0ffd785957a61af40e4d6d045c9b5
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
Source3:	%{name}-e_gen_menu
Source4:	%{name}-e_check_menu
Patch0:		%{name}-edirconf.patch
Patch1:		%{name}-ac_am_fixes.patch
Patch2:		%{name}-pl.patch
Patch3:		%{name}-check_menus.patch
Patch4:		%{name}-winter-i18n.patch
URL:		http://enlightenment.org/
BuildRequires:	XFree86
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.17
BuildRequires:	fnlib-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext-tools
BuildRequires:	giflib-devel
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	iconv
BuildRequires:	imlib2-devel >= 1.2.2
BuildRequires:	libghttp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel
Requires:	ImageMagick-coder-png
Requires:	vfmg >= 0.9.95
Obsoletes:	enlightenment <= 0.16.7.2
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/gnome/wm-properties
%define		_sysconfdir	/etc/X11/%{name}

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl.UTF-8
Enlightenment jest najpotężniejszym i najpiękniejszym zarządcą okien
jaki kiedykolwiek został stworzony dla Linuksa ;)

%description -l de.UTF-8
Enlightenment ist ein Window Manager für X. Sein Designziel ist es, so
konfigurierbar wie nur möglich in den Bereichen Aussehen und Bedienung
zu sein. Das derzeitige Design von Enlightenment steuert darauf hin,
ein "vernünftiger" Desktop zu werden, das bedeutet, es verwaltet
Anwendungsfenster, zudem wird in der Lage sein, Anwendungen zu starten
und Dateien zu verwalten.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
#%%patch2 -p1 	XXX: needs update
%patch -P3 -p1
mkdir themes/winter
tar -C themes/winter -zxf themes/winter.etheme
%patch -P4 -p1
rm themes/winter/fonts.cfg.*

mv -f po/{no,nb}.po
rm po/*.gmo

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
export LOCALEDIR=%{_datadir}/locale
%configure \
	--enable-sound=yes

# regenerate gmo files
%{__make} -C po update-gmo
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir},/etc/sysconfig/wmstyle}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{?with_gnome2:install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}}
install %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop
install %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/e_gen_menu
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts/e_check_menu

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%config %{_sysconfdir}
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/[!s]*
%dir %{_datadir}/%{name}/scripts
%attr(755,root,root) %{_datadir}/%{name}/scripts/*
%{_datadir}/xsessions/%{name}.desktop
%{?with_gnome2:%{_wmpropsdir}/*}
