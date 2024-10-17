Name:		texlive-anufinalexam
Version:	26053
Release:	2
Summary:	LaTeX document shell for ANU final exam
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/anufinalexam/ANUfinalexam.tex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anufinalexam.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/anufinalexam.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Provides:		texlive-ANUfinalexam

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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
