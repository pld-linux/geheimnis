Summary:	Geheimnis: KDE program for using GnuPG, PGP2, and PGP5 in a graphical manner.
Name:		geheimnis
Version:	0.60
Release:	1
Copyright:	GPL
Group:		X11/KDE/Utilities
Vendor:		Chris Wiegand <cwiegand@urgentmail.com>
Source:		%{name}-%{version}.tar.gz
Patch:		%{name}-%{version}.patch
URL:		http://members.home.com/cdwiegand/geheimnis
BuildRequires:	qt-devel >= 1.42
BuildRequires:	kdesupport-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geheimnis is a KDE program for using GnuPG, PGP2, and PGP5 in a graphical
manner reminiscent of Win31's PGP shells. It is built and tested under KDE
1.0 (actually, revision 0.99 it appears).

%description -l pl
Geheminis jest programem KDE umozliwiaj±cym u¿ycie GNUPG, PGP2 i PGP5 poprzez
interfejs graficzny, podobnie jak w pow³okach PGP Windows 3.1x. Program
zosta³ zbudowany i przetestowany pod KDE 1.0 (a dok³adnie w wersji 0.99).

%prep
%setup -q
%patch -p1

%build
if [ -z "$KDEDIR" ]; then
	export KDEDIR=%{prefix}
fi
./configure --build-rpms
make CFLAGS="$RPM_OPT_FLAGS -I. -Wall"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

cd $RPM_BUILD_ROOT
find . -type d | sed '1,2d;s,^\.,\%attr(-\,root\,root) \%dir ,' > $RPM_BUILD_DIR/file.list.%{name}
find . -type f | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}
find . -type l | sed 's,^\.,\%attr(-\,root\,root) ,' >> $RPM_BUILD_DIR/file.list.%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ../file.list.%{name}
