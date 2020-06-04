%global commit0 6d42b88a75fc67376b9f39b98cd72c8933840d7e
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Summary:    the simplest + fastest video cutter & joiner
Name:       vidcutter
Version:    6.0.0.5
Release:    3%{?dist}
License:    GPLv3+
Source0:    https://github.com/ozmartian/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch:  x86_64
Group:      Applications/Multimedia
Url:        http://vidcutter.ozmartians.com
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc-c++
%if 0%{?fedora} >= 33
BuildRequires:  python3.9-devel
%else
BuildRequires:  python3-devel
%endif
BuildRequires: python3-setuptools
BuildRequires: mpv-libs-devel

Requires: python3-qt5 
Requires: mpv-libs
Requires: ffmpeg 
Requires: mediainfo
Requires: python3-pyopengl


%description
 The simplest & sexiest tool for cutting and joining your videos without the need for
 re-encoding or a diploma in multimedia. VidCutter focuses on getting the job done
 using tried and true tech in its arsenal via mpv and FFmpeg.

%prep
%autosetup -n %{name}-%{commit0} 

# Remove shebang from Python libraries
find -depth -type f -writable -name "*.py" -exec sed -iE '1s=^#! */usr/bin/\(python\|env python\)[23]\?=#!%{__python3}=' {} +

%build
%define debug_package %{nil}
python3 setup.py build

%install
python3 setup.py install --root %{buildroot}

%clean
rm -rf %{buildroot}

%files 

%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_docdir}/vidcutter/CHANGELOG
%{_docdir}/vidcutter/LICENSE
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-*-py*.egg-info
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/com.ozmartians.VidCutter.png
%{_datadir}/icons/hicolor/scalable/apps/com.ozmartians.VidCutter.svg
%{_datadir}/mime/packages/com.ozmartians.VidCutter.xml
%{_datadir}/metainfo/com.ozmartians.VidCutter.appdata.xml

%changelog

* Tue Jun 02 2020 David Va <davidva AT tuta DOT io> 6.0.0.5-3
- Rebuilt for python3.9

* Tue Jul 16 2019 David Va <davidva AT tuta DOT io> 6.0.0.5-2
- Updated to 6.0.0.5

* Thu Aug 02 2018 David Va <davidva AT tuta DOT io> 6.0.0-2
- Updated to current commit

* Fri Jul 13 2018 David Va <davidva AT tuta DOT io> 6.0.0-0.3
- Rebuilt for Python 3.7
- Updated to current commit

* Wed Jul 04 2018 David Va <davidva AT tuta DOT io> 6.0.0-0.2
- Updated to current commit

* Thu May 03 2018 David Vásquez <davidva AT tutanota DOT com> 6.0.0-0.1
- Updated to 6.0.0 RC1

* Mon Feb 05 2018 David Vásquez <davidva AT tutanota DOT com> 5.5.0-1
- Updated to 5.5.0

* Tue Dec 26 2017 David Vásquez <davidva AT tutanota DOT com> 5.0.5-2
- Reversing Python 3 OpenGL

* Sat Dec 02 2017 David Vásquez <davidva AT tutanota DOT com> 5.0.5-1
- Updated to 5.0.5

* Wed Nov 15 2017 David Vásquez <davidva AT tutanota DOT com> 5.0.0-1
- 5.0.0 release

* Sun Oct 29 2017 David Vásquez <davidva AT tutanota DOT com> 4.0.5-1
- 4.0.5 release

* Fri Aug 11 2017 Pete Alexandrou <pete AT ozmartians DOT com> 4.0.0-2
- Prevent debuginfo builds + specify x64 architecture specifically

* Thu Aug 03 2017 Pete Alexandrou <pete AT ozmartians DOT com> 4.0.0-1
- 4.0.0 release

* Mon May 29 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.5.0-1
- 3.5.0 release

* Fri May 12 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.2.0-1
- Latest release

* Thu Mar 23 2017 Pete Alexandrou <pete AT ozmartians DOT com> 3.0.1-1
- Latest version build w/ libmpv support

* Fri Jan 20 2017 David Vásquez <davidva AT tutanota DOT com> 2.2.5-1
- Initial build
