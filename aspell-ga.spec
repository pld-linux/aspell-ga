Summary:	Irish dictionary for aspell
Summary(pl.UTF-8):   Słownik irlandzki dla aspella
Name:		aspell-ga
Version:	4.1
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/ga/aspell5-ga-%{version}-%{subv}.tar.bz2
# Source0-md5:	e5f4e3a1925f7cdc7f2f65a8ab990c94
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 2:0.50.0
Requires:	aspell >= 2:0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Irish dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik irlandzki (lista słów) dla aspella.

%prep
%setup -q -n aspell5-ga-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/ChangeLog
%{_libdir}/aspell/*
%{_datadir}/aspell/*
