Summary:    FFmpeg based video cutter & joiner with a modern PyQt5 GUI
Name:       vidcutter
Version:    2.2.5
Release:    1%{?dist}
License:    GPLv3
Source0:    https://github.com/ozmartian/%{name}/archive/%{version}.tar.gz
Group:      Applications/Multimedia
BuildArch:  noarch
Url:        http://vidcutter.ozmartians.com/
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python3-devel 
BuildRequires: python3-setuptools 
Requires: ffmpeg 
Requires: python3-qt5 
Requires: qt5-qtmultimedia


%description
Cross-platform Qt5 based app for quick and easy video trimming/splitting 
and merging/joining for simple quick edits. FFmpeg drives the backend with 
a stylishly hand edited Qt5 UI. 



%prep
%setup -q 
sed -i "s/pypi/arch/" __init__.py

%build
python3 setup.py build

%install
python3 setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files 

%{_bindir}/vidcutter
%{python3_sitelib}/vidcutter-%{version}-py*.egg-info/
%{python3_sitelib}/vidcutter/
%{_datadir}/applications/vidcutter.desktop
%{_datadir}/pixmaps/vidcutter.png

%changelog

* Fri Jan 20 2017 David Vásquez <davidva AT tutanota DOT com> 2.2.5-1
- Initial build
