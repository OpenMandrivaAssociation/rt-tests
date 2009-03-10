%define name rt-tests
%define version 0.30
%define release %mkrel 1

Summary: Programs that test various rt-features
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group:   Development/Other
URL:     http://rt.wiki.kernel.org/index.php/Cyclictest
Source0: %{name}-%{version}.tar.gz
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
make DESTDIR=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog COPYING
%{_bindir}/classic_pi
%{_bindir}/cyclictest
%{_bindir}/pi_stress
%{_bindir}/signaltest
%{_mandir}/man8/cyclictest.8.lzma
%{_mandir}/man8/pi_stress.8.lzma
