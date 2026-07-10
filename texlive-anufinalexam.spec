%global tl_name anufinalexam
%global tl_revision 26053

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX document shell for ANU final exam
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/anufinalexam
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anufinalexam.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/anufinalexam.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX document shell is created for the standard formatting of
final exams in The Australian National University.

