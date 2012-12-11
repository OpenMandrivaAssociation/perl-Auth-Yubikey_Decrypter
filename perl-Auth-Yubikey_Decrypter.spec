%define upstream_name	 Auth-Yubikey_Decrypter
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Decrypting the output from the yubikey token
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MASSYN/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::Rijndael)

BuildArch:	noarch

%description
The Yubikey Decrypter can be used to decrypt the AES encrypted output generated
from the one time password USB generator from Yubico. You need to have the AES
key to perform the decryption. You can obtain it by contacting Yubico, or by
seeding your own AES key to the Yubikey.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files 
%doc Changes README
%{perl_vendorlib}/Auth/Yubikey_Decrypter.pm
%{_mandir}/*/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 680483
- mass rebuild

* Sun Dec 13 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 478054
- update to 0.07

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.05-2mdv2010.0
+ Revision: 430264
- rebuild

* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdv2009.0
+ Revision: 285173
- import perl-Auth-Yubikey_Decrypter


* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 0.05-1mdv2009.0
- initial Mandriva package
