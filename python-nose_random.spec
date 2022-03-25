#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Random scenario testing in Nose
Summary(pl.UTF-8):	Testowanie losowych scenariuszy w Nose
Name:		python-nose_random
Version:	1.0.0
Release:	4
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/fzumstein/nose-random/releases
Source0:	https://github.com/fzumstein/nose-random/archive/%{version}/nose-random-%{version}.tar.gz
# Source0-md5:	302e05c65601a0239aaf8616f39a4cd4
URL:		https://github.com/fzumstein/nose-random
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
nose-random is designed to facilitate Monte-Carlo style unit testing.
The idea is to improve testing by running your code against a large
number of randomly generated input scenarios.

%description -l pl.UTF-8
nose-random jest zaprojektowany, aby wspomóc testowanie jednostkowe w
stylu Monte-Carlo. Idea ta polega na testowaniu przez uruchamianie
kodu na dużej liczbie losowo wygenerowanych scenariuszy wejściowych.

%package -n python3-nose_random
Summary:	Random scenario testing in Nose
Summary(pl.UTF-8):	Testowanie losowych scenariuszy w Nose
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-nose_random
nose-random is designed to facilitate Monte-Carlo style unit testing.
The idea is to improve testing by running your code against a large
number of randomly generated input scenarios.

%description -n python3-nose_random -l pl.UTF-8
nose-random jest zaprojektowany, aby wspomóc testowanie jednostkowe w
stylu Monte-Carlo. Idea ta polega na testowaniu przez uruchamianie
kodu na dużej liczbie losowo wygenerowanych scenariuszy wejściowych.

%prep
%setup -q -n nose-random-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python-nose_random-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python-nose_random-%{version}

%py_postclean
%endif

%if %{with python3}
%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-nose_random-%{version}
cp -p examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-nose_random-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py_sitescriptdir}/nose_random
%{py_sitescriptdir}/nose_random-0.0.1-py*.egg-info
%{_examplesdir}/python-nose_random-%{version}
%endif

%if %{with python3}
%files -n python3-nose_random
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/nose_random
%{py3_sitescriptdir}/nose_random-0.0.1-py*.egg-info
%{_examplesdir}/python3-nose_random-%{version}
%endif
