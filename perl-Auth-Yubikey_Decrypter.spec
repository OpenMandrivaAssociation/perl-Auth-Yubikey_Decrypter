%define upstream_name	 Auth-Yubikey_Decrypter
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Decrypting the output from the yubikey token
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MASSYN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Crypt::Rijndael)

Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
The Yubikey Decrypter can be used to decrypt the AES encrypted output generated
from the one time password USB generator from Yubico. You need to have the AES
key to perform the decryption. You can obtain it by contacting Yubico, or by
seeding your own AES key to the Yubikey.

%prep

%setup -q -n %{upstream_name}-%{upstream_version}

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
