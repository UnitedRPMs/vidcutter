Summary:    the simple & fast video cutter & joiner with the help of mpv + FFmpeg
Name:       vidcutter
Version:    3.0.1
Release:    1%{?dist}
License:    GPLv3+
Source0:    https://github.com/ozmartian/%{pkg_name}/archive/%{version}.tar.gz
Group:      Applications/Multimedia
BuildArch:  noarch
Url:        http://vidcutter.ozmartians.com
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python3-devel 
BuildRequires: python3-setuptools 
Requires: python3-qt5 
Requires: mpv-libs
Requires: ffmpeg 
Requires: mediainfo


%description
 The simplest & sexiest tool for cutting and joining your videos without the need for
 re-encoding or a diploma in multimedia. VidCutter focuses on getting the job done
 using tried and true tech in its arsenal via mpv and FFmpeg.

%prep
%setup -q 
sed -i "s/pypi/rpm/" vidcutter/__init__.py

%build
python3 setup.py build

%install
python3 setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files 

%license vidcutter/LICENSE.html LICENSE
%doc README.md
%{_bindir}/vidcutter
%{python3_sitelib}/%{pkg_name}
%{python3_sitelib}/%{pkg_name}-%{version}-py?.?.egg-info
%{_datadir}/applications/vidcutter.desktop
%{_datadir}/pixmaps/vidcutter.svg


%changelog

* Thu Mar 23 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.0.1-1
- Latest version build w/ libmpv support
* Fri Jan 20 2017 David Vásquez <davidva AT tutanota DOT com> 2.2.5-1
- Initial build
