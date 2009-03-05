%define name	gourmet
%define version 0.13.8
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Recipe manager for the GNOME desktop
Version: 	%{version}
Release: 	%{release}

Source:		http://prdownloads.sourceforge.net/grecipe-manager/%{name}-%{version}.tar.gz
URL:		http://grecipe-manager.sourceforge.net/
License:	GPLv2+
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	python-devel 
BuildRequires:  python-metakit imagemagick
BuildRequires:  desktop-file-utils pygtk2.0-devel python-sqlite2 python-pyrtf python-imaging
Requires:	gnome-python pygtk2.0-libglade
Requires:	python-metakit python-imaging python-sqlite2 python-imaging
Requires:	python-reportlab
BuildArch:	noarch
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
Gourmet allows you to collect, search and organize your recipes, and to
automatically generate shopping lists from your collection.

%prep
%setup -q
chmod -x data/recipe.dtd

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %buildroot --disable-modules-check

%find_lang %name

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-category="Other" \
  --remove-key="Icon" \
  --add-category="GTK" \
  --add-category="Database;Office" \
  --add-category="X-MandrivaLinux-MoreApplications-Databases" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*


#icons
mkdir -p %{buildroot}/%_liconsdir
convert -size 48x48 images/recbox.png %{buildroot}/%_liconsdir/%name.png
mkdir -p %{buildroot}/%_iconsdir
convert -size 32x32 images/recbox.png %{buildroot}/%_iconsdir/%name.png
mkdir -p %{buildroot}/%_miconsdir
convert -size 16x16 images/recbox.png %{buildroot}/%_miconsdir/%name.png

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%files -f %name.lang
%defattr(-,root,root)
%doc CHANGES MANIFEST PKG-INFO README TODO
%{_bindir}/%name
%{py_puresitedir}/%{name}*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png

