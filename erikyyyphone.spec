Summary:	Voice over IP
Name:		erikyyyphone
Version:	1.0.0
Release:	1
Group:		Applications/Sound	
Group(pl):	Aplikacje/D¼wiêk
License:	GPL
Source0:	http://www.erikyyy.de/erikyyyphone/%{name}-%{version}.tar.gz
Patch0:		%{name}-make.patch
BuildPrereq:	libgsm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Voice over IP

%prep
%setup  -q
%patch0 -p1

%build
automake
CPPFLAGS="-I/usr/include/ncurses" ; export CPPFLAGS
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
