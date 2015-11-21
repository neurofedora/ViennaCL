Name:          ViennaCL
Version:       1.7.0
Release:       1%{?dist}
Summary:       Linear algebra and solver library using CUDA, OpenCL, and OpenMP

License:       MIT
URL:           http://viennacl.sourceforge.net/
Source0:       http://sourceforge.net/projects/viennacl/files/1.7.x/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: gcc-c++ cmake
BuildRequires: opencl-headers ocl-icd-devel
BuildRequires: boost-devel
#BuildRequires: blas-devel
#BuildRequires: eigen3-devel eigen3-static
#BuildRequires: armadillo  armadillo-devel

%description
ViennaCL provides high level C++ interfaces for linear algebra routines on CPUs
and GPUs using CUDA, OpenCL, and OpenMP. The focus is on generic implementations
of iterative solvers often used for large linear systems and simple integration
into existing projects.

%prep
%autosetup

%build
pushd build
  %cmake .. \
  -DBUILD_TESTING=ON \
  -DBUILD_EXAMPLES=ON \
  -DVIENNACL_WITH_OPENMP=ON \
  -DVIENNACL_WITH_OPENCL=ON \
  -DENABLE_OPENCL=ON \
  -DENABLE_OPENMP=ON
  %make_build
popd

#-DENABLE_UBLAS=ON \
#-DBUILD_EXAMPLES=ON \
#-DVIENNACL_WITH_EIGEN=ON \
#-DENABLE_EIGEN=ON \
#-DEIGEN_INCLUDE_DIR:PATH=%{_includedir}/eigen3/ \
#-DENABLE_ARMADILLO=ON \
#-DCMAKE_INSTALL_LIBDIR=%{_libdir} \

%install
pushd build
  %make_install
popd

%check
pushd build
  ctest -V || :
popd

%files
%doc README
%license LICENSE
%{_includedir}/*
%exclude /usr/lib/cmake/*


%changelog
* Mon Nov 16 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.0-1
- Initial package											
