Summary:     Enlightenment Window Manager
Summary(pl): X Window menad¿er - Enlightenment  
Name:        enlightenment
Version:     0.14
Release:     2
Copyright:   GPL
Group:       X11/Applications
Source:      ftp://www.rasterman.com/pub/enlightenment/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root
URL:         http://www.rasterman.com/
Requires:    perl >= 5.005

%description
Enlightenment is a Windowmanager for X-Windows that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym window-menad¿erem 
jaki kiedykolwiek zosta³ stworzony dla Linuxa ;)

%prep
%setup -q -n e

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=/usr/X11R6
make

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr/X11R6 install
strip $RPM_BUILD_ROOT/usr/X11R6/enlightenment/bin/* || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc doc/AUTHORS doc/README doc/FAQ
%dir /usr/X11R6/enlightenment
%dir /usr/X11R6/enlightenment/bin
%attr(755, root, root) /usr/X11R6/enlightenment/bin/ConfigEdit
%attr(755, root, root) /usr/X11R6/enlightenment/bin/enlightenment
%attr(755, root, root) /usr/X11R6/enlightenment/bin/dox
/usr/X11R6/enlightenment/config
/usr/X11R6/enlightenment/E-docs
%dir /usr/X11R6/enlightenment/themes
%attr(755, root, root) /usr/X11R6/bin/*

%changelog
* Mon Jul 20 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.14-2]
- added pl translation,
- minor modifications of spec file.

* Tue Jun 2 1998 The Rasterman <raster@redhat.com>
- wrote .spec file
