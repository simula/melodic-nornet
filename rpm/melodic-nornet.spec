Name: melodic-nornet
Version: 1.1.7
Release: 1
Summary: MELODIC/NorNet Integration
Group: Applications/Internet
License: GPL-3+
URL: https://github.com/simula/melodic-nornet
Source: https://packages.nntb.no/software/%{name}/%{name}-%{version}.tar.xz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: dejavu-sans-fonts
BuildRequires: dejavu-sans-mono-fonts
BuildRequires: dejavu-serif-fonts
BuildRequires: gcc
BuildRequires: ghostscript
BuildRequires: gimp
BuildRequires: google-noto-cjk-fonts
BuildRequires: google-noto-sans-fonts
BuildRequires: google-noto-serif-fonts
BuildRequires: GraphicsMagick
BuildRequires: perl-Image-ExifTool
BuildRequires: urw-base35-fonts
BuildRoot: %{_tmppath}/%{name}-%{version}-build

BuildArch: noarch

# TEST ONLY:
%define _unpackaged_files_terminate_build 0


%description
This package contains software for MELODIC system management.
The software installed provides a common working environment.
See https://www.melodic.cloud for details on MELODIC!

%prep
%setup -q

%build
# NOTE: CMAKE_VERBOSE_MAKEFILE=OFF for reduced log output!
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DFLAT_DIRECTORY_STRUCTURE=0 -DCMAKE_VERBOSE_MAKEFILE=OFF .
%cmake_build

%install
%cmake_install
# ====== Relocate files =====================================================
mkdir -p %{buildroot}/boot/MELODIC
mv %{buildroot}/usr/share/melodic-desktop/Splash/Management1-*.jpeg  %{buildroot}/boot/MELODIC
mv %{buildroot}/usr/share/melodic-desktop/Splash/Development1-*.jpeg %{buildroot}/boot/MELODIC
mv %{buildroot}/usr/share/melodic-desktop/Splash/Desktop1-*.jpeg     %{buildroot}/boot/MELODIC
mkdir -p %{buildroot}/etc/melodic
mv %{buildroot}/usr/share/melodic-desktop/Splash/melodic-version %{buildroot}/etc/melodic
# ===========================================================================


%package management
Summary: Management tools for the MELODIC system environment
Group: Applications/Internet
Requires: bash-completion
Requires: bc
Requires: bridge-utils
Requires: btrfs-progs
Requires: bwm-ng
Requires: colordiff
Requires: cronie
Requires: ethtool
Requires: git
Requires: gpm
Requires: hping3
Requires: htop
Requires: joe
Requires: jq
Requires: libidn
Requires: lksctp-tools
Requires: mlocate
Requires: netperfmeter
Requires: net-snmp-utils
Requires: net-tools
Requires: nmap
Requires: (ntpsec or ntpdate)
Requires: pxz
Requires: reprepro
Requires: rsplib-docs
Requires: rsplib-services
Requires: rsplib-tools
Requires: smartmontools
Requires: subnetcalc
Requires: tcpdump
Requires: tftp
Requires: traceroute
Requires: tree
Requires: vconfig
Requires: virt-what
Requires: whois
Requires: wireshark-cli
Recommends: grub2-tools
Recommends: reiserfs-utils

%description management
This metapackage contains basic software for MELODIC system management.
The software installed provides a common working environment.
See https://www.melodic.cloud for details on MELODIC!

%files management
/boot/MELODIC/Management1-*.jpeg
%{_sysconfdir}//grub.d/??_melodic_management_theme
%{_sysconfdir}//melodic/melodic-version
%{_datadir}/melodic-nornet/grub-defaults
%{_sysconfdir}/system-info.d/15-melodic
%{_sysconfdir}/system-maintenance.d/15-melodic

