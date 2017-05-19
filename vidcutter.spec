Summary:    the simplest + fastest video cut & merge tool
Name:       vidcutter
Version:    3.2.0
Release:    2%{?dist}
License:    GPLv3+
Source0:    https://github.com/ozmartian/%{name}/archive/%{version}.tar.gz
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

%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py?.?.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.svg

%changelog
* Fri May 12 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.2.0-1
- Latest release

* Thu Mar 23 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.0.1-1
- Latest version build w/ libmpv support

* Fri Jan 20 2017 David Vásquez <davidva AT tutanota DOT com> 2.2.5-1
- Initial build
