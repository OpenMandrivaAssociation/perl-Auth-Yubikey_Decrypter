%define module	Auth-Yubikey_Decrypter

Summary:	Decrypting the output from the yubikey token
Name:		perl-%{module}
Version:	0.05
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MASSYN/%{module}-%{version}.tar.gz
BuildRequires:	perl(Crypt::Rijndael)
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Yubikey Decrypter can be used to decrypt the AES encrypted output generated
from the one time password USB generator from Yubico. You need to have the AES
key to perform the decryption. You can obtain it by contacting Yubico, or by
seeding your own AES key to the Yubikey.

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Auth/Yubikey_Decrypter.pm
%{_mandir}/*/*

