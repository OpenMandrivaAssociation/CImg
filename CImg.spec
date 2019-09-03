%define	oname CImg

Summary:	Tools for advanced image processing
Name:	cimg
Version:	2.7.1
Release:	1
Source0:	http://cimg.eu/files/CImg_%{version}.zip
Patch0:		cimg-2.4.2-arm.patch
URL:		http://cimg.eu/
License:	CeCiLLv2
Group:		Graphics/Utilities

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libjpeg)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	doxygen
BuildRequires:  gomp-devel

%description
Advanced image manipulation algorithms, including the GREYCSTORATION
image regularization algorithm which is mainly used for removing image
noise.

This package contains tools based on the CImg library.

%package   devel
Summary:   Library for advanced image processing (development files)
Group:     Development/C
Provides:  cimg-devel = %version-%release

%description devel
This package contains the development files for the CImg library. It is
needed to compile programes which use functions of the CImg library.

Note that this library is not a dynamic library. The whole library
code is in the CImg.h file which is in this package. The main package
is not needed to compile software using this library.

%prep
%setup -q -n %{oname}-%{version}
%ifarch %{arm}
%patch0 -p1
%endif

%build
pushd examples
%make_build olinux
popd

%install
mkdir -p %{buildroot}%{_bindir}
pushd examples
mv captcha %{buildroot}%{_bindir}
mv CImg_demo %{buildroot}%{_bindir}
mv curve_editor2d %{buildroot}%{_bindir}
mv dtmri_view3d %{buildroot}%{_bindir}
mv edge_explorer2d %{buildroot}%{_bindir}
mv fade_images %{buildroot}%{_bindir}
mv gaussian_fit1d %{buildroot}%{_bindir}
mv generate_loop_macros %{buildroot}%{_bindir}
mv hough_transform2d %{buildroot}%{_bindir}
mv image2ascii %{buildroot}%{_bindir}
mv image_registration2d %{buildroot}%{_bindir}
mv image_surface3d %{buildroot}%{_bindir}
mv jawbreaker %{buildroot}%{_bindir}
mv mcf_levelsets2d %{buildroot}%{_bindir}
mv mcf_levelsets3d %{buildroot}%{_bindir}
mv odykill %{buildroot}%{_bindir}
mv pde_heatflow2d %{buildroot}%{_bindir}
mv pde_TschumperleDeriche2d %{buildroot}%{_bindir}
mv plotter1d %{buildroot}%{_bindir}
mv radon_transform2d %{buildroot}%{_bindir}
mv scene3d %{buildroot}%{_bindir}
mv spherical_function3d %{buildroot}%{_bindir}
mv tetris %{buildroot}%{_bindir}
mv tron %{buildroot}%{_bindir}
mv tutorial %{buildroot}%{_bindir}
mv use_chlpca %{buildroot}%{_bindir}
mv use_draw_gradient %{buildroot}%{_bindir}
mv use_nlmeans %{buildroot}%{_bindir}
mv use_RGBclass %{buildroot}%{_bindir}
mv use_skeleton %{buildroot}%{_bindir}
mv wavelet_atrous %{buildroot}%{_bindir}
popd

mkdir -p %{buildroot}%{_includedir}/%{oname}
mv plugins %{buildroot}%{_includedir}/%{oname}
mv %{oname}.h %{buildroot}%{_includedir}/%{oname}
ln -s %{oname}/%{oname}.h %{oname}.h
mv %{oname}.h %{buildroot}%{_includedir}

%files
%{_bindir}/*

%files devel
%{_includedir}/%{oname}*
%doc README.txt Licence_CeCILL* examples resources/CImg_reference.pdf


%changelog
* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 1.2.7-4mdv2011.0
+ Revision: 627690
- tighten BR

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - fix spacing at top of description
    - kill re-definition of %%buildroot on Pixel's request

  + Tiago Salem <salem@mandriva.com.br>
    - Upgrade to 1.2.7 version
    - drop greycstoration patch. It is no longer required.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Frederic Crozat <fcrozat@mandriva.com> 1.2.2.1-2mdv2008.0
+ Revision: 55537
-Release 1.2.2.1
-Patch0 : update greycstoration to 2.5.2.1
-split greycstoration in a subpackage, including gimp plugin

* Thu May 10 2007 Erwan Velu <erwan@mandriva.org> 1.2.0.3-1mdv2008.0
+ Revision: 26096
- Fixing buildrequires
- 1.2.0.3
- 1.2.0.3
- Import CImg



* Wed Mar 08 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.1.1-2mdk
- Add BuildRequires

* Mon Feb  6 2006 Till Kamppeter <till@mandriva.com> 1.1.1-1mdk
- Initial Mandriva release.
