%define octpkg symbolic

Summary:	Symbolic toolbox for Octave
Name:		octave-%{octpkg}
Version:	2.5.0
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 4.0.0

Requires:	octave(api) = %{octave_api}
Requires:	python-sympy >= 1.0

Requires(post): octave
Requires(postun): octave

%description
The Octave-Forge Symbolic package adds symbolic calculation
features to GNU Octave.  These include common Computer Algebra System tools
such as algebraic operations, calculus, equation solving, Fourier and Laplace
transforms, variable precision arithmetic and other features.  Internally,
the package uses [SymPy](www.sympy.org), but no knowledge of Python is
required.  Compatibility with other symbolic toolboxes is intended.

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}-%{version}/NEWS
%doc %{octpkg}-%{version}/COPYING

