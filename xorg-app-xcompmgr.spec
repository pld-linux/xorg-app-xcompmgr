Summary:	Composite extension option manager
Summary(pl):	Zarz±dca opcji dla rozszerzenia composite
Name:		xcompmgr
Version:	040915
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	640b34cfefa8e655743083c3e51c6887
URL:		http://freedesktop.org/cgi-bin/viewcvs.cgi/xapps/xcompmgr/
BuildRequires:	X11-devel >= 1:6.8.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	X11-libs >= 1:6.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		%{_usr}/X11R6
%define		_mandir		%{_prefix}/man

%description
Composite extension option manager.

%description -l pl
Zarz±dca opcji dla rozszerzenia composite.

%prep
%setup -q -n %{name}

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
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
