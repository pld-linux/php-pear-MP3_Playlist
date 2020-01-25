%define		_status		alpha
%define		_pearname	MP3_Playlist
Summary:	%{_pearname} - create MP3 playlists on the fly
Summary(pl.UTF-8):	%{_pearname} - tworzenie list utworów MP3 w locie
Name:		php-pear-%{_pearname}
Version:	0.5.2
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	601821984dd7c40cd130c6c64f84363e
URL:		http://pear.php.net/package/MP3_Playlist/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 5.0.0
Requires:	php-pear
Requires:	php-pear-MP3_Id >= 1.1.4
Requires:	php-pear-Net_URL >= 1.0.14
Requires:	php-pear-PEAR-core >= 1:1.3.0
Obsoletes:	php-pear-MP3_Playlist-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MP3_Playlist is a PHP library to facilitate the creation and to some
extend the rendering of MP3 playlists. It scans a local folder with
all the MP3 files and outputs the playlist in several formats
including M3U, SMIL, XML, XHTML with the possibility to backup the
lists on the fly with an SQLite DB.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
MP3_Playlist jest biblioteką PHP ułatwiającą tworzenie i rozszerzanie
list utworów MP3. Skanuje lokalne foldery w poszukiwaniu plików MP3 i
zwraca listy utworów w różnych formatach, włączając w to M3U, SMIL,
XML, XHTML z możliwością tworzenia kopii list w bazie SQLite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

# package build script
rm .%{php_pear_dir}/generate_package_xml.php

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/MP3/Playlist.php
%{php_pear_dir}/MP3/Playlist

%{_examplesdir}/%{name}-%{version}
