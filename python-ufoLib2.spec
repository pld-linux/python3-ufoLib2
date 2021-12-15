#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (built from python3-ufoLib2.spec)

Summary:	UFO font library
Summary(pl.UTF-8):	Biblioteka do fontów UFO
Name:		python-ufoLib2
# keep 0.3.x here for python2 support
Version:	0.3.2.post2
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/ufoLib2/
Source0:	https://files.pythonhosted.org/packages/source/u/ufoLib2/ufoLib2-%{version}.zip
# Source0-md5:	87547f47e17284bca0823b5a63f81790
URL:		https://pypi.org/project/ufoLib2/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_scm
%if %{with tests}
BuildRequires:	python-attrs >= 18.2.0
BuildRequires:	python-enum34
# fonttools[ufo,lxml]
BuildRequires:	python-fonttools >= 3.34.0
BuildRequires:	python-fs >= 2.2.0
BuildRequires:	python-lxml >= 4.0
BuildRequires:	python-py
BuildRequires:	python-pytest
BuildRequires:	python-typing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%if %{with tests}
BuildRequires:	python3-attrs >= 18.2.0
BuildRequires:	python3-fonttools >= 3.34.0
BuildRequires:	python3-fonttools < 4
BuildRequires:	python3-fs >= 2.2.0
BuildRequires:	python3-lxml >= 4.0
BuildRequires:	python3-py
BuildRequires:	python3-pytest
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	unzip
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ufoLib2 is a UFO font library.

%description -l pl.UTF-8
ufoLib2 to biblioteka do fontów UFO.

%package -n python3-ufoLib2
Summary:	UFO font library
Summary(pl.UTF-8):	Biblioteka do fontów UFO
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-ufoLib2
ufoLib2 is a UFO font library.

%description -n python3-ufoLib2 -l pl.UTF-8
ufoLib2 to biblioteka do fontów UFO.

%prep
%setup -q -n ufoLib2-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTHONPATH=$(pwd)/src \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/ufoLib2
%{py_sitescriptdir}/ufoLib2-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-ufoLib2
%defattr(644,root,root,755)
%doc README.md
%{py3_sitescriptdir}/ufoLib2
%{py3_sitescriptdir}/ufoLib2-%{version}-py*.egg-info
%endif
