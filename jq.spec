Name:           jq
Version:        1.6
Release:        2
Summary:        A lightweight and flexible command-line JSON processor
License:        MIT and ASL 2.0 and CC-BY and GPLv3
URL:            http://stedolan.github.io/jq/
Source0:        https://github.com/stedolan/jq/releases/download/jq-%{version}/jq-%{version}.tar.gz
BuildRequires:  make flex bison valgrind gcc chrpath oniguruma-devel

Patch0001:      jv_string_implode-avoid-producing-unprintable-string-fromreserved-code-points.patch
Patch0002:      Binary-strings-preserve-UTF-8-and-UTF-16-errors.patch
Patch0003:      Update-base64-utf8bytelength-and-fromjson-to-handlebinary-strings.patch
Patch0004:      Correct-UTF-8-and-UTF-16-errors-during-concatenation.patch

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
%autosetup -n jq-%{version} -p1

%build
%configure
%make_build

%install
%make_install
%delete_la_and_a
chrpath -d %{buildroot}%{_bindir}/%{name}

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
* Mon Aug 30 2021 lingsheng <lingsheng@huawei.com> - 1.6-2
- Support binary strings preserve UTF-8 and UTF-16 errors

* Wed Aug 25 2021 wangyue <wangyue92@huawei.com> - 1.6-1
- Upgrade to 1.6

* Thu Jun 03 2021 wulei <wulei80@huawei.com> - 1.5-18
- fixes failed: no acceptable C compiler found in $PATH

* Sat Mar 21 2020 yanglijin <yanglijin@huawei.com> -1.5-17
- close check

* Tue Mar 17 2020 likexin <likexin4@huawei.com> -1.5-16
- fix up cve-2016-4074

* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.5-15
- Delete unndeeded build requires

* Tue Dec 31 2019 zhujunhao <zhujunhao5@huawei.com> - 1.5-14
- Package init
