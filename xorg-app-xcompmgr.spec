Summary:	Composite extension option manager
Summary(pl):	Mened¿er opcji dla rozszrzenia composite
Name:		xcompmgr
Version:	040915
Release:	1
License:	GPL
Group:		X11
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	640b34cfefa8e655743083c3e51c6887
URL:		http://freedesktop.org/cgi-bin/viewcvs.cgi/xapps/xcompmgr/
BuildRequires:	X11-devel >= 1:6.8.0
BuildRequires:	pkgconfig
Requires:	X11-libs >= 1:6.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		%{_usr}/X11R6

%description
Composite extension option manager.

%description -l pl
Mened¿er opcji dla rozszrzenia composite.

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
install -d $RPM_BUILD_ROOT%{_bindir}

%{makeinstall}

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*.1*
