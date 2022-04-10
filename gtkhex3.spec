Summary:	GNOME binary editor library based on GTK+ 3
Summary(pl.UTF-8):	Biblioteka edytora binarnego dla GNOME oparta na GTK+ 3
Name:		gtkhex3
Version:	3.41.1
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/ghex/3.41/ghex-%{version}.tar.xz
# Source0-md5:	8d2c32a81893637d32cacd8e5c1bee6d
URL:		https://wiki.gnome.org/Apps/Ghex
BuildRequires:	atk-devel >= 1:1.22.0
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.4.0
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires:	atk >= 1:1.22.0
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.4.0
Obsoletes:	ghex-libs < 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GHex allows the user to load data from any file, view and edit it in
either hex or ascii. A must for anyone playing games that use
non-ascii format for saving.

%description -l pl.UTF-8
GHex pozwala użytkownikowi na wczytanie danych z dowolnego pliku,
przeglądanie i edycję ich w trybie szesnastkowym i ASCII. Obowiązkowe
narzędzie dla wszystkich graczy, których gry zapisują stan w formacie
innym niż tekstowy.

%package devel
Summary:	GtkHex 3 development files
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GtkHex 3
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk+3-devel >= 3.4.0
Obsoletes:	ghex-devel < 4

%description devel
GtkHex 3 development files.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GtkHex 3.

%package static
Summary:	GtkHex 3 static library
Summary(pl.UTF-8):	Biblioteka statyczna GtkHex 3
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	ghex-static < 4

%description static
GtkHex 3 static library.

%description static -l pl.UTF-8
Biblioteka statyczna GtkHex 3.

%prep
%setup -q -n ghex-%{version}

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# package just library (for nemiver etc.)
%{__rm} $RPM_BUILD_ROOT%{_bindir}/ghex
%{__rm} $RPM_BUILD_ROOT%{_desktopdir}/org.gnome.GHex.desktop
%{__rm} $RPM_BUILD_ROOT%{_datadir}/glib-2.0/schemas/org.gnome.GHex.gschema.xml
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/*/ghex
%{__rm} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/*/apps/org.gnome.GHex*.svg
%{__rm} $RPM_BUILD_ROOT%{_localedir}/*/LC_MESSAGES/ghex.mo
%{__rm} $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.GHex.appdata.xml

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) %{_libdir}/libgtkhex-3.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtkhex-3.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhex-3.so
%{_includedir}/gtkhex-3
%{_pkgconfigdir}/gtkhex-3.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgtkhex-3.a
