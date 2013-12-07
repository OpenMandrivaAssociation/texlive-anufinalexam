# revision 26053
# category Package
# catalog-ctan /macros/latex/contrib/anufinalexam/ANUfinalexam.tex
# catalog-date 2012-04-17 00:02:56 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-anufinalexam
Version:	20120417
Release:	7
Summary:	LaTeX document shell for ANU final exam
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/anufinalexam/ANUfinalexam.tex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anufinalexam.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anufinalexam.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This LaTeX document shell is created for the standard
formatting of final exams in The Australian National
University.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/anufinalexam/ANUfinalexam.tex
%doc %{_texmfdistdir}/doc/latex/anufinalexam/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
