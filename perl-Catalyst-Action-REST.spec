%define upstream_name    Catalyst-Action-REST
%define upstream_version 0.90

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A request trait for REST and browsers
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Catalyst::Runtime)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(Config::General)
BuildRequires: perl(Data::Serializer)
BuildRequires: perl(Data::Taxi)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(FreezeThaw)
BuildRequires: perl(JSON)
BuildRequires: perl(LWP::UserAgent)
BuildRequires: perl(MRO::Compat)
BuildRequires: perl(Module::Pluggable::Object)
BuildRequires: perl(Moose)
BuildRequires: perl(PHP::Serialization)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI::Find)
BuildRequires: perl(XML::Simple)
BuildRequires: perl(YAML::Syck)
BuildRequires: perl(namespace::autoclean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This Action handles doing automatic method dispatching for REST requests.
It takes a normal Catalyst action, and changes the dispatch to append an
underscore and method name. First it will try dispatching to an action with
the generated name, and failing that it will try to dispatch to a regular
method.

For example, in the synopsis above, calling GET on "/foo" would result in
the foo_GET method being dispatched.

If a method is requested that is not implemented, this action will return a
status 405 (Method Not Found). It will populate the "Allow" header with the
list of implemented request methods. You can override this behavior by
implementing a custom 405 handler like so:

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


