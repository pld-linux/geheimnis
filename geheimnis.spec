%define name geheimnis
%define	version 0.60
%define release 1
%define prefix /opt/kde

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Geheimnis: KDE program for using GnuPG, PGP2, and PGP5 in a graphical manner.
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Group: X11/KDE/Utilities
Copyright: GPL
Vendor: Chris Wiegand <cwiegand@urgentmail.com>
Packager: Troy Engel <tengel@sonic.net>
Distribution: KDE
Source: %{name}-%{version}.tar.gz
URL: http://members.home.com/cdwiegand/geheimnis
Requires: qt kdelibs
BuildRoot: /tmp/build-%{name}-%{version}
Patch: %{name}-%{version}.patch

%description
Geheimnis is a KDE program for using GnuPG, PGP2, and PGP5 in a
graphical manner reminiscent of Win31's PGP shells. It is built
and tested under KDE 1.0 (actually, revision 0.99 it appears).

%prep
rm -rf %{builddir}

%setup
%patch -p1
touch `find . -type f`

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
rm -rf %{builddir}
rm -f $RPM_BUILD_DIR/file.list.%{name}

%files -f ../file.list.%{name}
