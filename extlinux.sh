#!/bin/sh

# Copyright (C) 2015, 2017 Red Hat Inc.
# Author(s): Dennis Gilmore <dennis@ausil.us>
#            Merlin Mathesius <mmathesi@redhat.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.  See http://www.gnu.org/copyleft/gpl.html for
# the full text of the license.

# is the system a calxeda one
is_calxeda() {
    grep -Eq '^Hardware[^ ]* (Highbank|Midway)' /proc/cpuinfo
}

# update /etc/sysconfig/uboot to reflect if the platform provides its own dtb and
# we do not need to pass anything.
update_sysconfig() {
    sed -i -e 's/#SHIPSDTB=no/SHIPSDTB=yes/g' /etc/sysconfig/uboot
}

# insert into /boot/extlinux/extlinux.conf a fdtdir line
insert_fdtdir() {
    # for every 'kernel' directive found, map it to an 'fdtdir' directive
    # referencing the dtb directory and add it after the 'append' directive
    sed -i \
        -e '/	fdtdir/d' \
        -e '/	kernel/{h;s/kernel/fdtdir/g;s/vmlinuz/dtb/g;x}' \
        -e '/	append/{p;x}' \
        /boot/extlinux/extlinux.conf
}

# check if there is a rescue image and copy the dtb files if there is
copy_rescue_dtbs() {
    has_rescue=0
    for target in /boot/vmlinuz-0-rescue* ; do
        # if target exists, the glob matched a file
        if [ -e "$target" ] ; then
            has_rescue=1
            dtbdest=$(echo "$target" | sed -e 's/vmlinuz/dtb/g')
        fi
	break
    done
    for target in /boot/dtb* ; do
        # if target exists, the glob matched a file
        if [ -e "$target" ] ; then
            dtbsource="$target"
        fi
	break
    done
    if [ $has_rescue = 1 ] && [ ! -d "$dtbdest" ] ; then
       mkdir "$dtbdest"
       for dtb in $(ls "$dtbsource") ; do
           ln "$dtbsource/$dtb" "$dtbdest/$dtb"
       done
    fi
}

# platform ships its own dtb
if is_calxeda
then
    update_sysconfig
else
    # need to add fdtdir to extlinux.conf
    insert_fdtdir
    copy_rescue_dtbs
fi
