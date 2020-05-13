#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gtable
Version  : 0.3.0
Release  : 74
URL      : https://cran.r-project.org/src/contrib/gtable_0.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gtable_0.3.0.tar.gz
Summary  : Arrange 'Grobs' in Tables
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
Tools to make it easier to work with "tables" of 'grobs'. The 'gtable' package
defines a 'gtable' grob class that specifies a grid along with a list of grobs
and their placement in the grid. Further the package makes it easy to
manipulate and combine 'gtable' objects so that complex compositions can be
build up sequentially.

%prep
%setup -q -c -n gtable
cd %{_builddir}/gtable

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589403431

%install
export SOURCE_DATE_EPOCH=1589403431
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gtable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gtable
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gtable
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gtable || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gtable/DESCRIPTION
/usr/lib64/R/library/gtable/INDEX
/usr/lib64/R/library/gtable/Meta/Rd.rds
/usr/lib64/R/library/gtable/Meta/features.rds
/usr/lib64/R/library/gtable/Meta/hsearch.rds
/usr/lib64/R/library/gtable/Meta/links.rds
/usr/lib64/R/library/gtable/Meta/nsInfo.rds
/usr/lib64/R/library/gtable/Meta/package.rds
/usr/lib64/R/library/gtable/Meta/vignette.rds
/usr/lib64/R/library/gtable/NAMESPACE
/usr/lib64/R/library/gtable/NEWS.md
/usr/lib64/R/library/gtable/R/gtable
/usr/lib64/R/library/gtable/R/gtable.rdb
/usr/lib64/R/library/gtable/R/gtable.rdx
/usr/lib64/R/library/gtable/doc/index.html
/usr/lib64/R/library/gtable/doc/profiling.R
/usr/lib64/R/library/gtable/doc/profiling.Rmd
/usr/lib64/R/library/gtable/doc/profiling.html
/usr/lib64/R/library/gtable/help/AnIndex
/usr/lib64/R/library/gtable/help/aliases.rds
/usr/lib64/R/library/gtable/help/figures/README-unnamed-chunk-2-1.png
/usr/lib64/R/library/gtable/help/figures/README-unnamed-chunk-3-1.png
/usr/lib64/R/library/gtable/help/figures/logo.png
/usr/lib64/R/library/gtable/help/gtable.rdb
/usr/lib64/R/library/gtable/help/gtable.rdx
/usr/lib64/R/library/gtable/help/paths.rds
/usr/lib64/R/library/gtable/html/00Index.html
/usr/lib64/R/library/gtable/html/R.css
/usr/lib64/R/library/gtable/tests/testthat.R
/usr/lib64/R/library/gtable/tests/testthat/Rplots.pdf
/usr/lib64/R/library/gtable/tests/testthat/helper-grobs.r
/usr/lib64/R/library/gtable/tests/testthat/helper-units.r
/usr/lib64/R/library/gtable/tests/testthat/test-bind.r
/usr/lib64/R/library/gtable/tests/testthat/test-filter.R
/usr/lib64/R/library/gtable/tests/testthat/test-layout.r
/usr/lib64/R/library/gtable/tests/testthat/test-new-data-frame.R
/usr/lib64/R/library/gtable/tests/testthat/test-subsetting.r
/usr/lib64/R/library/gtable/tests/testthat/test-trim.R
/usr/lib64/R/library/gtable/tests/testthat/test-z-order.r
