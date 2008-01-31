%include	/usr/lib/rpm/macros.php
%define		_class		MP3
%define		_subclass	Playlist
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create MP3 playlists on the fly
Summary(pl.UTF-8):	%{_pearname} - tworzenie list utworów MP3 w locie
Name:		php-pear-%{_pearname}
Version:	0.5.1
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}alpha1.tgz
# Source0-md5:	5eab4294f35c79b4d1046d1d13d9ddfc
URL:		http://pear.php.net/package/MP3_Playlist/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:5.0.0
Requires:	php-pear
Requires:	php-pear-MP3_Id >= 1.1.4
Requires:	php-pear-Net_URL >= 1.0.14
Requires:	php-pear-PEAR-core >= 1:1.3.0
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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
