Summary:	Geheimnis: KDE program for using GnuPG, PGP2, and PGP5 in a graphical manner
Summary(pl):	Graficzny interfejs pod KDE do programów GnuPG, PGP2 i PGP5
Name:		geheimnis
Version:	1.96
Release:	1
License:	GPL
Group:		X11/Applications
Vendor:		Chris Wiegand <cwiegand@urgentmail.com>
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/geheimnis/%{name}-%{version}.tar.gz
URL:		http://geheimnis.sourceforge.net/
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Geheimnis is a KDE program for using GnuPG, PGP2, and PGP5 in a
graphical manner reminiscent of Win31's PGP shells.

%description -l pl
Geheminis jest programem KDE umozliwiaj±cym u¿ycie GNUPG, PGP2 i PGP5
poprzez interfejs graficzny, podobnie jak w pow³okach PGP Windows
3.1x.

%prep
%setup -q -n %{name}

%build
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Utilities}

gzip -9nf AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/geheimnis
%{_pixmapsdir}/*/*/apps/*
%{_applnkdir}/Utilities/geheimnis.desktop
