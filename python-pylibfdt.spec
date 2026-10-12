Name:		python-pylibfdt
Version:	1.7.2.post2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pylibfdt/pylibfdt-%{version}.tar.gz
Summary:	Python binding for libfdt
URL:		https://pypi.org/project/pylibfdt/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	pkgconfig(python3)
BuildRequires:	swig

%description
Python binding for libfdt

%prep
%autosetup -p1 -n pylibfdt-%{version}
# The sdist pins the PyPI swig wrapper. The system swig binary is used instead.
sed -i 's/,"swig==4\.4\.\*"//' pyproject.toml
# The SWIG interface still calls the Python 2 C API.
sed -i \
	-e 's/PyString_FromString/PyUnicode_FromString/g' \
	-e 's/PyInt_AsLong/PyLong_AsLong/g' \
	libfdt/libfdt.i

%build
# The sdist is not a git checkout, so setuptools_scm needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py_build

%install
%py_install

%files
%{py_platsitedir}/_libfdt.*
%{py_platsitedir}/libfdt.py
%{py_platsitedir}/pylibfdt*.*-info
%{python_sitearch}/__pycache__/libfdt.cpython-*.pyc
