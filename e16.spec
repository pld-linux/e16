Summary:	Enlightenment Window Manager
Summary(pl):	X Window menad¿er - Enlightenment  
Name:		enlightenment
Version:	0.16
Release:	0.2
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy okien
Source:		ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.devel.2.tar.gz
Patch:		enlightenment-config-path.patch
URL:		http://www.rasterman.com/
Requires:	glib >= 1.2.1
Requires:	gtk+ >= 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Enlightenment is a Windowmanager for X-Windows that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym window-menad¿erem 
jaki kiedykolwiek zosta³ stworzony dla Linuxa ;)

%prep
%setup -q -n %{name}-%{version}.devel.2
%patch -p1

%build
%configure \
	--enable-fsstd \
	--enable-sound

make configdatadir=/etc/X11/enlightenment

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/bin

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	configdatadir=/etc/X11/enlightenment

gzip -9nf AUTHORS README NEWS 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,NEWS}.gz
%attr(755,root,root) /usr/X11R6/bin/*
/usr/X11R6/share/enlightenment

%dir /etc/X11/enlightenment
%config /etc/X11/enlightenment/*

%changelog
* Sun Mar 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.15.4-4]
- aadded --enable-fsstd to ./configure parameters,
- gzipping %doc (instead bzipping2),
- config files moved to /etc/X11/enlightenment,
- removed Requires (autogenerate).

* Sat Feb  6 1999 Micha³ Kuratczyk <kurkens@polbox.com>
  [0.15.0-3d]
- added %config macros
- changed Group to X11/Window Managers
- changed BuildRoot to /tmp/buildroot-%%{name}-%%{version}

* Fri Feb 05 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.15.0-2.1d]
- updated to latest snapshoot,
- added Require: stringlist, Gtk-prel.

* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.14-2d]
- build against glibc-2.1,
- translation modified for pl,
- added Require: Gtk-perl,
- minor modifications of spec file.

* Tue Jun 2 1998 The Rasterman <raster@redhat.com>
- wrote .spec file
