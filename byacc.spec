Summary:     public domain yacc parser generator
Summary(de): Public Domain yacc-Parser-Generator
Summary(fr): Générateur d'analyseur lexical yacc du domaine public
Summary(pl): Generator analizatora sk³adni 
Summary(tr): Ayrýþtýrýcý üreteci
Name:        byacc
Version:     1.9
Release:     9
Copyright:   public domain
Group:       Development/Tools
Source:      ftp://ftp.cs.berkeley.edu/ucb/4bsd/%{name}.%{version}.tar.Z
Buildroot:   /tmp/%{name}-%{version}-root

%description
This is a public domain yacc parser. It is used by many programs during
their build process. You probably want this package if you do development.

%description -l de
Dies ist ein yacc-Parser aus dem Public Domain. Er wird von vielen
Programmen zum Aufbau benutzt. Als Entwickler sind, werden Sie dieses Paket
zu schätzen wissen.

%description -l fr
C'est un analyseur de syntaxe du domain public. Il est utilisé par de
nombreux programmes lors de leur processus de construction. Vous ne
voudrez probablement pas ce package si vous ne faîtes pas de développement.

%description -l pl
Yacc jest analizatorem sk³adni dostêpnym na zasadach w³asno¶ci publicznej,
czêsto wykorzystywanym podczas budowania programów. Je¿eli zamierzasz
zajmowaæ siê wytwarzaniem oprogramowania, warto zainstalowaæ ten pakiet.

%description -l tr
byacc bir yacc ayrýþtýrýcýsýdýr. Pek çok program tarafýndan, kurulum süreci
sýrasýnda kullanýlýr. Geliþtirme yapanlara gerekli olabilir.

%prep
%setup -c -q 

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s yacc $RPM_BUILD_ROOT/usr/bin
install yacc.1 $RPM_BUILD_ROOT/usr/man/man1

ln -sf yacc $RPM_BUILD_ROOT/usr/bin/byacc
echo ".so yacc.1" > $RPM_BUILD_ROOT/usr/man/man1/byacc.1

%files
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%changelog
* Mon Oct 26 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [1.9-9]
- byacc(1) man page is now maked as nroff include to yacc(1) instead
  making sym link to yacc.1 (this allow compress man pages in future).

* Wed Sep 23 1998 Marcin Korzonek <mkorz@shadow.eu.org>
- allow building from non root account,
- added using $RPM_OPT_FLAGS during compile,
- added pl translation.

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Thu Oct 23 1997 Donnie Barnes <djb@redhat.com>
- various spec file cleanups

* Mon Jun 02 1997 Erik Troan <ewt@redhat.com>
- built against glibc
