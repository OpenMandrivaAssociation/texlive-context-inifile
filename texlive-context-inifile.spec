Name:		texlive-context-inifile
Version:	47085
Release:	2
Summary:	An ini-file pretty-printer, using ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/context-inifile
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-inifile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-inifile.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The module parses an ini-file and prints the contents with a
user-defined layout. The entries of the file may be sorted by
up to three sort keys. The format of a simple ini-file would
be: [key1] symbol1 = value1 symbol2 = value2 [key2] symbol1 =
value3 symbol2 = value4 The module only works with ConTeXt
MkIV, and uses Lua to help process the input.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/context/third/inifile
%doc %{_texmfdistdir}/doc/context/third/inifile

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
