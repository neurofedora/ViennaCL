Name:          viennacl
Version:       1.7.1
Release:       1%{?dist}
Summary:       Linear algebra and solver library using CUDA, OpenCL, and OpenMP
License:       MIT
URL:           http://viennacl.sourceforge.net/
Source0:       http://sourceforge.net/projects/%{name}/files/1.7.x/ViennaCL-%{version}.tar.gz
BuildArch:     noarch

BuildRequires: gcc-c++ cmake
BuildRequires: opencl-headers ocl-icd-devel pocl
BuildRequires: boost-devel
BuildRequires: eigen3-devel


%description
ViennaCL provides high level C++ interfaces for linear algebra routines on CPUs
and GPUs using CUDA, OpenCL, and OpenMP. The focus is on generic implementations
of iterative solvers often used for large linear systems and simple integration
into existing projects.

%package devel
Summary:  Linear algebra and solver library using CUDA, OpenCL, and OpenMP

%description devel
ViennaCL provides high level C++ interfaces for linear algebra routines on CPUs
and GPUs using CUDA, OpenCL, and OpenMP. The focus is on generic implementations
of iterative solvers often used for large linear systems and simple integration
into existing projects.

%package doc
Summary: Documentation for %{name}

%description doc
ViennaCL provides high level C++ interfaces for linear algebra routines on CPUs
and GPUs using CUDA, OpenCL, and OpenMP. The focus is on generic implementations
of iterative solvers often used for large linear systems and simple integration
into existing projects.

%package example
Summary: Examples for %{name}

%description example
ViennaCL provides high level C++ interfaces for linear algebra routines on CPUs
and GPUs using CUDA, OpenCL, and OpenMP. The focus is on generic implementations
of iterative solvers often used for large linear systems and simple integration
into existing projects.


%prep
%autosetup -n ViennaCL-%{version}
rm -vrf CL

%build
pushd build
        %cmake .. \
        -DINSTALL_CMAKE_DIR:PATH=%{_datadir}/cmake \
        -DENABLE_ASAN=ON \
        -DVIENNACL_WITH_OPENCL=ON \
        -DBUILD_EXAMPLES=ON \
        -DENABLE_OPENCL=ON \
        -DENABLE_EIGEN=ON \
        -DEIGEN_INCLUDE_DIR:PATH=%{_includedir}/eigen3 \
        -DENABLE_UBLAS=ON \
        -DBUILD_TESTING=ON
        %make_build
popd


%install
pushd build
        %make_install
popd

%check
pushd build
        ctest -VV \
        -I 1,59,1,61,62,63,64,65,66,67,68,69,70,71,72,73 \
        -E  bisect-opencl  structured-matrices-opencl
popd


%files devel
%doc README
%license LICENSE
%{_includedir}/%{name}
%{_datadir}/cmake/*

%files doc
%doc doc/html

%files example
%doc examples


%changelog
* Thu Jan 21 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.1-1
- update to 1.7.1
 
* Sat Dec 19 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.0-2
- add devel, doc and example files
- trivial fixes in spec

* Sun Dec 06 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.0-1
- Initial package
