Summary:	Geheimnis: KDE program for using GnuPG, PGP2, and PGP5 in a graphical manner
Summary(pl):	Graficzny interfejs pod KDE do programów GnuPG, PGP2 i PGP5
Name:		geheimnis
Version:	1.98
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Chris Wiegand <cwiegand@urgentmail.com>
Source0:	http://dl.sourceforge.net/geheimnis/%{name}-%{version}.tar.gz
# Source0-md5:	f22452568cad98de77689311f3fa251e
Patch0:		%{name}-build.patch
URL:		http://geheimnis.sourceforge.net/
# stupid ac macros check for artsc-config
BuildRequires:	artsc-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geheimnis is a KDE program for using GnuPG, PGP2, and PGP5 in a
graphical manner reminiscent of Win31's PGP shells.

%description -l pl
Geheminis jest programem KDE umo¿liwiaj±cym u¿ywanie GNUPG, PGP2 i
PGP5 poprzez interfejs graficzny, podobnie jak w pow³okach PGP Windows
3.1x.

%prep
%setup -q -n %{name}
%patch -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure2_13 \
	--enable-mt \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/geheimnis
%{_pixmapsdir}/*/*/apps/*
%{_applnkdir}/Utilities/geheimnis*.desktop
