Name:		airsonic
Version:	10.5.0
Release:	1%{?dist}
Summary:    web-based media streamer

Group:		WEB
License:	GPLv3+
URL:		https://github.com/airsonic/airsonic
Source0:	https://github.com/airsonic/airsonic/releases/download/v10.5.0/airsonic.war
Source1:    https://github.com/airsonic/airsonic/blob/master/contrib/airsonic.service
Source2:    https://github.com/airsonic/airsonic/blob/master/LICENSE.txt

BuildRequires:	java-1.8.0-openjdk-headless
Requires:	    java-1.8.0-openjdk-headless
Requires(pre):  /usr/sbin/useradd

%description
Airsonic is a free, web-based media streamer, providing ubiquitous access to your music

%prep
#wget https://github.com/airsonic/airsonic/releases/download/v%{version}/airsonic.war -O %{SOURCE0}
#wget https://github.com/airsonic/airsonic/raw/main/contrib/airsonic.service -O %{SOURCE1}
#wget https://github.com/airsonic/airsonic/raw/main/LICENSE.txt -O %{SOURCE2}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/%{name}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_localstatedir}/%{name}/%{name}.war
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/%{name}.service
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}
install -p -m 644 $RPM_%{SOURCE2} $RPM_BUILD_ROOT/%{_docdir}/%{name}-%{version}/LICENSE.txt

%pre
getent passwd airsonic >/dev/null || adduser --system --user-group -M --shell=/bin/bash --home=/var/airsonic airsonic

%post
systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun

%files
%defattr(-,%{name},%{name})
%{_unitdir}/%{name}.service
%{_localstatedir}/%{name}
%{_docdir}/%{name}-%{version}/*

%changelog
* Tue Nov 19 2019 CasjaysDev <rpm-devel@casjaysdev.com> - 10.5.0
- Initial RHEL Package
