Summary:	Voice over IP
Summary(pl):	G³os po IP
Name:		erikyyyphone
Version:	1.0.0
Release:	1
Group:		Applications/Communications
License:	GPL
Source0:	http://www.erikyyy.de/erikyyyphone/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
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

%build
aclocal
automake -a -c
CPPFLAGS="-I%{_includedir}/ncurses" ; export CPPFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

gzip -9nf AUTHORS README TODO

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
