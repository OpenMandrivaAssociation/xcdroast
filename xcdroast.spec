%define	alpharel	alpha15
%define	alpha		15
%define	rel		38
%define release		%mkrel 0.a%{alpha}.%{rel}

Summary:	A GUI program for burning CDs
Name:		xcdroast
Version:	0.98
Release:	%{release}
Epoch:		11
URL:		http://www.xcdroast.org/
Source:		http://xcdroast.sourceforge.net/RPMS/%{alpha}/src/%{name}-%{version}%{alpharel}.tar.bz2
Patch1:		xcdroast-0.98alpha15-linebuffer.patch
Patch2:		xcdroast-0.98alpha15-nowarn.patch
Patch3:		xcdroast-0.98alpha15-scan.patch

Patch11:	xcdroast-0.98alpha15-01_upstream_configure.patch
Patch12:	xcdroast-0.98alpha15-02_upstream_gtk2locale.patch
Patch13:	xcdroast-0.98alpha15-03_upstream_64bit_gsize.patch
Patch14:	xcdroast-0.98alpha15-04_upstream_read_eagain.patch
Patch15:	xcdroast-0.98alpha15-05_upstream_wav.patch
Patch16:	xcdroast-0.98alpha15-06_man.patch
Patch17:	xcdroast-0.98alpha15-07_case_cmp.patch
Patch18:	xcdroast-0.98alpha15-08_desktop.patch
Patch19:	xcdroast-0.98alpha15-09_share_dir.patch
Patch20:	xcdroast-0.98alpha15-10_cddbtool.patch
Patch21:	xcdroast-0.98alpha15-11_mkisofs_options.patch
Patch22:	xcdroast-0.98alpha15-12_cdrecord_versions.patch
Patch23:	xcdroast-0.98alpha15-13_cdrecord_to_wodim.patch
Patch24:	xcdroast-0.98alpha15-14_atapi_to_oldatapi.patch
Patch25:	xcdroast-0.98alpha15-15_no_readcd_version.patch

Patch30:	xcdroast-0.98alpha15-prodvd.patch
Patch31:	xcdroast-0.98alpha15-frozen_gui.patch
Patch32:	xcdroast-0.98alpha15-nogtk1.patch

Patch40:	xcdroast-0.98alpha15.spell.patch
Patch41:	xcdroast-linux-new_kernel.patch
License:	LGPLv2+
Group:		Archiving/Cd burning
Requires: 	cdrkit
Requires:	cdrkit-genisoimage
Requires:	cdrkit-icedax
BuildRequires:	gtk2-devel 
BuildRequires:	libgdk_pixbuf2.0-devel 
BuildRequires:	pcre-devel 
BuildRequires:	ImageMagick
BuildRequires:	bison

%description
X-CD-Roast provides a GUI interface for writing optical discs and disc 
images. X-CD-Roast includes a self-explanatory X11 user interface,
automatic SCSI and IDE hardware setup, support for mastering of new
ISO9660 data CDs, support for production of new audio CDs, fast
copying of CDs without hard disk buffering, and a logfile option.

%prep
%setup -q -n %{name}-%{version}%{alpharel}
%patch1 -p1 -b .linebuffer
%patch2 -p1 -b .nowarn
%patch3 -p1 -b .scan

%patch11 -p1 -b .p11
%patch12 -p1 -b .p12
%patch13 -p1 -b .p13
%patch14 -p1 -b .p14
%patch15 -p1 -b .p15
%patch16 -p1 -b .p16
%patch17 -p1 -b .p17
%patch18 -p1 -b .p18
%patch19 -p1 -b .p19
%patch20 -p1 -b .p20
%patch21 -p0 -b .p21
%patch22 -p1 -b .p22
%patch23 -p1 -b .p23
%patch24 -p0 -b .p24
%patch25 -p1 -b .p25

%patch30 -p1 -b .cdrkit
%patch31 -p1 -b .frozen
%patch32 -p1 -b .nogtk1

%patch40 -p1 -b .spell
%patch41 -p0

%build
%configure2_5x --with-xcdroast-libdir-prefix=%{_prefix}/lib/xcdroast-0.98 --enable-gtk2
%make PREFIX=%{_prefix}

%install
rm -fr %{buildroot}
%makeinstall_std PREFIX=%{_prefix}

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -size 48x48 xpms/xcdricon.xpm $RPM_BUILD_ROOT%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -size 32x32 xpms/xcdricon.xpm $RPM_BUILD_ROOT%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -size 16x16 xpms/xcdricon.xpm $RPM_BUILD_ROOT%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=X-CD-Roast
Comment=CD / DVD writing application
Exec=soundwrapper %{_bindir}/%{name} -n
Icon=%{name}
Terminal=false
Type=Application
Categories=GTK;AudioVideo;DiscBurning;
EOF

%find_lang %{name}

%post 
%update_menus
%{update_icon_cache hicolor}

%postun
%clean_menus
%{clean_icon_cache hicolor}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc ChangeLog doc README 
%{_bindir}/xcdroast
%{_prefix}/lib/xcdroast-0.98
%{_mandir}/man1/xcdroast.1*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png

