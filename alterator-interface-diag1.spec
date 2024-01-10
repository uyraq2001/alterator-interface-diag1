Name: alterator-interface-diag1
Version: 0.1.0
Release: alt1

Summary: XML files for ru.basealt.alterator.diag1 interface.
License: GPLv2+
Group: Other
URL: https://github.com/AlexSP0/alterator-interface-diag1.git

BuildArch: noarch

Source0: %name-%version.tar

%description
XML files describing D-Bus interface ru.basealt.alterator.diag1 for ADT (Alt Diagnostic Tool).

%prep
%setup

%install
install -p -m 644 -D ru.basealt.alterator.diag1.xml %buildroot%_datadir/dbus-1/interfaces/ru.basealt.alterator.diag1.xml
install -p -m 644 -D ru.basealt.alterator.diag1.policy %buildroot%_datadir/polkit-1/actions/ru.basealt.alterator.diag1.policy

%files
%_datadir/dbus-1/interfaces/ru.basealt.alterator.diag1.xml
%_datadir/polkit-1/actions/ru.basealt.alterator.diag1.policy

%changelog
* Tue Nov 14 2023 Aleksey Saprunov <sav@altlinux.org> 0.1.0-alt1
- initial build
