%bcond_without qt4
%bcond_without qt5
%bcond_without pyqt5
%define debug_package %{nil}
%define _disable_ld_no_undefined 1

Name: qscintilla
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
Version: 2.9.1
Release: 1
License: GPLv2+
Group: System/Libraries
Source0: http://sourceforge.net/projects/pyqt/files/QScintilla2/QScintilla-%{version}/QScintilla-gpl-%{version}.tar.gz
URL: http://www.riverbankcomputing.co.uk/software/qscintilla/intro
%if %{with qt4}
BuildRequires: qt4-devel >= 2:4.3.1
BuildRequires: python-qt4-devel
%endif # with qt4
%if %{with qt5}
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets) pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5PrintSupport) qt5-macros qmake5
%define qt5dir %{_prefix}/lib/qt5
%define qt5lib %{qt5dir}/%{_lib}
%define qt5plugins %{_libdir}/qt5/plugins
%endif
BuildRequires: python-sip >= 1:4.7.10
BuildRequires: 	pkgconfig(python3)
BuildRequires:	pkgconfig(python)
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

%if %{with qt4}
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

%files -n %libqs4
%defattr(644,root,root,755)
%attr(755,root,root) %{qt4lib}/*.so.*
%{qt4dir}/translations/qscintilla*.qm

#--------------------------------------------------------------

%define libqs4dev %mklibname -d qscintilla-qt4

%package -n %libqs4dev
Summary: Libraries, include and other files to develop with QScintilla for Qt4
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
%{qt4dir}/mkspecs/features/qscintilla2.prf
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
%_datadir/python-sip/PyQt4
%qt4dir/qsci
%py_platsitedir/PyQt4/Qsci.so
%endif

#--------------------------------------------------------------

%if %{with qt5}
%define libqs5 %mklibname qscintilla-qt5_ 2

%package -n %libqs5
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
Group: System/Libraries
Obsoletes: qscintilla-translations

%description -n %libqs5
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%files -n %libqs5
%defattr(655,root,root,755)
%attr(755,root,root) %{qt5lib}/*.so.*
%{_datadir}/qt5/translations/qscintilla*.qm

#--------------------------------------------------------------

%define libqs5dev %mklibname -d qscintilla-qt5

%package -n %libqs5dev
Summary: Libraries, include and other files to develop with QScintilla for Qt5
Group: Development/KDE and Qt
Requires: %libqs5 = %{version}-%{release}
Provides: %{name}-qt5-devel = %{version}-%{release}
Obsoletes: %{_lib}qscintilla-qt5_-devel
Provides: qscintilla-qt5-devel = %{version}-%{release}
Conflicts: %{_lib}qscintilla-qt3_2 <= 2.2-2

%description -n %libqs5dev
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %libqs5dev
%defattr(655,root,root,755)
%{_includedir}/qt5/Qsci
%{qt5lib}/*.so
%{qt5plugins}/designer/*
%{_datadir}/qt5/mkspecs/features/qscintilla2.prf

#--------------------------------------------------------------

%if %{with pyqt5}
%package -n python-qt5-qscintilla
Summary: Python qt5 QScintilla bindings
Group: Development/KDE and Qt
Requires: python-qt5-core
Requires: python-qt5-gui
Requires: %libqs5

%description -n python-qt5-qscintilla
Python qt5 QScintilla bindings.

%files -n python-qt5-qscintilla 
%defattr(655,root,root,755)
%_datadir/python-sip/PyQt5
%qt5dir/qsci
%py_platsitedir/PyQt5/Qsci.so
%endif
%endif

#--------------------------------------------------------------

%package doc
Summary: QScintilla docs
Group: Development/KDE and Qt

%description doc
QScintilla doc.

%files doc
%defattr(644,root,root,755)
%doc NEWS README doc	

#--------------------------------------------------------------

%prep 
%setup -qn QScintilla-gpl-%{version}
%apply_patches

%build

%if %{with qt4}
cp -a Qt4Qt5 Qt4
cp -a designer-Qt4Qt5 designer-Qt4

pushd Qt4
    export QTDIR=%qt4dir
    %qmake_qt4 DESTDIR=%buildroot/%{qt4lib} qscintilla.pro
    %make 
popd

pushd designer-Qt4
    echo "INCLUDEPATH += ../Qt4" >> designer.pro
    echo "LIBS += -L%buildroot/%{qt4lib}" >> designer.pro
    %qmake_qt4 designer.pro
    %make
popd
%endif

%if %{with qt5}
cp -a Qt4Qt5 Qt5
cp -a designer-Qt4Qt5 designer-Qt5

pushd Qt5
    export QTDIR=%qt5dir
    %qmake_qt5 DESTDIR=%buildroot/%{qt5lib} qscintilla.pro
    %make 
popd

pushd designer-Qt5
    echo "INCLUDEPATH += ../Qt5" >> designer.pro
    echo "LIBS += -L%buildroot/%{qt5lib}" >> designer.pro
    %qmake_qt5 designer.pro
    %make
popd
%endif

%install
%if %{with qt4}
mkdir -p %buildroot/%qt4lib
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
	--pyqt-sipdir=/usr/share/python-sip/PyQt4 \
        -o %buildroot/%{qt4lib} 
    sed -i -e 's,-lpthread,-lpthread -lpython2.7,g' Makefile
    %make 
    make INSTALL_ROOT=%buildroot install
popd
%endif

%if %{with qt5}
mkdir -p %buildroot/%qt5lib
pushd Qt5
    make INSTALL_ROOT=%buildroot install
popd

pushd designer-Qt5
    make INSTALL_ROOT=%buildroot install
popd

%if %{with pyqt5}
pushd Python
    export QTDIR=%qt5dir
    export PATH=%qt5dir/bin:$PATH
    python configure.py \
        -n ../Qt5 \
        -o %buildroot/%{qt5lib} 
    sed -i -e 's,-lpthread,-lpthread -lpython2.7,g' Makefile
    %make 
    make INSTALL_ROOT=%buildroot install
popd
%else
rm -rf %buildroot%{_datadir}/qt5/qsci
%endif
%endif
