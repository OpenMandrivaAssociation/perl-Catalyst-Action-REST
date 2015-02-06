%define upstream_name    Catalyst-Action-REST
%define upstream_version 0.90

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A request trait for REST and browsers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Class::Inspector)
BuildRequires:	perl(Config::General)
BuildRequires:	perl(Data::Serializer)
BuildRequires:	perl(Data::Taxi)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FreezeThaw)
BuildRequires:	perl(JSON)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(MRO::Compat)
BuildRequires:	perl(Module::Pluggable::Object)
BuildRequires:	perl(Moose)
BuildRequires:	perl(PHP::Serialization)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI::Find)
BuildRequires:	perl(XML::Simple)
BuildRequires:	perl(YAML::Syck)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.900.0-2mdv2011.0
+ Revision: 657392
- rebuild for updated spec-helper

* Wed Mar 02 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.900.0-1
+ Revision: 641318
- update to new version 0.90

* Sun Jan 30 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.890.0-1
+ Revision: 634207
- update to new version 0.89

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.870.0-1mdv2011.0
+ Revision: 595079
- update to new version 0.87

* Sat Sep 04 2010 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2011.0
+ Revision: 575736
- update to 0.86

* Tue Jul 27 2010 Shlomi Fish <shlomif@mandriva.org> 0.850.0-1mdv2011.0
+ Revision: 561126
- import perl-Catalyst-Action-REST


* Thu Jul 15 2010 cpan2dist 0.85-1mdv
- initial mdv release, generated with cpan2dist
