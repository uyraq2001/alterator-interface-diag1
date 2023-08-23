Name: domain-diag-interface
Version: 0.1.0
Release: alt1

Summary: Xml files for domain-diag package.
License: GPLv2+
Group: Other
URL: https://github.com/uyraq2001/domain-diag-interface

Source0: %name-%version.tar

%description
Xml files describing D-Bus interfaces of domain-diag object.

%prep
%setup

%install
mkdir -p %buildroot%{_datadir}/d-bus1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.diag1.xml %buildroot%{_datadir}/d-bus1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.object.xml %buildroot%{_datadir}/d-bus1/interfaces
mkdir -p %buildroot%{_sysconfdir}/polkit-1/rules.d
install -v -p -m 644 -D 49-alterator.rules %buildroot%{_sysconfdir}/polkit-1/rules.d

%files
%{_datadir}/d-bus1/interfaces/ru.basealt.alterator.diag1.xml
%{_datadir}/d-bus1/interfaces/ru.basealt.alterator.object.xml
%{_sysconfdir}/polkit-1/rules.d/49-alterator.rules

%changelog
* Wed Aug 23 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.0-alt1
- initial build
