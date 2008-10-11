%define with_qt3 0
%{?_with_qt3: %{expand: %%global with_qt3 1}}

Name: qscintilla
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
Version: 2.3
Release: %mkrel 1
License: GPLv2+
Group: System/Libraries
Source0: http://www.riverbankcomputing.co.uk/static/Downloads/QScintilla2/QScintilla-gpl-%version.tar.gz
Patch0: QScintilla-gpl-2.2-libdir.patch
URL: http://www.riverbankcomputing.co.uk/qscintilla
%if %{with_qt3}
BuildRequires: qt3-devel
BuildRequires: python-qt >= 1:3.16.0
%endif # with_qt3
BuildRequires: qt4-devel >= 2:4.3.1
BuildRequires: python-sip >= 1:4.7
BuildRequires: python-qt4-devel
%py_requires -d
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

%if %{with_qt3}

%define libqs3 %mklibname qscintilla-qt3_ 2

%package -n %libqs3
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
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

%if %mdkversion < 200900
%post -n %libqs3 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libqs3 -p /sbin/ldconfig
%endif

%files -n %libqs3
%defattr(644,root,root,755)
%attr(755,root,root) %{qt3lib}/*.so.*
%{qt3dir}/translations/qscintilla*.qm

#--------------------------------------------------------------

%define libqs3dev %mklibname -d qscintilla-qt3

%package -n %libqs3dev
Summary: Libraries, include and other files to develop applications with QScintilla for Qt3
Group: Development/KDE and Qt
Requires: %libqs3 = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Provides: %{name}-qt3-devel = %{version}-%{release}
Provides: qscintilla-qt3-devel = %{version}-%{release}
Obsoletes: %{_lib}qscintilla-qt3_-devel

%description -n %libqs3dev
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %libqs3dev
%defattr(644,root,root,755)
%{qt3dir}/include/*
%{qt3lib}/*.so

#--------------------------------------------------------------

%package -n python-qt3-qscintilla
Summary: Python qt3 QScintilla bindings
Group: Development/KDE and Qt
Requires: python-qt
Requires: %libqs3

%description -n python-qt3-qscintilla
Python qt3 QScintilla bindings.

%files -n python-qt3-qscintilla
%defattr(644,root,root,755)
%_datadir/sip/qsci
%qt3dir/qsci
%py_platsitedir/qsci.so

%endif # with_qt3

#--------------------------------------------------------------

%define libqs4 %mklibname qscintilla-qt4_ 2

%package -n %libqs4
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
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

%if %mdkversion < 200900
%post -n %libqs4 -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libqs4 -p /sbin/ldconfig
%endif

%files -n %libqs4
%defattr(644,root,root,755)
%attr(755,root,root) %{qt4lib}/*.so.*
%{qt4dir}/translations/qscintilla*.qm

#--------------------------------------------------------------

%define libqs4dev %mklibname -d qscintilla-qt4

%package -n %libqs4dev
Summary: Libraries, include and other files to develop applications with QScintilla for Qt3
Group: Development/KDE and Qt
Requires: %libqs4 = %{version}-%{release}
Provides: %{name}-qt4-devel = %{version}-%{release}
Obsoletes: %{_lib}qscintilla-qt4_-devel
Provides: qscintilla-qt4-devel = %{version}-%{release}
Conflicts: %{_lib}qscintilla-qt3_2 <= 2.2-2

%description -n %libqs4dev
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %libqs4dev
%defattr(644,root,root,755)
%{qt4dir}/include/*
%{qt4lib}/*.so
%{qt4plugins}/designer/*

#--------------------------------------------------------------

%package -n python-qt4-qscintilla
Summary: Python qt4 QScintilla bindings
Group: Development/KDE and Qt
Requires: python-qt4-core
Requires: python-qt4-gui
Requires: %libqs4

%description -n python-qt4-qscintilla
Python qt4 QScintilla bindings.

%files -n python-qt4-qscintilla 
%defattr(644,root,root,755)
%_datadir/sip/PyQt4
%qt4dir/qsci
%py_platsitedir/PyQt4/Qsci.so

#--------------------------------------------------------------

%package doc
Summary: QScintilla docs
Group: Development/KDE and Qt

%description doc
QScintilla doc.

%files doc
%defattr(644,root,root,755)
%doc ChangeLog NEWS README doc	

#--------------------------------------------------------------

%prep 
%setup -qn QScintilla-gpl-%{version}
%patch0 -p1 -b .libbuild

%build
%if %{with_qt3}
pushd Qt3 
    export QTDIR=%qt3dir
    %qmake_qt3 DESTDIR=%buildroot/%{qt3lib} qscintilla.pro
    %make 
popd
%endif

pushd Qt4
    export QTDIR=%qt4dir
    %qmake_qt4 DESTDIR=%buildroot/%{qt4lib} qscintilla.pro
    %make 
popd

pushd designer-Qt4
    echo "INCLUDEPATH += ../Qt4" >> designer.pro
    echo "LIBS += -L%buildroot/%{qt4lib}" >> designer.pro
    %qmake_qt4 designer.pro
    make
popd


%install
rm -fr %{buildroot}
mkdir -p %buildroot/%qt4lib

%if %{with_qt3}
mkdir -p %buildroot/%qt3lib
pushd Qt3
    make INSTALL_ROOT=%buildroot install
popd

pushd Python
    export QTDIR=%qt3dir
    python configure.py -p 3 \
        -n ../Qt3 \
        -o %buildroot/%{qt3lib} 
    %make 
    make DESTDIR=%buildroot install
popd
%endif #with_qt3

pushd Qt4
    make INSTALL_ROOT=%buildroot install
popd

pushd designer-Qt4
    make INSTALL_ROOT=%buildroot install
popd

pushd Python
    export QTDIR=%qt4dir
    export PATH=%qt4dir/bin:$PATH
    python configure.py \
        -n ../Qt4 \
        -o %buildroot/%{qt4lib} 
    %make 
    make DESTDIR=%buildroot install
popd

%clean
rm -rf %{buildroot}


