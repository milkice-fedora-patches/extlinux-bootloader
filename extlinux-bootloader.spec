Name:           extlinux-bootloader
Version:        1.1
Release:        2%{?dist}
Summary:        The EXTLINUX bootloader framework, for booting the local system

License:        GPLv2+
URL:            http://fedoraproject.org/wiki/extlinux-bootloader
Source1:        extlinux

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
install -p %{SOURCE1} %{buildroot}%{_sbindir}

%files
%doc
%{_sbindir}/extlinux
/boot/extlinux
%config(noreplace) /etc/extlinux.conf



%changelog
* Wed Apr 01 2015 Dennis Gilmore <dennis@ausil.us> - 1.1-2
- add a function to copy the dtbs to the rescue boot target if one exists

* Mon Mar 30 2015 Dennis Gilmore <dennis@ausil.us> - 1.1-1
- add a new extlinux script to setup dtb handling on arm 

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-4
- Enable for build on aarch64 too

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Dennis Gilmore <dennis@ausil.us> - 1.0-1
- initial package
