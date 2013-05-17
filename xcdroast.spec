%define	alpharel	alpha15
%define	alpha		15

Summary:	A GUI program for burning CDs
Name:		xcdroast
Version:	0.98
Release:	0.a%{alpha}.41
Epoch:		11
URL:		http://www.xcdroast.org/
Source:		http://xcdroast.sourceforge.net/RPMS/%{alpha}/src/%{name}-%{version}%{alpharel}.tar.bz2
Patch1:		xcdroast-0.98alpha15-linebuffer.patch
Patch2:		xcdroast-0.98alpha15-nowarn.patch
Patch3:		xcdroast-0.98alpha15-scan.patch
Patch4:		xcdroast-0.98alpha15-fix-str-fmt.patch

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
BuildRequires:	pkgconfig(gdk-pixbuf-2.0) 
BuildRequires:	pcre-devel 
BuildRequires:	imagemagick
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
%patch4 -p0 -b .str

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
autoreconf -fi
%configure2_5x --with-xcdroast-libdir-prefix=%{_prefix}/lib/xcdroast-0.98 --enable-gtk2
%make PREFIX=%{_prefix}

%install
%makeinstall_std PREFIX=%{_prefix}

# icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -size 48x48 xpms/xcdricon.xpm %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -size 32x32 xpms/xcdricon.xpm %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -size 16x16 xpms/xcdricon.xpm %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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

%clean

%files -f %{name}.lang
%doc ChangeLog doc README 
%{_bindir}/xcdroast
%{_prefix}/lib/xcdroast-0.98
%{_mandir}/man1/xcdroast.1*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%{_iconsdir}/hicolor/16x16/apps/%{name}.png



%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 11:0.98-0.a15.40mdv2011.0
+ Revision: 615495
- the mass rebuild of 2010.1 packages

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 11:0.98-0.a15.39mdv2010.1
+ Revision: 508724
- fix str fmt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 11:0.98-0.a15.38mdv2009.0
+ Revision: 218426
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 11:0.98-0.a15.38mdv2008.0
+ Revision: 76389
- rebuild for 2008
- correct license, use Fedora license policy
- clean file list
- correct xdg categories
- run via soundwrapper as it plays audio
- better description in menu entry
- better name in menu entry
- fd.o icons
- put stuff in /usr/lib/xcdroast not %%_libdir/xcdroast as it's not at all arch-dependent
- use Fedora description, slightly modified
- update requires for cdrkit
- sync patches with Fedora (preserving our old patch2 and patch3 as patch40 and patch41; our old patch and patch1 are superseded). brings cdrkit support
- fix the stupidly broken and non-policy-conformant versioning: bump epoch
- Import xcdroast



* Tue Sep 05 2006 Stéphane Téletchéa <steletch@mandriva.org> 0.98-38.alpha15mdv2007.0
- Migration to XDG menus
- add mkrel macro

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.98-36.alpha16mdk
- Rebuild

* Fri Jul 15 2005 Per Ã˜yvind Karlsen <pkarlsen@mandriva.com> 0.98-36.alpha15mdk
- %%mkrel
- cosmetics
- from Michael Collard <quadfour@iinet.net.au> :
	o patch for non root writing on recent kernels (suid but not used)

* Mon Sep 06 2004 Marcel Pol <mpol@mandrake.org> 9:0.98-35.alpha15mdk
- fix menu section

* Wed Aug 25 2004 Warly <warly@mandrakesoft.com> 9:0.98-34.alpha15mdk
- fix a missing word (from list -> from this list)

* Wed Apr 14 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.98-33.alpha15mdk
- 64-bit fixes

* Mon Mar  1 2004 Warly <warly@mandrakesoft.com> 9:0.98-32.alpha15mdk
- Update DVD patch to allow ide burning

* Fri Jan 23 2004 Austin Acton <austin@mandrake.org> 0.98-31.alpha15mdk
- 0.98alpha15
- enable gtk2 build
- rediff the dvd patch
- add icon
- add some buildrequires

* Thu Oct  9 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.98-30.alpha14mdk
- fix build

* Mon Aug 11 2003 Warly <warly@mandrakesoft.com> 9:0.98-29.alpha14mdk
- fix segfault on startup with new cdrecord message

* Mon Jun 16 2003 Warly <warly@mandrakesoft.com> 9:0.98-28.alpha14mdk
- new version
- Activate DVD burning

