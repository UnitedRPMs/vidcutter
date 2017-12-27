%global commit0 18c04afe1ddeec38982e24a50a14482834019db0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Summary:    the simplest + fastest video cutter & joiner
Name:       vidcutter
Version:    5.0.5
Release:    2%{?dist}
License:    GPLv3+
Source0:    https://github.com/ozmartian/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Patch:      OpenGL_fix.patch
BuildArch:  x86_64
Group:      Applications/Multimedia
Url:        http://vidcutter.ozmartians.com
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: python3-devel 
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
%autosetup -n %{name}-%{commit0} -p1

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
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-*-py*.egg-info
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/16x16/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/22x22/apps/%{name}.png
%{_datadir}/icons/hicolor/24x24/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/x-%{name}.xml
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/appdata/*.appdata.xml

%changelog

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
