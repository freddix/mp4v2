Summary:	MP4v2 library provides API for creation and modification of MP4 files
Name:		mp4v2
Version:	2.0.0
Release:	2
License:	MPL v1.1
Group:		Applications/Multimedia
Source0:	http://mp4v2.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	c91f06711225b34b4c192c9114887b14
URL:		http://code.google.com/p/mp4v2/
BuildRequires:	libstdc++-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MP4v2 library provides an API to create and modify MP4 files as
defined by ISO-IEC:14496-1:2001 MPEG-4 Systems. This file format is
derived from Apple's QuickTime file format that has been used as a
multimedia file format in a variety of platforms and applications. It
is a very powerful and extensible format that can accomodate
practically any type of media.

%package libs
Summary:	Header files for MP4v2
Group:		Libraries

%description libs
The libmp4v2 library provides an abstraction layer for working with
files using the mp4 container format.

%package devel
Summary:	Header files for MP4v2
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for MP4v2.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /usr/sbin/ldconfig
%postun libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/*.txt
%attr(755,root,root) %{_bindir}/mp4track
%attr(755,root,root) %{_bindir}/mp4extract
%attr(755,root,root) %{_bindir}/mp4trackdump
%attr(755,root,root) %{_bindir}/mp4art
%attr(755,root,root) %{_bindir}/mp4tags
%attr(755,root,root) %{_bindir}/mp4subtitle
%attr(755,root,root) %{_bindir}/mp4chaps
%attr(755,root,root) %{_bindir}/mp4info
%attr(755,root,root) %{_bindir}/mp4file
%{_mandir}/man1/mp4art.1*
%{_mandir}/man1/mp4file.1*
%{_mandir}/man1/mp4subtitle.1*
%{_mandir}/man1/mp4track.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libmp4v2.so.2
%attr(755,root,root) %{_libdir}/libmp4v2.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmp4v2.so
%{_includedir}/mp4v2

