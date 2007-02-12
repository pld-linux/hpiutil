Summary:	sys utils that conform to the SA Forum's Hardware Platform Interface specification
Summary(pl.UTF-8):   Narzędzia systemowe zgodne ze specyfikacją Hardware Platform Interface SA Forum
Name:		hpiutil
Version:	1.1.3
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/panicsel/%{name}-%{version}.tar.gz
# Source0-md5:	bd20ec134d1251c47ffce9ffa6b6e2c1
URL:		http://panicsel.sourceforge.net/
BuildRequires:	openhpi-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The HPI utilities package provides system management utilities that
conform to the SA Forum's Hardware Platform Interface specification,
and as such are hardware-independent across platforms that have an HPI
library implementation.  The HPI library on Intel platforms requires
an IPMI driver.  An IPMI driver can be provided by either the Intel
IPMI driver (/dev/imb) or the OpenIPMI driver (/dev/ipmi0) in Linux
kernel versions 2.4.20 and greater.

%description -l pl.UTF-8
Pakiet narzędzi HPI dostarcza narzędzia do zarządzania systemem zgodne
ze specyfikacją Hardware Platform Interface (interfejsu platformy
sprzętowej) SA Forum i jako takie są niezależne od sprzętu dla
platform z implementacją biblioteki HPI. Biblioteka HPI na platformach
intelowskich wymaga sterownika IPMI. Sterownik IPMI może być
dostarczony przez sterownik Intel IPMI (/dev/imb) lub OpenIPMI
(/dev/ipmi0) w jądrach Linuksa w wersji 2.4.20 lub wyższej.

%prep
%setup -q -c

%build
%{__make} \
	CC="%{__cc}" \
	DEBFLAGS="%{rpmcflags}" \
	LIBDIR=/usr/%{_lib} \
	LIBHPI=openhpi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

install hpialarmpanel hpisel hpifru hpisensor hpireset hpiwdt \
	$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
