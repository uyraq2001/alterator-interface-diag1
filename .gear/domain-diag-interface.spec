Name: doamain-diag-interface
Version: 0.1.0
Release: alt1

Summary: Xml files for domain-diag package.
License: GPLv2+
Group: Other
URL: https://github.com/uyraq2001/alterator-module-browser

Source0: %name-%version.tar

%description
Xml files describing D-Bus interfaces of domain-diag object.

%prep
%setup

%files
%datadir ru.basealt.alterator.diag1.xml ru.basealt.alterator.object.xml

%changelog
* Wed Aug 23 2023 Kozyrev Yuri <kozyrevid@altlinux.org> 0.1.0-alt1
- initial build
