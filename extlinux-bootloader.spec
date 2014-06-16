Name:           extlinux-bootloader
Version:        1.0
Release:        4%{?dist}
Summary:        The EXTLINUX bootloader framework, for booting the local system

License:        GPLv2+
URL:            http://fedoraproject.org/wiki/extlinux-bootloader

Provides:       syslinux-extlinux

ExclusiveArch:  %{arm} aarch64

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
* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-4
- Enable for build on aarch64 too

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Dennis Gilmore <dennis@ausil.us> - 1.0-1
- initial package
