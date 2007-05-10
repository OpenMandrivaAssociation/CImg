%define fver 1-11

Summary:	Tools for advanced image processing
Name:		CImg
Version:	1.1.1
Release:	%mkrel 2
Source0:	http://download.sourceforge.net/libusb/%name-%fver.tar.bz2
License:	CeCiLL
Group:		Graphics
BuildRoot:	%_tmppath/%name-%version-root
URL:		http://cimg.sourceforge.net/
BuildRequires:	doxygen
BuildRequires:  X11-devel

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
%setup -q -n %name-%fver
chmod -R go+rX .

%build
cd examples
make "ARCHFLAGS=%{optflags}" all
cd ..
cd documentation
doxygen CImg.doxygen
cd ..

%install

install -d %{buildroot}%{_includedir}
cp CImg.h %{buildroot}%{_includedir}

cd examples
install -d %{buildroot}%{_bindir}
cp CImg_test \
     fade_images \
     greycstoration \
     hough_transform \
     image_registration \
     image2ascii \
     inrcast \
     mcf_levelsets \
     odykill \
     pslider \
     pde_heatflow2D \
     pde_TschumperleDeriche2D \
     render3d \
     tetris \
     tutorial \
     wavelet_atrous %{buildroot}%{_bindir}
cd ..

%clean
rm -rf %buildroot


%files
%defattr(-,root,root)
%_bindir/*
%doc README.txt LICENSE*.txt CHANGES.txt

%files devel
%defattr(-,root,root)
%_includedir/*
%doc documentation/*
