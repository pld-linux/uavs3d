Summary:	AVS3 decoder library
Summary(pl.UTF-8):	Biblioteka dekodera AVS3
Name:		uavs3d
Version:	1.1
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/uavs3/uavs3d/releases
Source0:	https://github.com/uavs3/uavs3d/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	a22d9d4f1da4d1e2d0b19a25754505c3
Patch0:		%{name}-x86.patch
URL:		https://github.com/uavs3/uavs3d
BuildRequires:	cmake >= 2.8
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
uavs3d is an opensource and cross-platform AVS3 decoder, supports
AVS3-P2 baseline profile.

%description -l pl.UTF-8
uavs3d to mający otwarte źródła, wieloplatformowy dekoder AVS3,
obsługujący profil AVS3-P2.

%package devel
Summary:	Header files for uavs3d library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki uavs3d
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for uavs3d library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki uavs3d.

%prep
%setup -q
%patch -P0 -p1

%{__sed} -i -e '/libdir/ s/"lib"/"%{_lib}"/' source/CMakeLists.txt

%build
install -d builddir
cd builddir
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C builddir install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md 
%attr(755,root,root) %{_libdir}/libuavs3d.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/uavs3d.h
%{_pkgconfigdir}/uavs3d.pc
