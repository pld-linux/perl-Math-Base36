#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Base36
Summary:	Math::Base36 Perl module - Encoding and decoding of base36 strings
Summary(pl):	Modu³ Perla Math::Base36 - kodowanie i dekodowanie ³añcuchów base36
Name:		perl-Math-Base36
Version:	0.02
Release:	2
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	399c6850c99334627d2d9245c9ca0980
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module converts to and from Base36 numbers (0..9 - A..Z).

%description -l pl
Ten modu³ konwertuje do i z liczb Base36 (w systemie o podstawie 36 -
z cyframi 0..9,A..Z).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes LICENSE
%{perl_vendorlib}/Math/Base36.pm
%{perl_vendorlib}/auto/Math/Base36
%{_mandir}/man3/*
