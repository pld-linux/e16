Summary:	Enlightenment Window Manager
Summary(pl):	X Window menad�er - Enlightenment  
Name:		enlightenment
Version:	0.16.2
Release:	0.2
Copyright:	GPL
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy Okien
Source:		ftp://ftp.enlightenment.org/pub/enlightenment/enlightenment/%{name}-%{version}.tar.gz
Patch:		enlightenment-config-path.patch
URL:		http://www.enlightenment.org/
Requires:	glib >= 1.2.1
Requires:	gtk+ >= 1.2.1
BuildRoot:	/tmp/%{name}-%{version}-root

%define	_prefix	/usr/X11R6

%description
Enlightenment is a Windowmanager for X-Windows that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpot�niejszym i najpi�kniejszym window-menad�erem 
jaki kiedykolwiek zosta� stworzony dla Linuxa ;)

%prep
%setup -q
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
CFLAGS="-I/usr/include/freetype $RPM_OPT_FLAGS"; export CFLAGS
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

strip --strip-unneeded $RPM_BUILD_ROOT/usr/X11R6/bin/* || :

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
