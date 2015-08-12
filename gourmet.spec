Name:		gourmet
Summary:	Recipe manager for the GNOME desktop
Version:	0.17.4
Release:	3
Source0:	https://github.com/thinkle/gourmet/archive/%{name}-%{version}.tar.gz
URL:		http://thinkle.github.io/gourmet/
License:	GPLv2+
Group:		Graphical desktop/GNOME
BuildRequires:	python-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-elib.intl
BuildRequires:	python2-pyrtf
BuildRequires:	python2-imaging
BuildRequires:	intltool
BuildRequires:	python-distutils-extra
Requires:	pygtk2.0-libglade
Requires:	python-elib.intl
Requires:	python2-imaging
Requires:	python2-pyrtf
Requires:	python2-sqlalchemy
Requires:	python-reportlab
Requires:	python-pypoppler
BuildArch:	noarch
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils

%description
Gourmet allows you to collect, search and organize your recipes, and to
automatically generate shopping lists from your collection.

%prep
%setup -q

#fix .desktop file
sed -i -e 's/Icon=recbox.png/Icon=gourmet/g' %{name}.desktop.in

%build
%{__python2} setup.py build

%install
rm -rf %{buildroot}
%{__python2} setup.py install -O1 --root %{buildroot}

#menu
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="GTK" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%files -f %{name}.lang
%doc ChangeLog README.md
%{_bindir}/%{name}
%{py2_puresitedir}/%{name}
%{py2_puresitedir}/%{name}-%{version}-py%{py2_ver}.egg-info
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_iconsdir}/hicolor/*/apps/gourmet.*
%{_datadir}/appdata/gourmet.appdata.xml
