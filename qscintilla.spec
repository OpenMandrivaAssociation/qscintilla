%define scintilla 1.73

Name: qscintilla
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Version: 2.1
Release: %mkrel 1
License: GPL
Group: System/Libraries
Source:	QScintilla-%{scintilla}-gpl-%{version}.tar.gz
URL: http://www.riverbankcomputing.co.uk/qscintilla
BuildRequires: qt3-devel
BuildRequires: qt4-devel >= 2:4.3.1
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

#--------------------------------------------------------------

%define libqs3 %mklibname qscintilla-qt3_ 2

%package -n %libqs3
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Group: System/Libraries
Obsoletes: qscintilla-translations

%description -n %libqs3
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%post -n %libqs3 -p /sbin/ldconfig
%postun -n %libqs3 -p /sbin/ldconfig

%files -n %libqs3
%defattr(644,root,root,755)
%attr(755,root,root) %{qt3lib}/*.so.*
%{qt3dir}/translations/qscintilla*.qm
%exclude %{qt3dir}/qsci/api/python

#--------------------------------------------------------------

%define libqs3dev %mklibname -d qscintilla-qt3_ 

%package -n %libqs3dev
Summary: Libraries, include and other files to develop applications with QScintilla for Qt3
Group: Development/KDE and Qt
Requires: %libqs3 = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-qt3-devel = %{version}-%{release}

%description -n %libqs3dev
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %libqs3dev
%defattr(644,root,root,755)
%{qt3dir}/include/*
%{qt3lib}/*.so

#--------------------------------------------------------------

%define libqs4 %mklibname qscintilla-qt4_ 2

%package -n %libqs4
Summary: QScintilla is a port to Qt of Neil Hodgson's Scintilla C++ editor class
Group: System/Libraries
Obsoletes: qscintilla-translations

%description -n %libqs4
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%post -n %libqs4 -p /sbin/ldconfig
%postun -n %libqs4 -p /sbin/ldconfig

%files -n %libqs4
%defattr(644,root,root,755)
%attr(755,root,root) %{qt4lib}/*.so.*
%{qt4dir}/translations/qscintilla*.qm
%exclude %{qt4dir}/qsci/api/python

#--------------------------------------------------------------

%define libqs4dev %mklibname -d qscintilla-qt4_ 

%package -n %libqs4dev
Summary: Libraries, include and other files to develop applications with QScintilla for Qt3
Group: Development/KDE and Qt
Requires: %libqs4 = %{version}-%{release}
Provides: %{name}-qt4-devel = %{version}-%{release}

%description -n %libqs4dev
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %libqs4dev
%defattr(644,root,root,755)
%{qt4dir}/include/*
%{qt4lib}/*.so

#--------------------------------------------------------------

%package doc
Summary: QScintilla docs
Group: Development/KDE and Qt

%description doc
QScintilla doc.

%files doc
%defattr(644,root,root,755)
%doc ChangeLog LICENSE NEWS README doc	

%prep 
%setup -qn QScintilla-%{scintilla}-gpl-%{version}

%build
# We will build both qt3 and qt4 qscintilla !
export QTDIR=%qt3dir
pushd Qt3
    qmake -o Makefile qscintilla.pro
    %make 
popd

pushd Qt4
    export QTDIR=%qt4dir
    export PATH=%qt4dir/bin:$PATH
    qmake -o Makefile qscintilla.pro
    %make
popd

%install
rm -fr %{buildroot}
mkdir -p %buildroot/{%qt3lib,%qt4lib}
pushd Qt3
    cp -d *.so* %buildroot/%qt3lib
    make INSTALL_ROOT=%buildroot install
popd
pushd Qt4
    cp -d *.so* %buildroot/%qt4lib
    make INSTALL_ROOT=%buildroot install
popd

%clean
rm -rf %{buildroot}