* Thu Feb 20 2003 Warly <warly@mandrakesoft.com> 9:0.98-27.alpha13mdk
- new version
- rollback new child processing code completely 
- fixes the multisession problems introduced in alpha12.

* Fri Dec 27 2002 Warly <warly@mandrakesoft.com> 9:0.98-26mdk
- new version alpha12

* Fri Dec  6 2002 Warly <warly@mandrakesoft.com> 9:0.98-25mdk
- new version

* Mon Dec  2 2002 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.98-24mdk
- Make it lib64 aware

* Wed Sep  4 2002 Warly <warly@mandrakesoft.com> 9:0.98-23mdk
- change xcdwrite group to cdwriter group

* Mon Jul 29 2002 Stefan van der Eijk <stefan@eijk.nu> 0.98-22mdk
- BuildRequires

* Fri Apr 26 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-21mdk
- big cleanup from Thomas Niederreiter 
		o add missing files
		o remove obsolete actions
		o spec cleanups
		o remove patches

* Thu Apr 25 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-20mdk
- 0.98alpha10
	o redesign dialogs on startup
	o allow to select multiple master-paths/excludes at the same time
	o man page
    o pushed max write speed to 64x ...

* Thu Apr 18 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-19mdk
- mkisofs-1.15a21

* Fri Apr 12 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-18mdk
- no version check in menu : Denis Pelletier <denis.pelletier@umontreal.ca>

* Fri Apr 12 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-17mdk
- cdrecord-1.11a19, mkisofs-1.11a20
- no root-mode for cd audio access (cdda2wav > a19)

* Wed Feb 27 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-16mdk
- for cdrecord-1.11-0.a15

* Sun Feb 17 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-15mdk
- update to cdrecord-1.11-0.a14.

* Fri Jan 25 2002 Daouda LO <daouda@mandrakesoft.com> 0.98-14mdk
- dirty fix for cdrecord-1.11-0.a13. 

* Wed Jan 09 2002 David BAUDENS <baudens@mandrakesoft.com> 0.98-13mdk
- Fix menu entry using png icon

* Wed Oct 10 2001 Till Kamppeter <till@mandrakesoft.com> 0.98-12mdk
- Rebuilt for libpng3.

* Tue Sep 11 2001 David BAUDENS <baudens@mandrakesoft.com> 0.98-11mdk
- Use new icons
- Use right macros for update/clean_menus

* Tue Sep 11 2001 Stefan van der Eijk <stefan@eijk.nu> 0.98-10mdk
- BuildRequires: gtk+-devel imlib-devel
- Copyright --> License

* Tue Aug  7 2001 Till Kamppeter <till@mandrakesoft.com> 0.98-9mdk
- Updated to version 0.98alpha9.

* Fri Jun  7 2001 Till Kamppeter <till@mandrakesoft.com> 0.98-8mdk
- Downdated to version 0.98alpha6 (non-root-mode introduced in 0.98alpha7
  does not work with GTK 1.2.9, 0.98alpha6 can simply be started as normal
  user when backends have correct permissions)
- Enabled usage by non-root users via non-root mode of X-CD-Roast
- Enabled usage with cdrecord > 1.9

* Fri Mar 30 2001 Till Kamppeter <till@mandrakesoft.com> 0.98-7mdk
- Replaced translation update file by the current one

* Tue Feb  6 2001 Daouda Lo <daouda@mandrakesoft.com> 0.98-6mdk
- release alpha 8
- regenerate patch

* Mon Jan 29 2001  Daouda Lo <daouda@mandrakesoft.com> 0.98-5mdk
- really fix xcdroast requiring cdrtools 1.9 .

* Fri Jan 26 2001  Daouda Lo <daouda@mandrakesoft.com> 0.98-4mdk
- fix  requires (thanx Ed) 

* Fri Jan 26 2001  Daouda Lo <daouda@mandrakesoft.com> 0.98-3mdk
- fix dependencies with cdrecord (thanx Quel Qun)
- fix standard dir owned by packages 

* Thu Oct 05 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.98-2mdk
- All icons size.
- Icons now work.

* Sun Sep  3 2000 Till Kamppeter <till@mandrakesoft.com> 0.98-1mdk
- Old ChangeLog removed becasue structure of specfile is completely new
- Complete replacement by the new GTK-based X-CD-Roast 0.98
- initial release
