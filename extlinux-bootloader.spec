Name:           extlinux-bootloader
Version:        1.0
Release:        1%{?dist}
Summary:        The EXTLINUX bootloader framework, for booting the local system

License:        GPLv2+
URL:            http://fedoraproject.org/wiki/extlinux-bootloader

Provides:       syslinux-extlinux

ExclusiveArch:  %{arm}

%description
The EXTLINUX bootloader framework, for booting the local system.
u-boot on arm supports extlinux.conf config files

%prep


%build


%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/boot/extlinux/

mkdir -p %{buildroot}/etc
( cd %{buildroot}/etc && ln -s ../boot/extlinux/extlinux.conf . )
cat > %{buildroot}%{_sbindir}/extlinux <<EOF
#!/bin/bash
# dummy script to allow anaconda code to call extlinux to install bootloader
# needed to allow the same code used for anaconda to work everywhere
true
EOF
chmod 755 %{buildroot}%{_sbindir}/extlinux


%files
%doc
%{_sbindir}/extlinux
/boot/extlinux
%config(noreplace) /etc/extlinux.conf



%changelog
* Wed Jun 05 2013 Dennis Gilmore <dennis@ausil.us> - 1.0-1
- initial package
