%define oname 	QScintilla
%define version 1.7.1
%define release %mkrel 1

%define scintilla 1.71
%define qtdir /usr/lib/qt3

%define major 7
%define libname %mklibname %{name} %{major}
%define libnamedev %mklibname %name %major -d

Summary:	QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Name:		qscintilla
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		System/Libraries
Source:		%{oname}-%{scintilla}-gpl-%{version}.tar.bz2
URL:		http://www.riverbankcomputing.co.uk/qscintilla
BuildRequires:	qt3-devel >= 3.3.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%package -n %{libname}
Summary:	QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Group:		System/Libraries
Provides:	lib%{name} = %{version}
Requires:	%{name}-translations

%description -n %{libname}
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%package -n %{libnamedev}
Summary:	Libraries, include and other files to develop applications with QScintilla
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d 6

%description -n %{libnamedev}
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%package translations
Summary:	Language files for qscintilla
Group:		Development/KDE and Qt
Conflicts:	%mklibname qscintilla 5

%description translations
Language files for qscintilla.

%prep 
%setup -qn %{oname}-%{scintilla}-gpl-%{version}

%build
export QTDIR=%{qtdir}
cd qt
%{qtdir}/bin/qmake -o Makefile qscintilla.pro

# x86_64 bs fixes
sed -i '415d' Makefile
sed -i '424d' Makefile
#

%make first DESTDIR=%{buildroot}/%{qtdir}/%{_lib}

%install
rm -fr %{buildroot}

mkdir -p %{buildroot}/%{qtdir}/{include,translations,%{_lib}}
cp qt/qextscintilla*.h %{buildroot}/%{qtdir}/include/
cp qt/qscintilla*.qm %{buildroot}/%{qtdir}/translations/
cp -d qt/*.so* %{buildroot}/%{qtdir}/%{_lib}/

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libnamedev}
%defattr(644,root,root,755)
%{qtdir}/include/*
%{qtdir}/%{_lib}/libqscintilla.so

%files -n %{libname}
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NEWS README doc	
%attr(755,root,root) %{qtdir}/%{_lib}/libqscintilla.so.%{major}*

%files translations
%defattr(644,root,root,755)
%{qtdir}/translations/qscintilla*.qm
