Summary:	Example compositing manager for X servers supporting the Composite extension
Summary(pl.UTF-8):	Przykładowy zarządca składania dla serwerów X z rozszerzeniem Composite
Name:		xorg-app-xcompmgr
Version:	1.1.9
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xcompmgr-%{version}.tar.xz
# Source0-md5:	4917d73c84180925ef2a2765a2a06e4e
URL:		https://freedesktop.org/wiki/Software/xapps/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Obsoletes:	xcompmgr < 1:1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xcompmgr is a sample compositing manager for X servers supporting the
XFIXES, DAMAGE, RENDER, and COMPOSITE extensions.  It enables basic
eye-candy effects.

%description -l pl.UTF-8
xcompmgr to przykładowy zarządca składania dla serwerów X
obsługujących rozszerzenia XFIXES, DAMAGE, RENDER i Composite. Włącza
podstawowe miłe dla oka efekty.

Zarządca opcji dla rozszerzenia composite.

%prep
%setup -q -n xcompmgr-%{version}

%build
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

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xcompmgr
%{_mandir}/man1/xcompmgr.1*
