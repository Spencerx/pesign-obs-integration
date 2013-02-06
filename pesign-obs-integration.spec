#
# spec file for package pesign-obs-integration (Version 1.0)
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild
# needssslcertforbuild

Name:           pesign-obs-integration
Summary:        Macros and scripts to sign the kernel and bootloader
Version:        6.0
Release:        1
Requires:       openssl mozilla-nss-tools
%ifarch %ix86 x86_64 ia64
Requires:       pesign
%endif
BuildRequires:  openssl
License:        GPL v2 only
Group:          Development/Tools/Other
URL:            http://en.opensuse.org/openSUSE:UEFI_Image_File_Sign_Tools
Source2:        pesign-repackage.spec.in
Source3:        pesign-gen-repackage-spec
Source4:        brp-99-pesign
Source5:        COPYING
Source6:        README
Source7:        kernel-sign-file
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%description
This package provides scripts and rpm macros to automate signing of the
boot loader, kernel and kernel modules in the openSUSE Buildservice.

%prep
%setup -cT
cp %_sourcedir/{COPYING,README} .

%build

%install

mkdir -p %buildroot/usr/lib/rpm/brp-suse.d %buildroot/usr/lib/rpm/pesign
cd %_sourcedir
install  pesign-gen-repackage-spec kernel-sign-file %buildroot/usr/lib/rpm/pesign
install  brp-99-pesign %buildroot/usr/lib/rpm/brp-suse.d
install -m644 pesign-repackage.spec.in %buildroot/usr/lib/rpm/pesign
if test -e _projectcert.crt; then
	openssl x509 -inform PEM -in _projectcert.crt \
		-outform DER -out %buildroot/usr/lib/rpm/pesign/pesign-cert.x509
else
	echo "No buildservice project certificate available"
fi

%files
%defattr(-,root,root)
%doc COPYING README
/usr/lib/rpm/*

%changelog

