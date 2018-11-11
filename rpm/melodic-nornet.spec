Name: melodic-nornet
Version: 0.0.0
Release: 1
Summary: MELODIC/NorNet Integration
Group: Applications/Internet
License: GPLv3
URL: https://github.com/simula/melodic-nornet
Source: https://packages.melodic-nornet.example/sources/%{name}-%{version}.tar.gz

AutoReqProv: on
BuildRequires: cmake
BuildRequires: perl-Image-ExifTool
BuildRequires: gimp
BuildRequires: ImageMagick
BuildRoot: %{_tmppath}/%{name}-%{version}-build


# This package does not generate debug information (no executables):
%global debug_package %{nil}

# TEST ONLY:
# %define _unpackaged_files_terminate_build 0


%description
 This package contains the scripts to configure a SuNILab desktop.
 See https://github.com/simula/melodic-nornet for details on SuNILab!

%prep
%setup -q

%build
%cmake -DCMAKE_INSTALL_PREFIX=/usr -DFLAT_DIRECTORY_STRUCTURE=0 -DPRINT_A4=1 -DINSTALL_ORIGINALS=0 .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
/usr/share/melodic-nornet/*.pdf
/usr/share/melodic-nornet/Desktop-with-Logo/*x*/*/*
/usr/share/melodic-nornet/Desktop-without-Logo/*x*/*/*
/usr/share/melodic-nornet/Splash/*

%doc

%changelog
* Wed Nov 22 2017 Thomas Dreibholz <dreibh@iem.uni-due.de> - 0.0.0
- Created RPM package.
