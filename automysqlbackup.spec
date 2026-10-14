%global commit0 7c0043ad4a2e5a0090a28cc9b9212eb6ee426c66
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:		automysqlbackup
Version:	3.0
Release:	1+mike1%{?dist}
Summary:	MySQL/MariaDB backup script
Group:		Applications/Databases
License:	GPLv2+
URL:		https://github.com/ksyz/automysqlbackup
Source0:	https://github.com/ksyz/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildArch:	noarch
Requires:	bash
Requires:	bzip2
Requires:	gzip
Requires:	diffutils
Requires:	openssl
Requires:	(mariadb or mysql)

%description
MySQL/MariaDB backup wrapper script for mysqldump, with support for 
backup rotation, compression and incremental backup.

%prep
%setup -qn %{name}-%{commit0}
sed -e 's|#!/usr/bin/env bash|#!/usr/bin/bash|g' -i automysqlbackup

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
* Sun May 02 2021 Mike Gerber <mike@sprachgewalt.de> 3.0-1+mike1
- Require mariadb or mysql

* Mon Dec 14 2015 Michal Ingeli <mi@v3.sk> 3.0-1
- Initial package
