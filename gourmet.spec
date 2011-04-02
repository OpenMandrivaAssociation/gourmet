Name: 	 	gourmet
Summary: 	Recipe manager for the GNOME desktop
Version: 	0.15.9
Release: 	%mkrel 1
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
