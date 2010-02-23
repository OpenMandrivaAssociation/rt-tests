%define name rt-tests
%define version 0.66
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
%{_bindir}/pi_stress
%{_bindir}/signaltest
%{_bindir}/hwlatdetect
%{_bindir}/ptsematest
%{_bindir}/rt-migrate-test
%{_bindir}/sendme
%{_bindir}/sigwaittest
%{_bindir}/svsematest
%{_bindir}/pip
%{_mandir}/man4/*.4.lzma
%{_mandir}/man8/*.8.lzma
%{python_sitelib}/hwlatdetect.py
