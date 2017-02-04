Summary:	Open source version of Google Authenticator
Name:		google-authenticator
Version:	1.02
Release:	0
License:	ASL 2.0
Group:		Networking/Other
URL:		https://github.com/google/%{name}
Source0:	https://github.com/google/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(libqrencode)

%description
The Google Authenticator package contains a pluggable authentication
module (PAM) which allows login using one-time passcodes conforming to
the open standards developed by the Initiative for Open Authentication
(OATH) (which is unrelated to OAuth).

Passcode generators are available (separately) for several mobile
platforms.

These implementations support the HMAC-Based One-time Password (HOTP)
algorithm specified in RFC 4226 and the Time-based One-time Password
(TOTP) algorithm specified in RFC 6238.

%files
%{_bindir}/%{name}
%{_libdir}/security/pam_google_authenticator.so
%doc libpam/totp.html
%doc libpam/FILEFORMAT
%doc libpam/README.md

#----------------------------------------------------------------------------

%prep
%setup -q

%build
pushd libpam
autoreconf -fiv
%configure
%make
popd

%install
%makeinstall_std -C libpam

%check
%make -C libpam test

