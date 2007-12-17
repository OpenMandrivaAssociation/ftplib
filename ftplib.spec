
%define name	ftplib
%define version	3.1
%define rel	1

%define major	3
%define libname	%mklibname ftp %major

Summary:	FTP Library Routines
Name:		%name
Version:	%version
Release:	%mkrel %rel
License:	LGPL
URL:		http://nbpfaus.net/~pfau/ftplib/
Source:		http://www.nbpfaus.net/~pfau/ftplib/%name-%version-src.tar.bz2
Patch0:		http://nbpfaus.net/~pfau/ftplib/ftplib-3.1-1.patch
Group:		System/Libraries

%description
This package implements a callable interface to FTP.  The FTP
protocol is specified in RFC 959.

%package -n qftp
Summary:	Command line driven ftp file transfer program
Group:		Networking/File transfer

%description -n qftp
qftp performs directories or file transfers using the ftp protocol
based on the command it was invoked with and command line arguments.

%package -n %libname
Summary:	Shared library of ftplib
Group:		System/Libraries
Provides:	%name = %version-%release

%description -n %libname
This package implements a callable interface to FTP.  The FTP
protocol is specified in RFC 959.

This package contains the library needed to run programs dynamically
linked with ftplib.

%package -n %libname-devel
Summary:	Headers and static library for ftplib development
Group:		Development/C
Requires:	%libname = %version
Provides:	libftp-devel = %version-%release
Provides:	ftp-devel = %version-%release

%description -n %libname-devel
This package implements a callable interface to FTP.  The FTP
protocol is specified in RFC 959.

This package contains the headers and static library that
programmers will need to develop applications which will use
ftplib.

%prep
%setup -q
%patch0 -p3
sed -i 's,/usr/local/bin,$(DESTDIR)%{_bindir},' linux/Makefile
sed -i 's,/usr/local/lib,$(DESTDIR)%{_libdir},' linux/Makefile
sed -i 's,/usr/local/include,$(DESTDIR)%{_includedir},' linux/Makefile

%build
cd linux
%make DEBUG="%optflags"

%install
rm -rf %{buildroot}
cd linux
install -d -m755 %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_libdir}
install -d -m755 %{buildroot}%{_includedir}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root)
%doc NOTES
%{_libdir}/*.so.%{major}*

%files -n %libname-devel
%defattr(-,root,root)
%doc CHANGES README.ftplib_v3.1 TODO NOTES
%{_libdir}/*.so
%{_includedir}/%{name}.h

%files -n qftp
%defattr(-,root,root)
%doc README.qftp
%{_bindir}/ftp*
%{_bindir}/qftp


