%define buildroot %{_topdir}/BUILDROOT/
%define release __RELEASE__

Name:       pingtest
Version:    1.%{release}
Release:    1%{?dist}
Summary:    multi-pinger
BuildRoot:  %{buildroot}

License:    GPLv2

Requires:   fping

%description
This package will ping multiple servers at once.

%prep
rm -rf %{buildroot} 
mkdir -p %{buildroot}/bin
cp %{_topdir}/SOURCES/pingtest %{buildroot}/bin/

%files
/bin/pingtest
