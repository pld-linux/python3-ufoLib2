#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	UFO font library
Summary(pl.UTF-8):	Biblioteka do fontów UFO
Name:		python3-ufoLib2
Version:	0.12.1
Release:	5
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ufoLib2/
Source0:	https://files.pythonhosted.org/packages/source/u/ufoLib2/ufoLib2-%{version}.tar.gz
# Source0-md5:	897c563e60a09639aa0a2fdfa79d9dab
URL:		https://pypi.org/project/ufoLib2/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:42
# 45
BuildRequires:	python3-setuptools_scm
# >= 6.2
%if %{with tests}
BuildRequires:	python3-attrs >= 20.1.0
# fonttools[ufo]
BuildRequires:	python3-fonttools >= 4.0.0
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-pytest
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-typing_extensions
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ufoLib2 is a UFO font library.

%description -l pl.UTF-8
ufoLib2 to biblioteka do fontów UFO.

%prep
%setup -q -n ufoLib2-%{version}

# setuptools stub for PLD macros
cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/ufoLib2
%{py3_sitescriptdir}/ufoLib2-%{version}-py*.egg-info
