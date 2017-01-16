#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gtable
Version  : 0.2.0
Release  : 30
URL      : https://cran.r-project.org/src/contrib/gtable_0.2.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gtable_0.2.0.tar.gz
Summary  : Arrange 'Grobs' in Tables
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
# gtable
[![Travis-CI Build Status](https://travis-ci.org/hadley/gtable.svg?branch=master)](https://travis-ci.org/hadley/gtable)
[![CRAN_Status_Badge](http://www.r-pkg.org/badges/version/gtable)](http://cran.r-project.org/package=gtable)
[![Coverage Status](https://img.shields.io/codecov/c/github/hadley/gtable/master.svg)](https://codecov.io/github/hadley/gtable?branch=master)

%prep
%setup -q -c -n gtable

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484539131

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1484539131
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gtable
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library gtable || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gtable/DESCRIPTION
/usr/lib64/R/library/gtable/INDEX
/usr/lib64/R/library/gtable/Meta/Rd.rds
/usr/lib64/R/library/gtable/Meta/hsearch.rds
/usr/lib64/R/library/gtable/Meta/links.rds
/usr/lib64/R/library/gtable/Meta/nsInfo.rds
/usr/lib64/R/library/gtable/Meta/package.rds
/usr/lib64/R/library/gtable/NAMESPACE
/usr/lib64/R/library/gtable/NEWS.md
/usr/lib64/R/library/gtable/R/gtable
/usr/lib64/R/library/gtable/R/gtable.rdb
/usr/lib64/R/library/gtable/R/gtable.rdx
/usr/lib64/R/library/gtable/help/AnIndex
/usr/lib64/R/library/gtable/help/aliases.rds
/usr/lib64/R/library/gtable/help/gtable.rdb
/usr/lib64/R/library/gtable/help/gtable.rdx
/usr/lib64/R/library/gtable/help/paths.rds
/usr/lib64/R/library/gtable/html/00Index.html
/usr/lib64/R/library/gtable/html/R.css
