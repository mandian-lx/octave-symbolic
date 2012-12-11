%define	pkgname symbolic
%define name	octave-%{pkgname}
%define version 1.0.9

Summary:	Symbolic toolbox for Octave
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
Patch0:		is_list-1.0.9.patch
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/symbolic/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 3.1.55
BuildRequires:  octave-devel >= 3.1.55
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildRequires:	ginac-devel

%description
Symbolic toolbox for Octave based on ginac and cln.

%prep
%setup -q -c %{pkgname}-%{version}
tar zxf %SOURCE0
%patch0 -p0
tar zcvf %{pkgname}-%{version}.tar.gz %{pkgname}-%{version}

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
%__install -m 755 -d %{buildroot}%{_libdir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
export OCT_ARCH_PREFIX=%{buildroot}%{_libdir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX $OCT_ARCH_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}-%{version}/COPYING .
mv %{pkgname}-%{version}/DESCRIPTION .

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}
%{_libdir}/octave/packages/%{pkgname}-%{version}



%changelog
* Tue Aug 16 2011 Lev Givon <lev@mandriva.org> 1.0.9-1mdv2012.0
+ Revision: 694743
- import octave-symbolic


