# Configuration Logic
%define name jube
%define version 2.2.1
%define unmangled_version 2.2.1
%define debug_package %{nil}
%undefine __brp_mangle_shebangs
%define _unpackaged_files_terminate_build 0

# Main preamble
Summary: JUBE Benchmarking Environment
Name: %{name}
Version: %{version}
Release:  1%{?dist}.edf
Source0: %{name}-%{unmangled_version}.tar.gz
License: GPLv3
Group: Application/System
Prefix: %{_prefix}
Vendor: Forschungszentrum Juelich GmbH
Packager: EDF CCN HPC <dsp-cspito-ccn-hpc@edf.fr>
Url: https://github.com/scibian/%{__name}

BuildRequires: git python3 

%description
JUBE Benchmarking Environment
 Automating benchmarks is important for reproducibility and
 hence comparability which is the major intent when
 performing benchmarks. Furthermore managing different
 combinations of parameters is error-prone and often
 results in significant amounts work especially if the
 parameter space gets large.
 .
 In order to alleviate these problems JUBE helps performing
 and analyzing benchmarks in a systematic way. It allows
 custom work flows to be able to adapt to new architectures.
 .
 For each benchmark application the benchmark data is written
 out in a certain format that enables JUBE to deduct the
 desired information. This data can be parsed by automatic
 pre- and post-processing scripts that draw information,
 and store it more densely for manual interpretation.
 .
 The JUBE benchmarking environment provides a script based
 framework to easily create benchmark sets, run those sets
 on different computer systems and evaluate the results. It
 is actively developed by the Juelich Supercomputing Centre
 of Forschungszentrum Juelich, Germany.

#########################################
# Prep, Setup, Build, Install & clean   #
#########################################

%prep
%setup -q

# Build Section
%build
python3 setup.py build

# Install & clean sections
%install
python3 setup.py install --single-version-externally-managed -O1 --root=%{buildroot}
install -d %{buildroot}/usr/share/jube/platform
install -d %{buildroot}/usr/share/jube/schema
install -d %{buildroot}/docs
cp -r contrib/schema %{buildroot}/usr/share/jube/schema
cp -r platform %{buildroot}/usr/share/jube/platform
install -m 644 docs/JUBE.pdf %{buildroot}/docs/

%clean
rm -rf %{buildroot}

##################
# Files Sections #
##################

%files
%defattr(-,root,root,-)
%doc README
%doc docs/JUBE.pdf
%license LICENSE
/usr/bin/jube
/usr/bin/jube-autorun
%{python3_sitelib}/jube2
%{python3_sitelib}/*.egg-info
/usr/share/jube

%changelog
* Fri Oct 09 2020 Romaric Kanyamibwa <romaric-externe.kanyamibwa@edf.fr> 1.0.2-1el8.edf
- Initial RPM release