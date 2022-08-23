#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pytest
Version  : 7.1.2
Release  : 180
URL      : https://files.pythonhosted.org/packages/4e/1f/34657c6ac56f3c58df650ba41f8ffb2620281ead8e11bcdc7db63cf72a78/pytest-7.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/1f/34657c6ac56f3c58df650ba41f8ffb2620281ead8e11bcdc7db63cf72a78/pytest-7.1.2.tar.gz
Summary  : pytest: simple powerful testing with Python
Group    : Development/Tools
License  : MIT
Requires: pypi-pytest-bin = %{version}-%{release}
Requires: pypi-pytest-license = %{version}-%{release}
Requires: pypi-pytest-python = %{version}-%{release}
Requires: pypi-pytest-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(atomicwrites)
BuildRequires : pypi(attrs)
BuildRequires : pypi(colorama)
BuildRequires : pypi(iniconfig)
BuildRequires : pypi(packaging)
BuildRequires : pypi(pluggy)
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_scm)
BuildRequires : pypi(tomli)
BuildRequires : pypi(wheel)
BuildRequires : pypi-hypothesis
BuildRequires : pypi-pytest
BuildRequires : pypi-xmlschema

%description
.. image:: https://github.com/pytest-dev/pytest/raw/main/doc/en/img/pytest_logo_curves.svg
:target: https://docs.pytest.org/en/stable/
:align: center
:height: 200
:alt: pytest

%package bin
Summary: bin components for the pypi-pytest package.
Group: Binaries
Requires: pypi-pytest-license = %{version}-%{release}

%description bin
bin components for the pypi-pytest package.


%package license
Summary: license components for the pypi-pytest package.
Group: Default

%description license
license components for the pypi-pytest package.


%package python
Summary: python components for the pypi-pytest package.
Group: Default
Requires: pypi-pytest-python3 = %{version}-%{release}

%description python
python components for the pypi-pytest package.


%package python3
Summary: python3 components for the pypi-pytest package.
Group: Default
Requires: python3-core
Provides: pypi(pytest)
Requires: pypi(atomicwrites)
Requires: pypi(attrs)
Requires: pypi(colorama)
Requires: pypi(iniconfig)
Requires: pypi(packaging)
Requires: pypi(pluggy)
Requires: pypi(py)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-pytest package.


%prep
%setup -q -n pytest-7.1.2
cd %{_builddir}/pytest-7.1.2
pushd ..
cp -a pytest-7.1.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656400718
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pytest || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pytest
cp %{_builddir}/pytest-7.1.2/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pytest/44c0d99d291b657acfcdcda79835e73e7758354c
cp %{_builddir}/pytest-7.1.2/doc/en/license.rst %{buildroot}/usr/share/package-licenses/pypi-pytest/7f8eb5b4026748f6a2abe43052835badaa5abeac
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/py.test
/usr/bin/pytest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pytest/44c0d99d291b657acfcdcda79835e73e7758354c
/usr/share/package-licenses/pypi-pytest/7f8eb5b4026748f6a2abe43052835badaa5abeac

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
