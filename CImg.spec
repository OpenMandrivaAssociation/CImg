%define	name CImg
%define version 1.2.2.1
%define greycstoration_version 2.5.2
%define release %mkrel 2

Summary:	Tools for advanced image processing
Name:		%name
Version:	%version
Release:	%release
Source0:	http://downloads.sourceforge.net/cimg/%name-%version.tar.bz2
# (fc) 1.2.2.1-2mdv Update to greycstoration version 2.5.2
Patch0:		CImg-1.2.2.1-greycstoration-2.5.2.patch
License:	CeCiLL
Group:		Graphics
BuildRoot:	%_tmppath/%name-%version-root
URL:		http://cimg.sourceforge.net/
BuildRequires:	doxygen
BuildRequires:  X11-devel, png-devel, jpeg-devel, tiff-devel, freetype-devel, libjbig-devel, libMagick-devel
BuildRequires:  lcms-devel, jasper-devel, libdjvulibre-devel, libfontconfig-devel, libsm-devel, libice-devel
BuildRequires:  bzip2-devel, libxml2-devel, fftw3-devel, gimp-devel

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

%package -n greycstoration
Summary:	Tool for image noise removal using the GREYCstoration algorithm
Group:		Graphics
Version:	%greycstoration_version

%description -n greycstoration

GIMP plug-in to do noise removal with the help of the GREYCstoration
algorithm. More sophisticated than built-in methods of most image
manipulation software.

%prep
%setup -q
%patch0 -p1 -b .252
chmod -R go+rX .

%build
cd examples
# create optimized build with minimum dependencies
%make ARCHFLAGS="-Dcimg_display_type=0 %{optflags}" all
g++ -o greycstoration4gimp greycstoration4gimp.cpp `gimptool-2.0 --cflags --libs` -I.. -I ../plugins -lpthread %{optflags}

cd ..
cd documentation
doxygen CImg.doxygen
cd ..

%install

install -d %{buildroot}%{_includedir}
cp CImg.h %{buildroot}%{_includedir}

cd examples
install -d %{buildroot}%{_bindir}
cp CImg_demo \
     dtmri_view \
     edge_explorer\
     fade_images \
     greycstoration \
     greycstoration4integration\
     hough_transform \
     image2ascii \
     image_registration \
     image_surface \
     inrcast \
     mcf_levelsets \
     mcf_levelsets3D\
     nlmeans\
     odykill \
     pde_TschumperleDeriche2D \
     pde_heatflow2D \
     pslider \
     tetris \
     tutorial \
     wavelet_atrous %{buildroot}%{_bindir}

install -d %{buildroot}%_libdir/gimp/2.0/plug-ins/
cp  greycstoration4gimp %{buildroot}%_libdir/gimp/2.0/plug-ins/

cd ..

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%_bindir/* 
%exclude %{_bindir}/greycstoration*
%doc README.txt Licence*.txt CHANGES.txt

%files devel
%defattr(-,root,root)
%_includedir/*
%doc documentation/*

%files -n greycstoration
%defattr(-,root,root)
%_bindir/greycstoration*
%_libdir/gimp/2.0/plug-ins/*
