%define module cram

Name:           python-%{module}
Version:        0.7
Release:        4
Summary:        Simple testing framework for command line applications
Group:          Development/Python
License:        GPLv2
Url:            https://bitheap.org/cram/
Source0:        http://pypi.python.org/packages/source/c/%{module}/%{module}-%{version}.tar.gz
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildArch:      noarch

%description
Cram tests look like snippets of interactive shell sessions. Cram runs each
command and compares the command output in the test with the command's actual
output.

%files -n python-%{module}
%doc README.* COPYING.txt NEWS.*
%{_bindir}/cram
%{py_puresitedir}/%{module}/
%{py_puresitedir}/%{module}-%{version}-py*.egg-info
#------------------------------------------------------------------------------

%prep
%setup -qn %{module}-%{version}

# remove shebangs
find . -type f -name '*.py' \
  -exec sed -i -e '/^#!/{1D}' {} \;

%build
%py_build

%install
%py_install
