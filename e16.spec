Summary:     Enlightenment Window Manager
Summary(pl): X Window menad¿er - Enlightenment  
Name:        enlightenment
Version:     0.15.0
Release:     1
Copyright:   GPL
Group:       X11/Applications
Source:      ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.tar.gz
Patch0:      enlightenment-DESTDIR.patch
Requires:    esound = 0.2.7, freetype = 1.2, fnlib = 0.4
Requires:    imlib = 1.8.2, perl >= 5.005
URL:         http://www.rasterman.com/
BuildRoot:   /tmp/%{name}-%{version}-root

%description
Enlightenment is a Windowmanager for X-Windows that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym window-menad¿erem 
jaki kiedykolwiek zosta³ stworzony dla Linuxa ;)

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc AUTHORS README TODO NEWS
%dir /usr/X11R6/enlightenment
/usr/X11R6/enlightenment/E-docs
%dir /usr/X11R6/enlightenment/bin
%attr(755, root, root) /usr/X11R6/enlightenment/bin/*
/usr/X11R6/enlightenment/config
/usr/X11R6/enlightenment/themes

%changelog
* Tue Jan 05 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.15.0-1]
- more Requires (fnlib = 0.4, imlib = 1.8.2, esound = 0.2.7,
  freetype = 1.2),
- updates in %files for 0.15.0,
- added LDFLAGS="-s" to ./configure enviroment.

* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.14-2]
- added pl translation,
- minor modifications of spec file.

* Tue Jun 2 1998 The Rasterman <raster@redhat.com>
- wrote .spec file
