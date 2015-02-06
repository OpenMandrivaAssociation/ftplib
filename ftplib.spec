%define major 4
%define libname %mklibname ftp %{major}
%define devname %mklibname ftp -d

Summary:	FTP Library Routines
Name:		ftplib
Version:	4.0
Release:	2
License:	Artistic
Group:		System/Libraries
Url:		http://nbpfaus.net/~pfau/ftplib/
Source0:	http://www.nbpfaus.net/~pfau/ftplib/%{name}-%{version}.tar.gz

%description
This package implements a callable interface to FTP. The FTP
protocol is specified in RFC 959.

#----------------------------------------------------------------------------

%package -n qftp
Summary:	Command line driven ftp file transfer program
Group:		Networking/File transfer

%description -n qftp
qftp performs directories or file transfers using the ftp protocol
based on the command it was invoked with and command line arguments.

%files -n qftp
%doc README.qftp
%{_bindir}/ftp*
%{_bindir}/qftp

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library of ftplib
Group:		System/Libraries

%description -n %{libname}
This package implements a callable interface to FTP. The FTP
protocol is specified in RFC 959.

This package contains the library needed to run programs dynamically
linked with ftplib.

%files -n %{libname}
%doc CHANGES README.ftplib-%{version} LICENSE
%{_libdir}/libftp.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Headers and static library for ftplib development
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	libftp-devel = %{EVRD}
Provides:	ftp-devel = %{EVRD}

%description -n %{devname}
This package implements a callable interface to FTP. The FTP
protocol is specified in RFC 959.

This package contains the headers and static library that
programmers will need to develop applications which will use
ftplib.

%files -n %{devname}
%doc CHANGES README.ftplib-%{version} LICENSE
%{_libdir}/*.so
%{_includedir}/%{name}.h

#----------------------------------------------------------------------------

%prep
%setup -q
sed -i 's,/usr/local/bin,$(DESTDIR)%{_bindir},' src/Makefile
sed -i 's,/usr/local/lib,$(DESTDIR)%{_libdir},' src/Makefile
sed -i 's,/usr/local/include,$(DESTDIR)%{_includedir},' src/Makefile

%build
cd src
%make DEBUG="%{optflags}"

%install
cd src
install -d -m755 %{buildroot}%{_bindir}
install -d -m755 %{buildroot}%{_libdir}
install -d -m755 %{buildroot}%{_includedir}
%makeinstall_std

# unstripped-binary-or-object
chmod 0755 %{buildroot}%{_libdir}/libftp.so.%{major}*

