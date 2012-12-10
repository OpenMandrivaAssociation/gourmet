Name: 	 	gourmet
Summary: 	Recipe manager for the GNOME desktop
Version: 	0.15.9
Release: 	%mkrel 2
Source:		http://prdownloads.sourceforge.net/grecipe-manager/%{name}-%{version}.tar.gz
URL:		http://grecipe-manager.sourceforge.net/
License:	GPLv2+
Group:		Graphical desktop/GNOME
BuildRequires:	python-devel 
BuildRequires:  python-metakit
BuildRequires:	imagemagick
BuildRequires:  desktop-file-utils
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-sqlite2
BuildRequires:	python-pyrtf
BuildRequires:	python-imaging
BuildRequires:	intltool
Requires:	gnome-python
Requires:	pygtk2.0-libglade
Requires:	python-metakit
Requires:	python-imaging
Requires:	python-sqlite2
Requires:	python-imaging
Requires:	python-reportlab
Requires:	gnome-python-gnomeprint
Requires:	gnome-python-gtkspell
Requires:	python-pyrtf
Requires:	python-sqlalchemy
Requires:	python-reportlab
Requires:	python-pypoppler
BuildArch:	noarch
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Gourmet allows you to collect, search and organize your recipes, and to
automatically generate shopping lists from your collection.

%prep
%setup -q

#fix .desktop file
sed -i -e 's/Icon=recbox.png/Icon=gourmet/g' %{name}.desktop.in

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot} --disable-modules-check

%find_lang %{name}

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

#icons
mkdir -p %{buildroot}%{_liconsdir}
convert -size 48x48 images/recbox.png %{buildroot}%{_liconsdir}/%{name}.png
mkdir -p %{buildroot}%{_iconsdir}
convert -size 32x32 images/recbox.png %{buildroot}%{_iconsdir}/%{name}.png
mkdir -p %{buildroot}%{_miconsdir}
convert -size 16x16 images/recbox.png %{buildroot}%{_miconsdir}/%{name}.png

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc CHANGES MANIFEST PKG-INFO README TODO
%{_bindir}/%{name}
%{py_puresitedir}/%{name}
%{py_puresitedir}/%{name}-%{version}-py%{py_ver}.egg-info
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Sun Apr 03 2011 Jani Välimaa <wally@mandriva.org> 0.15.9-2mdv2011.0
+ Revision: 650086
- require python-pypoppler

* Sat Apr 02 2011 Jani Välimaa <wally@mandriva.org> 0.15.9-1
+ Revision: 649885
- new version 0.15.9
- drop upstream applied patch
- drop support for old mdv versions
- drop buildroot definition
- clean .spec a bit

