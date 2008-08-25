Summary:	Composite extension option manager
Summary(pl.UTF-8):	Zarządca opcji dla rozszerzenia composite
Name:		xorg-app-xcompmgr
Version:	1.1.4
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/app/xcompmgr-%{version}.tar.bz2
# Source0-md5:	3eb1c2b7a6ceaec4ee872cb06d202d91
URL:		http://freedesktop.org/Software/xapps
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXrender-devel
Obsoletes:	xcompmgr
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Composite extension option manager.

%description -l pl.UTF-8
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
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
