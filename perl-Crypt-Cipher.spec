#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Crypt
%define		pnam	Cipher
Summary:	Crypt::Cipher - very flexible base class for text ciphers
Summary(pl.UTF-8):	Crypt::Cipher - bardzo elastyczna klasa bazowa dla szyfrów tekstowych
Name:		perl-Crypt-Cipher
Version:	0.03
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d4467342f81a0adb1f53cabb9cd473b
URL:		http://search.cpan.org/dist/Crypt-Cipher/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Regexp-Tr >= 0.04
%endif
Requires:	perl-Regexp-Tr >= 0.04
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Crypt::Cipher provides a standard interface and simple methods for
ciphers of various kinds, saving on development time and redundant
code.

%description -l pl.UTF-8
Moduł Crypt::Cipher dostarcza standardowy interfejs i proste metody
dla szyfrów różnego rodzaju, pozwalając zaoszczędzić na czasie
programowania i powielonym kodzie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
