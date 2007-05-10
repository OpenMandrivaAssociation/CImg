%define	name CImg
%define version 1.2.0.3
%define release %mkrel 1

Summary:	Tools for advanced image processing
Name:		%name
Version:	%version
Release:	%release
Source0:	http://download.sourceforge.net/libusb/%name-%version.tar.bz2
License:	CeCiLL
Group:		Graphics
BuildRoot:	%_tmppath/%name-%version-root
URL:		http://cimg.sourceforge.net/
BuildRequires:	doxygen
BuildRequires:  X11-devel, png-devel, jpeg-devel, tiff-devel, freetype-devel, libjbig-devel, libMagick-devel
BuildRequires:  lcms-devel, jasper-devel, libdjvulibre-devel, libfontconfig-devel, libsm6-devel, libice-devel
BuildRequires:  bzip2-devel, libxml2-devel, fftw3-devel 

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
%setup -q
chmod -R go+rX .

%build
cd examples
make "ARCHFLAGS=%{optflags}" Mlinux
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
cd ..

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%_bindir/*
%doc README.txt Licence*.txt CHANGES.txt

%files devel
%defattr(-,root,root)
%_includedir/*
%doc documentation/*
