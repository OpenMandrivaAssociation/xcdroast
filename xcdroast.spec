%define	name	xcdroast
%define	alpharel	alpha15
%define	alpha	a15
%define	rel	37
%define release	%mkrel %{rel}.%{alpha}

Summary:	A GUI program for burning CDs
Name:		xcdroast
Version:	0.98
Release:	%{release}
Epoch:		10
URL:		http://www.xcdroast.org/
Source:		http://xcdroast.sourceforge.net/RPMS/%{alpha}/src/%{name}-%{version}%{alpharel}.tar.bz2
# icon
Patch:		xcdroast-0.98alpha15-dvd.patch.bz2
Patch1:		xcdroast-0.98alpha15-64bit-fixes.patch.bz2
Patch2:		xcdroast-0.98alpha15.spell.patch.bz2
Patch3:		xcdroast-linux-new_kernel.patch.bz2
License:	GPL
Group:		Archiving/Cd burning
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	cdrecord >= 4:2.01-0.a25.4mdk cdrecord-cdda2wav >= 4:2.01-0.a25.4mdk mkisofs >= 1:2.01-0.a25.4mdk
BuildRequires:	gtk2-devel libgdk_pixbuf2.0-devel pcre-devel pkgconfig
BuildRequires:	ImageMagick
BuildRequires:	bison

%description
X-CD-Roast is a program-package dedicated to easy CD creation
under most Unix-platforms. It combines command line tools like "cdrecord",
"cdda2wav", and "mkisofs" into a nice graphical user interface.

Features:
 Self-explanatory X11 user interface. 
 Automatic SCSI-hardware setup 
 Copies of ISO9660-CDs, some non-ISO9660-CDs, and audio CDs
 Production of new ISO9660 data CDs ("mastering")
 Production of new audio CDs
 Fast copying of CDs without hardisk buffering 
 Logfile option
 User interface in more than 10 languages

%prep
%setup -q -n %{name}-%{version}%{alpharel}
%patch -p1 -z .dvd
%patch1 -p1 -b .64bit-fixes
%patch2 -p1 -b .spell
%patch3 -p0

%build
%configure2_5x --with-xcdroast-libdir-prefix=%{_libdir}/xcdroast-0.98 --enable-gtk2
%make PREFIX=%{_prefix}

%install
rm -fr %{buildroot}
%makeinstall_std PREFIX=%{_prefix}

# icons
mkdir -p $RPM_BUILD_ROOT{%{_miconsdir},%{_iconsdir},%{_liconsdir}}
convert -size 48x48 xpms/xcdricon.xpm $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
convert -size 32x32 xpms/xcdricon.xpm $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -size 16x16 xpms/xcdricon.xpm $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

# menu
install -d %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/xcdroast <<EOF
?package(xcdroast): command="xcdroast -n" \
needs="X11" \
icon="%{name}.png" \
section="System/Archiving/CD Burning" \
title="X-CD-Roast" \
longtitle="X-CD-Roast" \
xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOXDG
[Desktop Entry]
Name=%{name}
Comment=X-CD-Roast tries to be the most flexible CD-burning software ever
Exec=%{_bindir}/%{name} -n
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-System-Archiving-CDBurning;AudioVideo;DiscBurning;
EOXDG

%find_lang %{name}

%post 
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog doc README 
%{_bindir}/xcdroast
%dir %{_libdir}/xcdroast-0.98
%dir %{_libdir}/xcdroast-0.98/bin
%{_libdir}/xcdroast-0.98/bin/*
%dir %{_libdir}/xcdroast-0.98/icons
%{_libdir}/xcdroast-0.98/icons/*
%dir %{_libdir}/xcdroast-0.98/sound
%{_libdir}/xcdroast-0.98/sound/*
%{_menudir}/xcdroast
%{_mandir}/man1/xcdroast.1*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
