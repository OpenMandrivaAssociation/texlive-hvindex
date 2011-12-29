# revision 16136
# category Package
# catalog-ctan /macros/latex/contrib/hvindex
# catalog-date 2009-11-23 13:00:14 +0100
# catalog-license lppl
# catalog-version 0.02
Name:		texlive-hvindex
Version:	0.02
Release:	1
Summary:	Support for indexing
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hvindex
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hvindex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package simplifies the indexing of words using the \index
command of makeidx. With the package, to index a word in a
text, you only have to type it once; the package makes sure it
is both typeset and indexed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/hvindex/hvindex.sty
%doc %{_texmfdistdir}/doc/latex/hvindex/Changes
%doc %{_texmfdistdir}/doc/latex/hvindex/README
%doc %{_texmfdistdir}/doc/latex/hvindex/hvindex.pdf
%doc %{_texmfdistdir}/doc/latex/hvindex/hvindex.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
