Summary:	public domain yacc parser generator
Summary(de):	Public Domain yacc-Parser-Generator
Summary(fr):	G�n�rateur d'analyseur lexical yacc du domaine public
Summary(pl):	Generator analizatora sk�adni 
Summary(tr):	Ayr��t�r�c� �reteci
Name:		byacc
Version:	1.9
Release:	13
Copyright:	public domain
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://ftp.cs.berkeley.edu/ucb/4bsd/%{name}.%{version}.tar.Z
Patch0:		byacc-fixmanpage.patch
Provides:	yacc
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a public domain yacc parser. It is used by many programs
during their build process. You probably want this package if you do
development.

%description -l de
Dies ist ein yacc-Parser aus dem Public Domain. Er wird von vielen
Programmen zum Aufbau benutzt. Als Entwickler sind, werden Sie dieses
Paket zu sch�tzen wissen.

%description -l fr
C'est un analyseur de syntaxe du domain public. Il est utilis� par de
nombreux programmes lors de leur processus de construction. Vous ne
voudrez probablement pas ce package si vous ne fa�tes pas de
d�veloppement.

%description -l pl
Yacc jest analizatorem sk�adni dost�pnym na zasadach w�asno�ci
publicznej, cz�sto wykorzystywanym podczas budowania program�w. Je�eli
zamierzasz zajmowa� si� wytwarzaniem oprogramowania, warto
zainstalowa� ten pakiet.

%description -l tr
byacc bir yacc ayr��t�r�c�s�d�r. Pek �ok program taraf�ndan, kurulum
s�reci s�ras�nda kullan�l�r. Geli�tirme yapanlara gerekli olabilir.

%prep
%setup -c -q 
%patch -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install yacc $RPM_BUILD_ROOT%{_bindir}
install yacc.1 $RPM_BUILD_ROOT%{_mandir}/man1

ln -sf yacc $RPM_BUILD_ROOT%{_bindir}/byacc
echo ".so yacc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/byacc.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
