Name:		automysqlbackup
Version:	3.0.7
Release:	1~mike1%{?dist}
Summary:	MySQL/MariaDB backup script
Group:		Applications/Databases
License:	GPLv2+

%global github_tag %{version}

URL:			https://github.com/sixhop/AutoMySQLBackup
Source0:	https://github.com/sixhop/AutoMySQLBackup/archive/%{github_tag}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:	  76.patch

BuildArch:	noarch
Requires:	bash
Requires:	bzip2
Requires:	gzip
Requires:	pigz
Requires:	diffutils
Requires:	openssl
Requires:	(mariadb or mysql)

%description
MySQL/MariaDB backup wrapper script for mysqldump, with support for
backup rotation, compression and incremental backup.

%prep
%setup -qn AutoMySQLBackup-%{version}
sed -e 's|#!/usr/bin/env bash|#!/usr/bin/bash|g' -i automysqlbackup
%patch -P0 -p1

%build
true

%install
install -m 755 -d %{buildroot}/%{_bindir}
install -m 755 -d %{buildroot}/%{_sysconfdir}/automysqlbackup

install -m 755 automysqlbackup %{buildroot}/%{_bindir}/automysqlbackup
install -m 600 automysqlbackup.conf %{buildroot}/%{_sysconfdir}/automysqlbackup/automysqlbackup.conf


%files
%{_bindir}/automysqlbackup
%config(noreplace) %{_sysconfdir}/automysqlbackup/automysqlbackup.conf
%doc README.md LICENSE CHANGELOG

%changelog
* Wed Oct 14 2026 Mike Gerber <mike@mike-gerber.de> 3.0.7-1~mike1
- Switch to sixhop fork
- Update to 3.0.7
- Require pigz
- Add PR#76 to support mariadb-dump/remove deprecation warnings

* Sun May 02 2021 Mike Gerber <mike@sprachgewalt.de> 3.0-1+mike1
- Require mariadb or mysql

* Mon Dec 14 2015 Michal Ingeli <mi@v3.sk> 3.0-1
- Initial package
