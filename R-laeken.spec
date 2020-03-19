#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-laeken
Version  : 0.5.1
Release  : 27
URL      : https://cran.r-project.org/src/contrib/laeken_0.5.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/laeken_0.5.1.tar.gz
Summary  : Estimation of Indicators on Social Exclusion and Poverty
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-sampling
BuildRequires : R-sampling
BuildRequires : buildreq-R

%description
as Pareto tail modeling for empirical income distributions.

%prep
%setup -q -c -n laeken

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1580952225

%install
export SOURCE_DATE_EPOCH=1580952225
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library laeken
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library laeken
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library laeken
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc laeken || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/laeken/CITATION
/usr/lib64/R/library/laeken/DESCRIPTION
/usr/lib64/R/library/laeken/INDEX
/usr/lib64/R/library/laeken/Meta/Rd.rds
/usr/lib64/R/library/laeken/Meta/data.rds
/usr/lib64/R/library/laeken/Meta/features.rds
/usr/lib64/R/library/laeken/Meta/hsearch.rds
/usr/lib64/R/library/laeken/Meta/links.rds
/usr/lib64/R/library/laeken/Meta/nsInfo.rds
/usr/lib64/R/library/laeken/Meta/package.rds
/usr/lib64/R/library/laeken/Meta/vignette.rds
/usr/lib64/R/library/laeken/NAMESPACE
/usr/lib64/R/library/laeken/NEWS
/usr/lib64/R/library/laeken/R/laeken
/usr/lib64/R/library/laeken/R/laeken.rdb
/usr/lib64/R/library/laeken/R/laeken.rdx
/usr/lib64/R/library/laeken/data/datalist
/usr/lib64/R/library/laeken/data/eusilc.RData
/usr/lib64/R/library/laeken/data/ses.RData
/usr/lib64/R/library/laeken/doc/index.html
/usr/lib64/R/library/laeken/doc/laeken-intro.R
/usr/lib64/R/library/laeken/doc/laeken-intro.Rnw
/usr/lib64/R/library/laeken/doc/laeken-intro.pdf
/usr/lib64/R/library/laeken/doc/laeken-pareto.R
/usr/lib64/R/library/laeken/doc/laeken-pareto.Rnw
/usr/lib64/R/library/laeken/doc/laeken-pareto.pdf
/usr/lib64/R/library/laeken/doc/laeken-standard.R
/usr/lib64/R/library/laeken/doc/laeken-standard.Rnw
/usr/lib64/R/library/laeken/doc/laeken-standard.pdf
/usr/lib64/R/library/laeken/doc/laeken-variance.R
/usr/lib64/R/library/laeken/doc/laeken-variance.Rnw
/usr/lib64/R/library/laeken/doc/laeken-variance.pdf
/usr/lib64/R/library/laeken/help/AnIndex
/usr/lib64/R/library/laeken/help/aliases.rds
/usr/lib64/R/library/laeken/help/laeken.rdb
/usr/lib64/R/library/laeken/help/laeken.rdx
/usr/lib64/R/library/laeken/help/paths.rds
/usr/lib64/R/library/laeken/html/00Index.html
/usr/lib64/R/library/laeken/html/R.css
