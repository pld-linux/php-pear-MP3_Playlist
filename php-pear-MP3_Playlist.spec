%include	/usr/lib/rpm/macros.php
%define		_class		MP3
%define		_subclass	Playlist
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - create MP3 playlists on the fly
Summary(pl):	%{_pearname} - tworzenie list utworów MP3 w locie
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}alpha1.tgz
# Source0-md5:	1a577763fb278b411ae73b6e5a140271
URL:		http://pear.php.net/package/MP3_Playlist/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MP3_Playlist is a PHP library to facilitate the creation and to some
extend the rendering of MP3 playlists. It scans a local folder with
all the MP3 files and outputs the playlist in several formats
including M3U, SMIL, XML, XHTML with the possibility to backup the
lists on the fly with an SQLite DB.

In PEAR status of this package is: %{_status}.

%description -l pl
MP3_Playlist jest bibliotek± PHP u³atwiaj±c± tworzenie i rozszerzanie
list utworów MP3. Skanuje lokalne foldery w poszukiwaniu plików MP3 
i zwraca listy utworów w ró¿nych formatach, w³±czaj±c w to M3U, SMIL,
XML, XHTML z mo¿liwo¶ci± tworzenia kopii list w bazie SQLite.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}alpha1/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}alpha1/%{_class}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}alpha1/docs/*
%{php_pear_dir}/%{_class}/*
