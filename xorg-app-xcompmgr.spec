Summary:	Example compositing manager for X servers supporting the Composite extension
Summary(pl.UTF-8):	Przykładowy zarządca składania dla serwerów X z rozszerzeniem Composite
Name:		xorg-app-xcompmgr
Version:	1.1.6
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xcompmgr-%{version}.tar.bz2
# Source0-md5:	d45afaf2a153e8a5dd93a92955060c9a
URL:		http://freedesktop.org/Software/xapps
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-util-util-macros >= 1.3
Obsoletes:	xcompmgr
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xcompmgr
%{_mandir}/man1/xcompmgr.1*
