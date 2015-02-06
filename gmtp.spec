Summary:	Simple MTP Client
Name:		gmtp
Version:	1.3.7
Release:	2
License:	BSD
Group:		Sound
Url:		http://gmtp.sourceforge.net/
Source0:	http://download.sourceforge.net/gmtp/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(libmtp)
BuildRequires:	pkgconfig(vorbisfile)

%description
Supports MTP devices including those with multiple storage devices (typically
mobile phones). Supports Drag'n'Drop interface for upload/download of files.

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gmtp.gschema.xml
%{_datadir}/pixmaps/gmtpicon.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

