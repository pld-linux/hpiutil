Summary:	sys utils that conform to the SA Forum's Hardware Platform Interface specification
Summary(pl):	Narzêdzia systemowe zgodne ze specyfikacj± Hardware Platform Interface SA Forum
Name:		hpiutil
Version:	1.0.5
Release:	1
License:	BSD
Group:		Applications/System
Source0:	http://dl.sourceforge.net/panicsel/%{name}-%{version}.tar.gz
# Source0-md5:	686809b4d91b4a5998f9b048cb395c75
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

%description -l pl
Pakiet narzêdzi HPI dostarcza narzêdzia do zarz±dzania systemem zgodne
ze specyfikacj± Hardware Platform Interface (interfejsu platformy
sprzêtowej) SA Forum i jako takie s± niezale¿ne od sprzêtu dla
platform z implementacj± biblioteki HPI. Biblioteka HPI na platformach
intelowskich wymaga sterownika IPMI. Sterownik IPMI mo¿e byæ
dostarczony przez sterownik Intel IPMI (/dev/imb) lub OpenIPMI
(/dev/ipmi0) w j±drach Linuksa w wersji 2.4.20 lub wy¿szej.

%prep
%setup -q -c

%build
%{__make} \
	CC="%{__cc}" \
	DEBFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install $RPM_BUILD_ROOT%{_sbindir}

install hpialarmpanel hpisel hpifru hpisensor hpireset hpiwdt \
	$RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man?/*
