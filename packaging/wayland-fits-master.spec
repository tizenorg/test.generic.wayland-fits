#
# spec file for package
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           wayland-fits-master
Version:	0.2.2
Release:	0
License:	GPL-2.0+
Summary:        Wayland Test Suite
Url:		https://github.com/01org/wayland-fits
Group:		Applications/Core Applications
Source0:	https://github.com/01org/wayland-fits/archive/master.zip
Source101:      ADN_animation.gif
Source1001:     bridge_of_the_gods.png
BuildRequires:  boost-devel
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(weston)
BuildRequires:  pkgconfig(elementary)
BuildRequires:  pkgconfig(ecore-wayland)
BuildRequires:  pkgconfig(evas)
BuildRequires:  pkgconfig(evas-wayland-shm)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  unzip
BuildRequires:  pkgconfig(evas-wayland-egl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Graphical Test Suite for wayland

%prep
%setup -q

%build
export CXXFLAGS="-DMEDIA_PATH='\"%{_datadir}/media\"'"
./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p -m 755 %{buildroot}%{_datadir}/media
install -m 755 %{SOURCE101} %{buildroot}%{_datadir}/media
install -m 755 %{SOURCE1001} %{buildroot}%{_datadir}/media

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%_bindir/wfits
%_libdir/weston/weston-wfits.so
%_datadir/media/*
%doc README
%license COPYING
