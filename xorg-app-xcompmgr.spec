Summary:	Composite extension option manager
Summary(pl):	Zarz±dca opcji dla rozszerzenia composite
Name:		xcompmgr
Version:	1.1.1
Release:	1
Epoch:		1
License:	MIT
Group:		X11/Applications
Source0:	http://freedesktop.org/~xapps/release/%{name}-%{version}.tar.bz2
# Source0-md5:	5c7b7e1c0360fec4b185cf575cf3fa0a
URL:		http://www.freedesktop.org/Software/xapps
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
%setup -q

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
