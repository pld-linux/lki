Summary:	Linux Kernel 2.4 Internals
Summary(pl):	O kernelu 2.4
Name:		lki
Version:	20020807
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
# Source0-md5:	d296170427dbb52176fae57c9e93632a
URL:		http://www.tldp.org/LDP/lki/index.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An introduction to the Linux 2.4 kernel. The author is working as
senior Linux kernel engineer at VERITAS Software Ltd and wrote this
book for the purpose of supporting the short training course/lectures
he gave on this subject, internally at VERITAS.

%description -l pl
Wprowadzenie do Linuksa 2.4. Autor pracuje jako starszy in¿ynier w
firmie VERITAS Software Ltd i napisa³ tê ksi±¿kê jako pomocnicz± do
wyk³adów jakie tam prowadzi na temat Linuksa.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/lki
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/lki

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/lki
