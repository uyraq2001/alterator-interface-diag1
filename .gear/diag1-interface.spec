Name: alterator-interface-diag1
Version: 0.1.0
Release: alt1

Summary: XML files for ru.basealt.alterator.diag1 interface.
License: GPLv2+
Group: Other
URL: https://github.com/uyraq2001/alterator-interface-diag1.git

Source0: %name-%version.tar

%description
XML files describing D-Bus interface ru.basealt.alterator.diag1 for ADT (Alt Diagnostic Tool).

%prep
%setup

%install
mkdir -p %buildroot%{_datadir}/dbus-1/interfaces
install -v -p -m 644 -D ru.basealt.alterator.diag1.xml %buildroot%{_datadir}/dbus-1/interfaces
mkdir -p %buildroot%{_sysconfdir}/polkit-1/rules.d
install -v -p -m 644 -D 49-alterator.rules %buildroot%{_sysconfdir}/polkit-1/rules.d

%files
%{_datadir}/dbus-1/interfaces/ru.basealt.alterator.diag1.xml
%{_sysconfdir}/polkit-1/rules.d/49-alterator.rules

%changelog
* Wed Aug 23 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.0-alt1
- initial build
