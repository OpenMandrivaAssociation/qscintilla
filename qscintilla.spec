%global optflags %{optflags} -std=gnu++14
%bcond_with pyqt5
%define debug_package %{nil}
%define _disable_ld_no_undefined 1
%define _disable_lto 1

Name: qscintilla
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
Version: 2.11.1
Release: 1
License: GPLv2+
Group: System/Libraries
Source0: https://www.riverbankcomputing.com/static/Downloads/QScintilla/QScintilla_gpl-%{version}.tar.gz
URL: http://www.riverbankcomputing.co.uk/software/qscintilla/intro
BuildRequires: pkgconfig(Qt5Gui) pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5PrintSupport) qt5-macros qmake5
%define qt5dir %{_prefix}/lib/qt5
%define qt5plugins %{_libdir}/qt5/plugins
%if %{with pyqt5}
BuildRequires: python-qt5-devel
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

%define libqs5 %mklibname qscintilla_qt5 13

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
%attr(755,root,root) %{_libdir}/libqscintilla2_qt5.so.*
%{_datadir}/qt5/translations/qscintilla*.qm

#--------------------------------------------------------------

%define libqs5dev %mklibname -d qscintilla_qt5

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
%{_libdir}/libqscintilla2_qt5.so
%{qt5plugins}/designer/*
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

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
%_datadir/sip/PyQt5
%qt5dir/qsci
%py_platsitedir/PyQt5/Qsci.so
%py_platsitedir/PyQt5/Qsci.pyi
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
%setup -qn QScintilla_gpl-%{version}
%apply_patches

%build
export QTDIR=%qt5dir

pushd Qt4Qt5
	%qmake_qt5 qscintilla.pro
	%make 
popd

pushd designer-Qt4Qt5
	%qmake_qt5 designer.pro INCLUDEPATH+=../Qt4Qt5 LIBS+=-L../Qt4Qt5
	sed -i -e 's,-lpthread,-lpthread -lqscintilla2_qt5,g' Makefile
	%make
popd

%if %{with pyqt5}
pushd Python
	python configure.py \
		--qsci-incdir=../Qt4Qt5 \
		--pyqt-sipdir=/usr/share/sip/PyQt5 \
		--qsci-libdir=../Qt4Qt5 \
	--pyqt=PyQt5
	sed -i -e 's,-lpthread,-lpthread -lpython3.7m -lqscintilla2_qt5,g' Makefile
	%make
popd
%endif

%install
make -C Qt4Qt5 INSTALL_ROOT=%buildroot install

make -C designer-Qt4Qt5 INSTALL_ROOT=%buildroot install

%if %{with pyqt5}
	make -C Python INSTALL_ROOT=%buildroot install
%else
	rm -rf %buildroot%{_datadir}/qt5/qsci
%endif
