Summary:	Enlightenment Window Manager
Summary(pl):	X Window menad¿er - Enlightenment  
Name:		enlightenment
Version:	0.16.5
Release:	1
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
URL:		http://www.enlightenment.org/
BuildRequires:	gtk+-devel >= 1.2.1
BuildRequires:	esound-devel >= 0.2.13
BuildRequires:	imlib-devel >= 1.9.8
BuildRequires:	gettext-devel 
BuildRequires:	freetype-devel
BuildRequires:	libghttp-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng >= 1.0.8
BuildRequires:	libtiff-devel
BuildRequires:	libungif-devel
BuildRequires:	zlib-devel
BuildRequires:	fnlib-devel
Requires:	xinitrc >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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

%build
gettextize --copy --force
CFLAGS="-I%{_includedir}/freetype %{!?debug:$RPM_OPT_FLAGS}%{?debug:-O -g}"
%configure \
	--enable-fsstd \
	--enable-sound

%{__make} configdatadir=%{_sysconfdir}/X11/enlightenment

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties \
	$RPM_BUILD_ROOT/etc/sysconfig/wmstyle

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	configdatadir=%{_sysconfdir}/X11/enlightenment

install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.sh
install %{SOURCE3} $RPM_BUILD_ROOT/etc/sysconfig/wmstyle/%{name}.names
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties

gzip -9nf AUTHORS README NEWS \

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%dir %{_sysconfdir}/X11/enlightenment
%config %{_sysconfdir}/X11/enlightenment/*
%attr(755,root,root) /etc/sysconfig/wmstyle/*.sh
/etc/sysconfig/wmstyle/*.names
%attr(755,root,root) %{_bindir}/*
%{_datadir}/enlightenment
%{_datadir}/gnome/wm-properties/*
%{_mandir}/man1/*
