%define name	gourmet
%define version 0.11.2
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Recipe manager for the GNOME desktop
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/grecipe-manager/%{name}-%{version}.tar.bz2
URL:		http://grecipe-manager.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel 
BuildRequires:  metakit-python
BuildRequires:  pygtk2.0-devel python-sqlite2 PyRTF python-imaging
Requires:	gnome-python pygtk2.0-libglade
Requires:	metakit-python python-imaging python-sqlite2 python-imaging
BuildArch:	noarch

%description
Gourmet allows you to collect, search and organize your recipes, and to
automatically generate shopping lists from your collection.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%find_lang %name

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="Gourmet" longtitle="Recipe Manager" section="More Applications/Databases"\
xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Other" \
  --add-category="GTK" \
  --add-category="Database;Office" \
  --add-category="X-MandrivaLinux-MoreApplications-Databases" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*


#icons
mkdir -p $RPM_BUILD_ROOT/%_liconsdir
convert -size 48x48 images/recbox.png $RPM_BUILD_ROOT/%_liconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_iconsdir
convert -size 32x32 images/recbox.png $RPM_BUILD_ROOT/%_iconsdir/%name.png
mkdir -p $RPM_BUILD_ROOT/%_miconsdir
convert -size 16x16 images/recbox.png $RPM_BUILD_ROOT/%_miconsdir/%name.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
		
%postun
%clean_menus

%files -f %name.lang
%defattr(-,root,root)
%doc CHANGES MANIFEST PKG-INFO README TODO
%{_bindir}/%name
%{_libdir}/python*/site-packages/%name
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

