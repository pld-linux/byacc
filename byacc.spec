Summary:	public domain yacc parser generator
Summary(de):	Public Domain yacc-Parser-Generator
Summary(es): Yacc, generador de parser de dominio público
Summary(fr):	Générateur d'analyseur lexical yacc du domaine public
Summary(pl):	Generator analizatora sk³adni
Summary(pt_BR): Yacc, gerador de parser de domínio público
Summary(ru):	ó×ÏÂÏÄÎÏ ÒÁÓÐÒÏÓÔÒÁÎÑÅÍÙÊ ÇÅÎÅÒÁÔÏÒ ÐÁÒÓÅÒÏ× Yacc
Summary(tr):	Ayrýþtýrýcý üreteci
Summary(uk):	÷¦ÌØÎÏ ÒÏÚÐÏ×ÓÀÄÖÕ×ÁÎÉÊ ÇÅÎÅÒÁÔÏÒ ÐÁÒÓÅÒ¦× Yacc
Name:		byacc
Version:	1.9
Release:	23
License:	Public Domain
Group:		Development/Tools
Source0:	ftp://ftp.cs.berkeley.edu/ucb/4bsd/%{name}.%{version}.tar.Z
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
Patch0:		%{name}-fixmanpage.patch
Patch1:		%{name}-fix.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
Obsoletes:	bison
Provides:	yacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a public domain yacc parser. It is used by many programs
during their build process. You probably want this package if you do
development.

%description -l de
Dies ist ein yacc-Parser aus dem Public Domain. Er wird von vielen
Programmen zum Aufbau benutzt. Als Entwickler sind, werden Sie dieses
Paket zu schätzen wissen.

%description -l es
Este es un analista gramatical yacc de dominio público. Se usa en
varios programas durante su proceso de construcción. Probablemente
querrás este paquete si te dedicas al desarrollo.

%description -l fr
C'est un analyseur de syntaxe du domain public. Il est utilisé par de
nombreux programmes lors de leur processus de construction. Vous ne
voudrez probablement pas ce package si vous ne faîtes pas de
développement.

%description -l pl
Yacc jest analizatorem sk³adni dostêpnym na zasadach w³asno¶ci
publicznej, czêsto wykorzystywanym podczas budowania programów. Je¿eli
zamierzasz zajmowaæ siê wytwarzaniem oprogramowania, warto
zainstalowaæ ten pakiet.

%description -l pt_BR
Este é um analisador gramatical yacc de domínio público. Ele é
usado em vários programas durante seu processo de construção. Você
provavelmente vai querer este pacote se você faz desenvolvimento.

%description -l ru
Byacc (Berkeley Yacc) - ÜÔÏ Ó×ÏÂÏÄÎÏ ÒÁÓÐÒÏÓÔÒÁÎÑÅÍÙÊ ÇÅÎÅÒÁÔÏÒ
ÐÁÒÓÅÒÏ× LALR, ËÏÔÏÒÙÊ ÉÓÐÏÌØÚÕÅÔÓÑ ÍÎÏÇÉÍÉ ÐÒÏÇÒÁÍÍÁÍÉ × ÐÒÏÃÅÓÓÅ ÉÈ
ÐÏÓÔÒÏÅÎÉÑ.

%description -l tr
byacc bir yacc ayrýþtýrýcýsýdýr. Pek çok program tarafýndan, kurulum
süreci sýrasýnda kullanýlýr. Geliþtirme yapanlara gerekli olabilir.

%description -l uk
Byacc (Berkeley Yacc) - ÃÅ ×¦ÌØÎÏ ÒÏÚÐÏ×ÓÀÄÖÕ×ÁÎÉÊ ÇÅÎÅÒÁÔÏÒ ÐÁÒÓÅÒ¦×
LALR, ÑËÉÊ ×ÉËÏÒÉÓÔÏ×Õ¤ÔØÓÑ ÂÁÇÁÔØÍÁ ÐÒÏÇÒÁÍÁÍÉ × ÐÒÏÃÅÓ¦ §È ÐÏÂÕÄÏ×É.

%prep
%setup -c -q
%patch0 -p1
%patch1 -p1
chmod -R u+Xrw .
%patch2 -p1
%patch3 -p1

%build
rm -f missing
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf yacc $RPM_BUILD_ROOT%{_bindir}/byacc
echo ".so yacc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/byacc.1

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
%lang(ko) %{_mandir}/ko/man1/*
%lang(pl) %{_mandir}/pl/man1/*
