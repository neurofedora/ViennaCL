%ifnarch %{ix86} x86_64 %{arm}
%bcond_with tests
%else
%bcond_without tests
%endif

Name:          viennacl
Version:       1.7.1
Release:       3%{?dist}
Summary:       Linear algebra and solver library using CUDA, OpenCL, and OpenMP
License:       MIT and ISC
URL:           http://viennacl.sourceforge.net/
Source0:       http://sourceforge.net/projects/%{name}/files/1.7.x/ViennaCL-%{version}.tar.gz
BuildArch:     noarch

BuildRequires: gcc-c++ cmake
BuildRequires: opencl-headers ocl-icd-devel
Buildrequires: boost-devel
%if %{with tests}
BuildRequires: pocl
BuildRequires: clang
%endif


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


%prep
%autosetup -n ViennaCL-%{version}
rm -vrf CL

%build
pushd build
        %cmake .. \
        -DINSTALL_CMAKE_DIR:PATH=%{_datadir}/cmake/Modules \
        -DVIENNACL_WITH_OPENCL=ON \
        -DVIENNACL_WITH_OPENMP=ON \
        -DBUILD_TESTING=%{?with_tests:ON}%{!?with_tests:OFF}
        %make_build
popd


%install
%make_install -C build

%if %{with tests}
%check
pushd build
	# https://sourceforge.net/p/viennacl/mailman/message/35517365/
        ctest -VV --output-on-failure -E "(bisect-opencl|sparse_prod-opencl)"
popd
%endif

%files devel
%doc README
%license LICENSE
%{_includedir}/%{name}/
%dir %{_datadir}/cmake
%dir %{_datadir}/cmake/Modules
%{_datadir}/cmake/Modules/FindOpenCL.cmake
%{_datadir}/cmake/Modules/ViennaCLConfig.cmake
%{_datadir}/cmake/Modules/ViennaCLConfigVersion.cmake

%files doc
%doc doc/html


%changelog
* Thu Dec 01 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.1-3
- trivial changes in spec file 

* Wed Nov 30 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.1-2
- skipped two tests, status tests: https://sourceforge.net/p/viennacl/mailman/message/35517365/ 

* Thu Jan 21 2016 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.1-1
- update to 1.7.1
- deleted example files
 
* Sat Dec 19 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.0-2
- add devel, doc and example files
- trivial fixes in spec

* Sun Dec 06 2015 Ilya Gradina <ilya.gradina@gmail.com> - 1.7.0-1
- Initial package