%post management
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun management
rm -f /etc/grub.d/??_melodic_management_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package development
Summary: Development tools for the MELODIC system environment
Group: Applications/Internet
Requires: %{name}-management = %{version}-%{release}
Requires: autoconf
Requires: automake
Requires: banner
Requires: bison
Requires: bzip2-devel
Requires: clang
Requires: cmake
Requires: (createrepo_c or createrepo)
Requires: debhelper
Requires: dejavu-sans-fonts
Requires: dejavu-sans-mono-fonts
Requires: dejavu-serif-fonts
Requires: devscripts
Requires: flex
Requires: gcc
Requires: gcc-c++
Requires: gdb
Requires: ghostscript
Requires: gimp
Requires: glib2-devel
Requires: gnupg
Requires: gnuplot
Requires: google-noto-cjk-fonts
Requires: google-noto-sans-fonts
Requires: google-noto-serif-fonts
Requires: GraphicsMagick
Requires: libcurl-devel
Requires: libpcap-devel
Requires: libtool
Requires: lksctp-tools-devel
Requires: make
Requires: mock
Requires: openssl-devel
Requires: pbuilder
Requires: perl-Image-ExifTool
Requires: pkg-config
Requires: python3
Requires: qt5-qtbase-devel
Requires: quilt
Requires: R-base
Requires: rpm
Requires: texlive-epstopdf-bin
Requires: urw-base35-fonts
Requires: valgrind
Recommends: rsplib-devel


%description development
This metapackage contains basic software for MELODIC development.
The software installed provides a common working environment.
See https://www.melodic.cloud for details on MELODIC!

%files development
/boot/MELODIC/Development1-*.jpeg
%{_sysconfdir}//grub.d/??_melodic_development_theme

%post development
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun development
rm -f /etc/grub.d/??_melodic_development_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%package desktop
Summary: Desktop setup for the MELODIC system environment
Group: Applications/Internet
Requires: %{name}-management = %{version}-%{release}
Recommends: xorg-x11-drv-vmware

%description desktop
This metapackage contains the scripts to configure a MELODIC desktop.
See https://www.melodic.cloud for details on MELODIC!

%files desktop
/boot/MELODIC/Desktop1-*.jpeg
%{_sysconfdir}//grub.d/??_melodic_desktop_theme
%{_datadir}/melodic-desktop/MELODIC-A4.pdf
%{_datadir}/melodic-desktop/Desktop-with-Logo/*x*/*/*
%{_datadir}/melodic-desktop/Desktop-without-Logo/*x*/*/*
%ghost %{_datadir}/melodic-nornet/Splash

%post desktop
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi

%postun desktop
rm -f /etc/grub.d/??_melodic_desktop_theme
if [ -e /usr/sbin/grub2-mkconfig ] ; then /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg || true ; fi


%changelog
* Sun Sep 11 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.7
- New upstream release.
* Wed Feb 16 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.6
- New upstream release.
* Mon Feb 14 2022 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.5
- New upstream release.
* Mon Jun 14 2021 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.4
- New upstream release.
* Sun Nov 15 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.3
- New upstream release.
* Tue Oct 27 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.2
- New upstream release.
* Fri Oct 09 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.1
- New upstream release.
* Tue Oct 06 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.1.0
- New upstream release.
* Tue May 05 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.2
- New upstream release.
* Fri Apr 24 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.1
- New upstream release.
* Mon Jan 20 2020 Thomas Dreibholz <dreibh@iem.uni-due.de> - 1.0.0
- New upstream release.
* Thu Nov 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.8.4
- New upstream release.
* Wed Oct 23 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.8.3
- New upstream release.
* Fri Sep 20 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.8.2
- New upstream release.
* Fri Sep 20 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.8.1
- New upstream release.
* Thu Aug 22 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.8.0
- New upstream release.
* Wed Aug 07 2019 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.7.1
- New upstream release.
* Mon Aug 05 2019 Thomas Dreibholz <dreibh@simula.no> - 0.7.0
- New upstream release.
* Wed Jul 03 2019 Thomas Dreibholz <dreibh@simula.no> - 0.6.3
- New upstream release.
* Mon Jun 17 2019 Thomas Dreibholz <dreibh@simula.no> - 0.6.2
- New upstream release.
* Tue May 28 2019 Thomas Dreibholz <dreibh@simula.no> - 0.6.1
- New upstream release.
* Wed May 15 2019 Thomas Dreibholz <dreibh@simula.no> - 0.6.0
- New upstream release.
* Wed Mar 06 2019 Thomas Dreibholz <dreibh@simula.no> - 0.5.0
- New upstream release.
* Wed Nov 22 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
