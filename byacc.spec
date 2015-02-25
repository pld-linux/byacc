Summary:	Public domain yacc parser generator
Summary(de.UTF-8):	Public Domain yacc-Parser-Generator
Summary(es.UTF-8):	Yacc, generador de parser de dominio público
Summary(fr.UTF-8):	Générateur d'analyseur lexical yacc du domaine public
Summary(pl.UTF-8):	Generator analizatora składni
Summary(pt_BR.UTF-8):	Yacc, gerador de parser de domínio público
Summary(ru.UTF-8):	Свободно распространяемый генератор парсеров Yacc
Summary(tr.UTF-8):	Ayrıştırıcı üreteci
Summary(uk.UTF-8):	Вільно розповсюджуваний генератор парсерів Yacc
Name:		byacc
Version:	1.9
Release:	27
License:	Public Domain
Group:		Development/Tools
Source0:	ftp://ftp.cs.berkeley.edu/ucb/4bsd/%{name}.%{version}.tar.Z
# Source0-md5:	646801f9c335dc8d35ad044b526b289e
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	2de3e6e1e7098a7c9e5492f5b3911d56
Patch0:		%{name}-fixmanpage.patch
Patch1:		%{name}-fix.patch
Patch2:		%{name}-security.patch
Patch3:		%{name}-automake.patch
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	yacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a public domain yacc parser. It is used by many programs
during their build process. You probably want this package if you do
development.

%description -l de.UTF-8
Dies ist ein yacc-Parser aus dem Public Domain. Er wird von vielen
Programmen zum Aufbau benutzt. Als Entwickler sind, werden Sie dieses
Paket zu schätzen wissen.

%description -l es.UTF-8
Este es un analista gramatical yacc de dominio público. Se usa en
varios programas durante su proceso de construcción. Probablemente
querrás este paquete si te dedicas al desarrollo.

%description -l fr.UTF-8
C'est un analyseur de syntaxe du domain public. Il est utilisé par de
nombreux programmes lors de leur processus de construction. Vous ne
voudrez probablement pas ce package si vous ne faîtes pas de
développement.

%description -l pl.UTF-8
Yacc jest analizatorem składni dostępnym na zasadach własności
publicznej, często wykorzystywanym podczas budowania programów. Jeżeli
zamierzasz zajmować się wytwarzaniem oprogramowania, warto
zainstalować ten pakiet.

%description -l pt_BR.UTF-8
Este é um analisador gramatical yacc de domínio público. Ele é
usado em vários programas durante seu processo de construção. Você
provavelmente vai querer este pacote se você faz desenvolvimento.

%description -l ru.UTF-8
Byacc (Berkeley Yacc) - это свободно распространяемый генератор
парсеров LALR, который используется многими программами в процессе их
построения.

%description -l tr.UTF-8
byacc bir yacc ayrıştırıcısıdır. Pek çok program tarafından, kurulum
süreci sırasında kullanılır. Geliştirme yapanlara gerekli olabilir.

%description -l uk.UTF-8
Byacc (Berkeley Yacc) - це вільно розповсюджуваний генератор парсерів
LALR, який використовується багатьма програмами в процесі їх побудови.

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
