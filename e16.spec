Summary:	Enlightenment Window Manager
Summary(pl):	Zarz±dca okien X - Enlightenment
Name:		enlightenment
Version:	0.17.0
%define _snap	20050106
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/e-%{version}_pre10-%{_snap}.tar.gz
# Source0-md5:	bd9a373605308955931f9102c7ebc29d
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment is a Windowmanager for X Window that is designed to be
powerful, extensible, configurable and able to be really good looking.

%description -l pl
Enlightenment jest najpotê¿niejszym i najpiêkniejszym zarz±dc± okien
jaki kiedykolwiek zosta³ stworzony dla Linuksa ;)

%package devel
Summary:	Development headers for Enlightenment
Summary:	Pliki nag³ówkowe dla Enlightenmenta
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	edje-devel

%description devel
Development headers for Enlightenment.

%description -l pl devel
Pliki nag³ówkowe dla Enlightenmenta.

%prep
%setup -q -n e

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}/*.h
