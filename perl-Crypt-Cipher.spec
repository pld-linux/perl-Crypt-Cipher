#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Cipher
Summary:	Crypt::Cipher - very flexible base class for text ciphers
Summary(pl):	Crypt::Cipher - bardzo elastyczna klasa bazowa dla szyfr�w tekstowych
Name:		perl-Crypt-Cipher
Version:	0.02
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	65c132ea8ae178a182d0aba54d3f27ba
%{!?_without_tests:BuildRequires:	perl-Regexp-Tr >= 0.04}
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Regexp-Tr >= 0.04
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Cipher provides a standard interface and simple methods for
ciphers of various kinds, saving on development time and redundant
code.

%description -l pl
Modu� Crypt::Cipher dostarcza standardowy intefejs i proste metody dla
szyfr�w r�nego rodzaju, pozwalaj�c zaoszcz�dzi� na czasie
programowania i powielonym kodzie.

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
%doc README
%{perl_vendorlib}/Crypt/Cipher.pm
%{_mandir}/man3/*
