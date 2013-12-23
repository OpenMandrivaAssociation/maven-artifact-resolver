%_javapackages_macros
Name:           maven-artifact-resolver
Version:        1.0
Release:        9.0%{?dist}
# Epoch is added because the original package's version in maven-shared is 1.1-SNAPSHOT
Epoch:          1
Summary:        Maven Artifact Resolution API
License:        ASL 2.0
URL:            http://maven.apache.org/shared/%{name}
Source0:        http://central.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Replaced plexus-maven-plugin with plexus-component-metadata
Patch0:         %{name}-plexus.patch

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.easymock:easymock)

Obsoletes:      maven-shared-artifact-resolver < %{epoch}:%{version}-%{release}
Provides:       maven-shared-artifact-resolver = %{epoch}:%{version}-%{release}

%description
Provides a component for plugins to easily resolve project dependencies.


%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%setup -q
%patch0 -p1

%pom_xpath_inject pom:project/pom:dependencies "
<dependency>
  <groupId>org.apache.maven</groupId>
  <artifactId>maven-compat</artifactId>
  <version>1.0</version>
</dependency>" pom.xml

# Incompatible method invocation
rm src/test/java/org/apache/maven/shared/artifact/resolver/DefaultProjectDependenciesResolverIT.java

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc DEPENDENCIES LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Mon Aug 05 2013 Michal Srb <msrb@redhat.com> - 1:1.0-9
- Adapt to current guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Feb 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.0-7
- Add maven-shared to BR/R
- Add few other missing BRs

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.0-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Sep 14 2012 Tomas Radej <tradej@redhat.com> - 1:1.0-4
- Installing folders separately with -m 755
- Installing NOTICE in javadoc subpackage
- Fixed changelog

* Wed Sep 12 2012 Tomas Radej <tradej@redhat.com> - 1:1.0-3
- Really fixed Provides/Obsoletes by introducing epoch

* Thu Sep 06 2012 Tomas Radej <tradej@redhat.com> - 1.0-2
- Fixed Provides/Obsoletes

* Tue Jul 31 2012 Tomas Radej <tradej@redhat.com> - 1.0-1
- Initial version
