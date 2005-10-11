Summary:	Enlightenment Window Manager
Summary(pl):	Zarz±dca okien X - Enlightenment
Name:		enlightenment
Version:	0.16.999.018
Release:	1
License:	BSD
Group:		X11/Window Managers
Source0:	http://enlightenment.freedesktop.org/files/%{name}-%{version}.tar.gz
# Source0-md5:	2544e352df4eef6a6271aac0269f07ba
Source1:        %{name}-xsession.desktop
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	edje-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
Obsoletes:	enlightenmentDR17
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
Requires:	%{name} = %{version}-%{release}
Requires:	edje-devel

%description devel
Development headers for Enlightenment.

%description -l pl devel
Pliki nag³ówkowe dla Enlightenmenta.

%prep
%setup -q

%build
echo 'AC_DEFUN([AC_C___ATTRIBUTE__],
 [
  AC_MSG_CHECKING(for __attribute__)
  AC_CACHE_VAL(ac_cv___attribute__, [
  AC_TRY_COMPILE([#include <stdlib.h>],
  [int func(int x); int foo(int x __attribute__ ((unused))) { exit(1); }],
  ac_cv___attribute__=yes, ac_cv___attribute__=no)])
  if test "$ac_cv___attribute__" = "yes"; then
    AC_DEFINE(HAVE___ATTRIBUTE__, 1, [Define to 1 if compiler has __attribute__])
  fi
  AC_MSG_RESULT($ac_cv___attribute__)])' > acinclude.m4

%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop

cd $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts
VERA=$(ls Vera*.ttf)
for FONT in $VERA; do
	rm -f $FONT
	ln -s %{_fontsdir}/TTF/$FONT .
done
cd -

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING* README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libe.so.*.*.*
%{_libdir}/enlightenment
%{_datadir}/%{name}
%{_datadir}/xsessions/%{name}.desktop

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libe.so
%{_libdir}/libe.la
%dir %{_includedir}/enlightenment
%{_includedir}/enlightenment/*.h
%{_includedir}/E_Lib.h

%if 0
%files static
%defattr(644,root,root,755)
%{_libdir}/libe.a
%endif
