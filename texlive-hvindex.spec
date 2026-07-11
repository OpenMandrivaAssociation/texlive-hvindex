%global tl_name hvindex
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.04a
Release:	%{tl_revision}.1
Summary:	Support for indexing
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hvindex
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hvindex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package simplifies the indexing of words using the \index command of
makeidx. With the package, to index a word in a text, you only have to
type it once; the package makes sure it is both typeset and indexed.

