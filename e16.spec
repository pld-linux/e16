Summary:	Enlightenment Window Manager
Summary(pl):	X Window menad¿er - Enlightenment  
Name:		enlightenment
Version:	0.16.5
Release:	4
License:	GPL
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://ftp.enlightenment.org/pub/enlightenment/enlightenment/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.RunWM
Source3:	%{name}.wm_style
Patch0:		%{name}-config-path.patch
Patch1:		%{name}-makefile_fix.patch
Patch2:		%{name}-ac_am_fixes.patch
URL:		http://www.enlightenment.org/
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

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_wmpropsdir	%{_datadir}/wm-properties
%define		_sysconfdir	/etc/X11/enlightenment

%description
Enlightenment is a Windowmanager for X-Windows that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym
window-menad¿erem jaki kiedykolwiek zosta³ stworzony dla Linuxa ;)

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
rm -f missing
automake -a -c
CFLAGS="-I%{_includedir}/freetype %{rpmcflags}"
%configure \
	--enable-sound

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_wmpropsdir},/etc/sysconfig/wmstyle}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names
install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}

gzip -9nf AUTHORS README NEWS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%config %{_sysconfdir}
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%attr(755,root,root) %{_bindir}/*
%{_datadir}/enlightenment
%{_wmpropsdir}/*
%{_mandir}/man1/*
