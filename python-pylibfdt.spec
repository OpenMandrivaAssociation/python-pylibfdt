Name:		python-pylibfdt
Version:	1.7.0.post2
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pylibfdt/pylibfdt-%{version}.tar.gz
Summary:	Python binding for libfdt
URL:		https://pypi.org/project/pylibfdt/
License:	GPL
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	pkgconfig(python3)
BuildRequires:	swig

%description
Python binding for libfdt

%prep
%autosetup -p1 -n pylibfdt-%{version}

%build
%py_build

%install
%py_install

%files
%{py_platsitedir}/_libfdt.*
%{py_platsitedir}/libfdt.py
%{py_platsitedir}/pylibfdt*.*-info
