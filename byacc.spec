Summary:	public domain yacc parser generator
Summary(de):	Public Domain yacc-Parser-Generator
Summary(fr):	G�n�rateur d'analyseur lexical yacc du domaine public
Summary(pl):	Generator analizatora sk�adni
Summary(ru):	�������� ���������������� ��������� �������� Yacc
Summary(tr):	Ayr��t�r�c� �reteci
Summary(uk):	������ ���������������� ��������� �����Ҧ� Yacc
Name:		byacc
Version:	1.9
Release:	21
License:	public domain
Group:		Development/Tools
Source0:	ftp://ftp.cs.berkeley.edu/ucb/4bsd/%{name}.%{version}.tar.Z
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
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

%description -l ru
Byacc (Berkeley Yacc) - ��� �������� ���������������� ���������
�������� LALR, ������� ������������ ������� ����������� � �������� ��
����������.

%description -l tr
byacc bir yacc ayr��t�r�c�s�d�r. Pek �ok program taraf�ndan, kurulum
s�reci s�ras�nda kullan�l�r. Geli�tirme yapanlara gerekli olabilir.

%description -l uk
Byacc (Berkeley Yacc) - �� צ���� ���������������� ��������� �����Ҧ�
LALR, ���� ����������դ���� �������� ���������� � �����Ӧ �� ��������.

%prep
%setup -c -q
%patch0 -p1
%patch1 -p1
chmod -R u+Xrw .
%patch2 -p1
%patch3 -p1

%build
aclocal
autoheader
autoconf
automake -a -c
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
