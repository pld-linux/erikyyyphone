Summary:	Voice over IP
Summary(pl):	G³os po IP
Name:		erikyyyphone
Version:	1.0.1
Release:	1
Group:		Applications/Communications
License:	GPL
Source0:	http://www.erikyyy.de/erikyyyphone/%{name}-%{version}.tar.gz
# Source0-md5:	1d8b3327d158e81e28ebe89550c236fe
URL:		http://www.erikyyy.de/erikyyyphone/
Patch0:		%{name}-make.patch
Patch1:		%{name}-ac.patch
Patch2:		%{name}-c.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libgsm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voice over IP.

%description -l pl
G³os po IP.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"; export CPPFLAGS
%configure
%{__make} CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/*
