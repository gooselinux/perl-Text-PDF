Name:       perl-Text-PDF 
Version:    0.29a 
Release:    2.1%{?dist}
# lib/Text/PDF.pm -> GPL+ or Artistic
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Module for manipulating PDF files 
Source:     http://search.cpan.org/CPAN/authors/id/M/MH/MHOSKEN/Text-PDF-%{version}.tar.gz 
Url:        http://search.cpan.org/dist/Text-PDF
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n) 
Requires:   perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
BuildArch:  noarch

BuildRequires: perl(Compress::Zlib)
BuildRequires: perl(ExtUtils::MakeMaker)
Requires:      pdf-tools = %{version}-%{release}

%description
This module allows interaction with existing PDF files directly. It
includes various tools:

    pdfbklt   - make booklets out of existing PDF files 
    pdfrevert - remove edits from a PDF file 
    pdfstamp  - stamp text on each page of a PDF file

%package -n pdf-tools
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Manipulate PDF files
Requires:   %{name} = %{version}-%{release}

%description -n pdf-tools
This package allows existing PDF files to be modified; and includes various
tools:

    pdfbklt   - make booklets out of existing PDF files 
    pdfrevert - remove edits from a PDF file 
    pdfstamp  - stamp text on each page of a PDF file
    
%prep
# FIXME ugh.  This is the way upstream has it, tho
%setup -q -n Text-PDF-0.29

find . -type f -exec chmod -c -x     {} ';'
find . -type f -exec sed -i 's/\r//' {} ';'

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot} 

%files
%defattr(-,root,root,-)
%doc readme.txt examples/
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%files -n pdf-tools
%defattr(-,root,root,-)
%doc readme.txt
%{_bindir}/*

%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.29a-2.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.29a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.29a-1
- submission
- add pdf-tools subpackage

* Mon Jun 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.29a-0
- initial RPM packaging
- generated with cpan2dist (CPANPLUS::Dist::RPM version 0.0.8)

