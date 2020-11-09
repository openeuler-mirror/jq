Name:           jq
Version:        1.5
Release:        18
Summary:        A lightweight and flexible command-line JSON processor
License:        MIT and ASL 2.0 and CC-BY and GPLv3
URL:            http://stedolan.github.io/jq/
Source0:        https://github.com/stedolan/jq/releases/download/jq-%{version}/jq-%{version}.tar.gz
Patch0:         CVE-2015-8863.patch
Patch1:         CVE-2016-4074.patch
BuildRequires:  make flex bison valgrind
Requires:       %{name}-help = %{version}-%{release}

%description
jq is a lightweight and flexible command-line JSON processor.
you can use it to slice and filter and map and transform structured data.
It is written in portable C, and it has zero runtime dependencies.
it can mangle the data format that you have into the one that you want.

%package        devel
Summary:        Development files for jq
Requires:       jq = %{version}-%{release}

%description devel
Development files for jq.

%package        help
Summary:        Documentation for jq package
BuildArch:      noarch

%description    help
Documentation for jq package.

%prep
%autosetup -n jq-%{version}

%build
%configure --disable-static
%make_build

%install
%make_install
%delete_la

%check
%if %{?_with_check:1}%{!?_with_check:0}
%ifarch x86_64
make check
%endif
%endif

%post
/sbin/ldconfig

%postun
/sbin/ldconfig


%files
%{_bindir}/jq
%{_libdir}/libjq.so.*
%{_datadir}/doc/jq/COPYING
%{_datadir}/doc/jq/AUTHORS

%files devel
%{_includedir}/*.h
%{_libdir}/libjq.so

%files help
%{_datadir}/man/man1/jq.1.gz
%{_datadir}/doc/jq/README
%{_datadir}/doc/jq/README.md


%changelog
* Fri Nov 06 2020 leiju <leiju4@huawei.com> -1.5-18
- Add Requires jq-help into jq

* Sat Mar 21 2020 yanglijin <yanglijin@huawei.com> -1.5-17
- close check

* Tue Mar 17 2020 likexin <likexin4@huawei.com> -1.5-16
- fix up cve-2016-4074

* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.5-15
- Delete unndeeded build requires

* Tue Dec 31 2019 zhujunhao <zhujunhao5@huawei.com> - 1.5-14
- Package init
