Summary:	Enlightenment Window Manager
Summary(pl):	X Window menad¿er - Enlightenment  
Name:		enlightenment
Version:	0.15.0
Release:	3d
%define		date	19990203		
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz±dcy okien
#######		ftp://www.rasterman.com/pub/enlightenment
Source:		%{name}-%{version}-%{date}.tar.gz
URL:		http://www.rasterman.com/
Requires:	imlib >= 1.9.2
Requires:	fnlib >= 0.4
Requires:	libpng
Requires:	libtiff
Requires:	libjpeg
Requires:	zlib
Requires:	libgr-progs
Requires:	glib = 1.1.15
Requires:	gtk+ = 1.1.15
Requires:	libungif
Requires:	ImageMagick
Requires:	esound	 >= 0.2.7
Requires:	freetype >= 1.2
Requires:	Gtk-perl >= 0.5000
Requires:	stringlist >= 0.3
BuildRoot:	/tmp/buildroot-%{name}-%{version}

%description
Enlightenment is a Windowmanager for X-Windows that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym window-menad¿erem 
jaki kiedykolwiek zosta³ stworzony dla Linuxa ;)

%prep
%setup -q 

%build
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
    ./configure \
	--prefix=/usr/X11R6 \
	--enable-sound
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/X11R6/bin

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install


ln -s	/usr/X11R6/enlightenment/bin/enlightenment \
	$RPM_BUILD_ROOT/usr/X11R6/bin

bzip2 -9 AUTHORS README NEWS 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.bz2 README.bz2 NEWS.bz2 

%dir /usr/X11R6/enlightenment

%attr(755,root,root) /usr/X11R6/enlightenment/bin/*

%config /usr/X11R6/enlightenment/config
%config /usr/X11R6/enlightenment/themes
/usr/X11R6/enlightenment/E-docs

%attr(755,root,root) /usr/X11R6/bin/*

%changelog
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
