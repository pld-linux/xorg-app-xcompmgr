
%define		_pkgname	xcompmgr
%define		_snap		040304

Summary:	X Composite extension manager
Name:		xcompmgr
Version:	%{_snap}
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://ep09.pld-linux.org/~adgor/pld/%{_pkgname}-%{_snap}.tar.bz2
# Source0-md5:	50bfc5758314eb7aea1728d3da2b5d8f
URL:		http://www.freedesktop.org/Software/xserver
BuildRequires:	libXcomposite-devel
BuildRequires:	libXdamage-devel
BuildRequires:	libXfixes-devel
BuildRequires:	libXrender-devel
BuildRequires:	pkgconfig
Requires:	libXcomposite
Requires:	libXdamage
Requires:	libXfixes
Requires:	libXrender
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%define		_noautoreqdep	libX11.so.6 libXrender.so.1

%description
X Composite extension manager.

%prep
%setup -q -n %{_pkgname}-%{_snap}

%build

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}
install xcompmgr $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/xcompmgr
