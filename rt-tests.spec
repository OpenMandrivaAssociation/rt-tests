%define name rt-tests
%define version 0.72
%define release %mkrel 2

Summary: Programs that test various rt-features
Name:    %{name}
Version: %{version}
Release: %{release}
License: GPLv2
Group:   Development/Other
URL:     http://rt.wiki.kernel.org/index.php/Cyclictest
Source0: %{name}-%{version}.tar.bz2
Patch0: rt-tests-0.72-fix-str-fmt.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: python

%description
A set of programs that test and measure various components of "realtime"
kernel behavior, such as timer latency, signal latency and the functioning
of priority-inheritance mutexes.

%prep
%setup -q -n %{name}
%patch0 -p0

%build
%make CC="gcc %{optflags} %{ldflags}"

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
%{_mandir}/man4/*.4.*
%{_mandir}/man8/*.8.*
%{python_sitelib}/hwlatdetect.py
%{_usrsrc}/backfire/backfire.c


%changelog
* Mon Nov 22 2010 Funda Wang <fwang@mandriva.org> 0.72-2mdv2011.0
+ Revision: 599640
- bump rel
- fix linking

* Sun Aug 01 2010 trem <trem@mandriva.org> 0.72-1mdv2011.0
+ Revision: 564845
- update to 0.72

* Mon Apr 12 2010 trem <trem@mandriva.org> 0.70-1mdv2010.1
+ Revision: 533736
- add python as buildrequires
- update to 0.70
- update to 0.67

* Tue Feb 23 2010 trem <trem@mandriva.org> 0.66-1mdv2010.1
+ Revision: 510460
- update to 0.66

* Wed Jan 27 2010 trem <trem@mandriva.org> 0.63-1mdv2010.1
+ Revision: 497452
- update to 0.63

* Sat Jan 23 2010 trem <trem@mandriva.org> 0.61-1mdv2010.1
+ Revision: 495209
- update to 0.61

* Tue Dec 29 2009 trem <trem@mandriva.org> 0.60-1mdv2010.1
+ Revision: 483356
- update to 0.60

* Tue Dec 15 2009 trem <trem@mandriva.org> 0.57-1mdv2010.1
+ Revision: 479104
- update to 0.57

* Mon Jul 20 2009 trem <trem@mandriva.org> 0.50-1mdv2010.0
+ Revision: 398221
- update to 0.50

* Sat Jul 04 2009 trem <trem@mandriva.org> 0.46-1mdv2010.0
+ Revision: 391957
- update to 0.46
- update to 0.40

* Tue May 12 2009 trem <trem@mandriva.org> 0.39-1mdv2010.0
+ Revision: 375055
- update to 0.39

* Mon Apr 20 2009 trem <trem@mandriva.org> 0.36-1mdv2009.1
+ Revision: 368467
- update to 0.36
- remove patch fix_C_argument.patch (added upsteam)

* Sun Apr 19 2009 trem <trem@mandriva.org> 0.35-1mdv2009.1
+ Revision: 368028
- update to 0.35
- add patch fix_C_argument.patch
- update to 0.34

* Tue Mar 10 2009 trem <trem@mandriva.org> 0.30-1mdv2009.1
+ Revision: 353512
- update to 0.30

* Wed Oct 22 2008 trem <trem@mandriva.org> 0.28-1mdv2009.1
+ Revision: 296593
- update to 0.28

* Thu Sep 11 2008 trem <trem@mandriva.org> 0.27-1mdv2009.0
+ Revision: 283909
- import rt-tests


