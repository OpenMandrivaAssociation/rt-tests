%define name rt-tests
%define version 0.72
%define release %mkrel 1

Summary: Programs that test various rt-features
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group:   Development/Other
URL:     http://rt.wiki.kernel.org/index.php/Cyclictest
Source0: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python

%description
A set of programs that test and measure various components of "realtime"
kernel behavior, such as timer latency, signal latency and the functioning
of priority-inheritance mutexes.

%prep
%setup -q -n %{name}

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man8
mkdir -p $RPM_BUILD_ROOT/%{python_sitelib}
make DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING
%{_bindir}/cyclictest
%{_bindir}/hackbench
%{_bindir}/pip_stress
%{_bindir}/pi_stress
%{_bindir}/pmqtest
%{_bindir}/ptsematest
%{_bindir}/rt-migrate-test
%{_bindir}/sendme
%{_bindir}/signaltest
%{_bindir}/hwlatdetect
%{_bindir}/sigwaittest
%{_bindir}/svsematest
%{_mandir}/man4/*.4.lzma
%{_mandir}/man8/*.8.lzma
%{python_sitelib}/hwlatdetect.py
%{_usrsrc}/backfire/backfire.c
