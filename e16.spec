# TODO:
#	- fix attempts to use bogus path (differentiate absolute and relative
#	  pathnames)
#	- fix applnk submenu handling (for Ra)
#	- use the translated (locale dependent) script menu generating (???)
#
Summary:	Enlightenment Window Manager
Summary(pl):	Zarz±dca okien X - Enlightenment
Name:		enlightenment
Version:	0.16.6
Release:	2
License:	GPL
Group:		X11/Window Managers
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	fa1b5f062cd2ba005eb555c358450deb
Source1:	%{name}.desktop
Source2:	%{name}.RunWM
Source3:	%{name}.wm_style
Source4:	%{name}-xsession.desktop
Patch0:		%{name}-config-path.patch
Patch1:		%{name}-makefile_fix.patch
Patch2:		%{name}-ac_am_fixes.patch
Patch3:		%{name}-use_sys_snprintf.patch
Patch4:		%{name}-pl.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel >= 0.2.13
BuildRequires:	fnlib-devel
BuildRequires:	freetype1-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	imlib-devel >= 1.9.8
BuildRequires:	libghttp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libtool
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
Requires:	xinitrc >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_sysconfdir	/etc/X11/enlightenment

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym zarz±dc± okien
jaki kiedykolwiek zosta³ stworzony dla Linuksa ;)

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
CFLAGS="-I%{_includedir}/freetype %{rpmcflags}"
%configure \
	--enable-sound=yes

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xsessions,%{_wmpropsdir},/etc/sysconfig/wmstyle}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names
install %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README NEWS
%config %{_sysconfdir}
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/enlightenment
%{_datadir}/enlightenment/[!s]*
%attr(755,root,root) %{_datadir}/enlightenment/scripts
%{_datadir}/xsessions/%{name}.desktop
%{_wmpropsdir}/*
%{_mandir}/man1/*