* Sun Dec 05 2010 Jani Välimaa <wally@mandriva.org> 0.15.6-3mdv2011.0
+ Revision: 609812
- add patch from Fedora to fix database update from older versions (mdv#61872)

* Mon Nov 08 2010 Jani Välimaa <wally@mandriva.org> 0.15.6-2mdv2011.0
+ Revision: 595107
- rebuild for python 2.7

* Mon Aug 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.15.6-1mdv2011.0
+ Revision: 572184
- update to 0.15.6

* Thu Jul 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.15.5-1mdv2011.0
+ Revision: 557047
- update to 0.15.5

* Thu Jun 17 2010 Frederic Crozat <fcrozat@mandriva.com> 0.15.4-2mdv2010.1
+ Revision: 548201
- ensure icon is visible for menu entry
- clean categories for menu entry, remove Database, gourmet shouldn't end in Development/Databases

* Mon Mar 08 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.15.4-1mdv2010.1
+ Revision: 515743
- update to 0.15.4

* Fri Dec 18 2009 Jérôme Brenier <incubusss@mandriva.org> 0.15.3-1mdv2010.1
+ Revision: 480010
- new version 0.15.3

* Sun Aug 30 2009 Frederik Himpe <fhimpe@mandriva.org> 0.15.0-1mdv2010.0
+ Revision: 422545
- Update to new version 0.15.0

* Sun Jul 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14.10-2mdv2010.0
+ Revision: 395353
- Requires gnome-python-gtkspell for spell checking plug-in which is
  activated by default

* Sat Jun 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14.10-1mdv2010.0
+ Revision: 390089
- update to new version 0.14.10

* Sun May 03 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14.7-2mdv2010.0
+ Revision: 371183
- Add python-sqlalchemy and python-reportlab Requires

* Sat May 02 2009 Frederik Himpe <fhimpe@mandriva.org> 0.14.7-1mdv2010.0
+ Revision: 370554
- BuildRequires: intltool
- Update to new version 0.14.7

* Fri Mar 06 2009 Emmanuel Andry <eandry@mandriva.org> 0.13.8-2mdv2009.1
+ Revision: 349935
- Requires gnome-python-gnomeprint, python-pyrtf

* Fri Mar 06 2009 Emmanuel Andry <eandry@mandriva.org> 0.13.8-1mdv2009.1
+ Revision: 349584
- New version 0.13.8
- fix license
- BR python-pyrtf instead of PyRTF

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.13.4-5mdv2009.1
+ Revision: 325572
- rebuild

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 0.13.4-4mdv2009.0
+ Revision: 240795
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Sep 23 2007 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 0.13.4-2mdv2008.0
+ Revision: 92319
- Minor indentation fix.

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix Requires (Bug #33924)
      Remove old menu

* Wed Sep 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.13.4-1mdv2008.0
+ Revision: 80014
- Add ImageMagick
- Add desktop-file-utils
- New release 0.13.4

  + Pascal Terjan <pterjan@mandriva.org>
    - Ship the .egg-info
    - Fix BuildRequires/Requires on metakit-python


* Sun Sep 03 2006 Emmanuel Andry <eandry@mandriva.org> 0.11.2-2mdv2007.0
- xdg menu
- buildrequires python-sqlite2 PyRTF python-imaging

* Thu May 04 2006 Austin Acton <austin@mandriva.org> 0.11.2-1mdk
- New release 0.11.2

* Mon Apr 24 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.8.5.13-2mdk
- Add BuildRequires
- use mkrel

* Thu Nov 10 2005 Austin Acton <austin@mandriva.org> 0.8.5.13-1mdk
- New release 0.8.5.13

* Thu Sep 08 2005 Austin Acton <austin@mandriva.org> 0.8.5.12-1mdk
- New release 0.8.5.12

* Thu Aug 04 2005 Austin Acton <austin@mandriva.org> 0.8.5.9-1mdk
- New release 0.8.5.9

* Wed Jun 22 2005 Austin Acton <austin@mandriva.org> 0.8.5.3-1mdk
- New release 0.8.5.3

* Sun Jun 05 2005 Austin Acton <austin@mandriva.org> 0.8.5.0-1mdk
- New release 0.8.5.0

* Fri May 20 2005 Austin Acton <austin@mandriva.org> 0.8.4.4-1mdk
- New release 0.8.4.4

* Wed May 18 2005 Austin Acton <austin@mandriva.org> 0.8.4.3-1mdk
- New release 0.8.4.3

* Wed May 11 2005 Austin Acton <austin@mandriva.org> 0.8.4.1-1mdk
- New release 0.8.4.1

* Sun Apr 24 2005 Austin Acton <austin@mandriva.org> 0.8.3.4-1mdk
- New release 0.8.3.4
- locales

* Sun Apr 17 2005 Austin Acton <austin@mandrake.org> 0.8.3.3-1mdk
- New release 0.8.3.3

* Wed Apr 06 2005 Austin Acton <austin@mandrake.org> 0.8.3-1mdk
- New release 0.8.3

* Thu Mar 24 2005 Austin Acton <austin@mandrake.org> 0.8.2.1-1mdk
- 0.8.2.1

* Mon Mar 21 2005 Austin Acton <austin@mandrake.org> 0.8.2-2.1mdk
- 0.8.2-2

* Mon Mar 21 2005 Austin Acton <austin@mandrake.org> 0.8.2-1mdk
- New release 0.8.2

* Thu Mar 17 2005 Austin Acton <austin@mandrake.org> 0.8.1.2-1mdk
- New release 0.8.1.2

* Fri Mar 11 2005 Austin Acton <austin@mandrake.org> 0.8.0-1mdk
- 0.8.0
- source URL

* Sat Jan 10 2004 Austin Acton <austin@mandrake.org> 0.7.1-1mdk
- initial package

