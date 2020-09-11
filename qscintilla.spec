%define debug_package %{nil}

%define qt5plugins %{_libdir}/qt5/plugins
%define qt5include %{_includedir}/qt5

%define libqs5 %mklibname qscintilla_qt5 13
%define libqs5dev %mklibname -d qscintilla_qt5

%bcond_without pyqt5
%bcond_with py2qt5

Summary:	Port to Qt of Neil Hodgson's Scintilla C++ editor class
Name:		qscintilla
Version:	2.11.5
Release:	1
License:	GPLv2+
Group:		System/Libraries
Source0:	https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla-%{version}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/intro
BuildRequires:	qmake5
BuildRequires:	qt5-macros
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Designer)
%if %with pyqt5
BuildRequires:	pkgconfig(python)
BuildRequires:	qt5-qtbase-macros
BuildRequires:	python-qt5-devel
BuildRequires:	python-sip
%endif
%if %with py2qt5
BuildRequires:	pkgconfig(python2)
BuildRequires:	qt5-qtbase-macros
BuildRequires:	python2-qt5-devel
BuildRequires:	python2-sip
%endif

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

%package -n %{libqs5}
Summary:	Port to Qt of Neil Hodgson's Scintilla C++ editor class
Group:		System/Libraries

%description -n %{libqs5}
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%files -n %{libqs5} -f %{name}.lang
%{_libdir}/libqscintilla2_qt5.so.*
#% {_datadir}/qt5/translations/qscintilla*.qm

#--------------------------------------------------------------

%package -n %{libqs5dev}
Summary:	Libraries, include and other files to develop with QScintilla for Qt5
Group:		Development/KDE and Qt
Requires:	%{libqs5} = %{version}-%{release}
Provides:	%{name}-qt5-devel = %{version}-%{release}
Provides:	qscintilla-qt5-devel = %{version}-%{release}
#Obsoletes:	%{_lib}qscintilla-qt5_-devel

%description -n %{libqs5dev}
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %{libqs5dev}
%{_includedir}/qt5/Qsci
%{_libdir}/libqscintilla2_qt5.so
%{qt5plugins}/designer/*
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

#--------------------------------------------------------------

%if %{with pyqt5}
%package -n python-qt5-qscintilla
Summary:	Python qt5 QScintilla bindings
Group:		Development/KDE and Qt
Requires:	python-qt5-core
Requires:	python-qt5-gui
Requires:	%{libqs5}

%description -n python-qt5-qscintilla
Python qt5 QScintilla bindings.

%files -n python-qt5-qscintilla
%{_datadir}/sip/PyQt5
%{_qt5_datadir}/qsci/
%{py_platsitedir}/PyQt5/Qsci.so
%{py_platsitedir}/PyQt5/Qsci.pyi
%endif

#--------------------------------------------------------------

%if %{with py2qt5}
%package -n python2-qt5-qscintilla
Summary:	Python qt5 QScintilla bindings
Group:		Development/KDE and Qt
Requires:	python2-qt5-core
Requires:	python2-qt5-gui
Requires:	%{libqs5}

%description -n python2-qt5-qscintilla
Python qt5 QScintilla bindings.

%files -n python2-qt5-qscintilla
%{_datadir}/sip/PyQt5
%{_qt5_datadir}/qsci/
%{py2_platsitedir}/PyQt5/Qsci.so
%{py2_platsitedir}/PyQt5/Qsci.pyi
%endif

#--------------------------------------------------------------

%package doc
Summary:	QScintilla docs
Group:		Development/KDE and Qt

%description doc
QScintilla doc.

%files doc
%defattr(644,root,root,755)
%doc NEWS README doc

#--------------------------------------------------------------

%prep
%setup -qn QScintilla_gpl-%{version}
%autopatch -p1

%build
cp -a Qt4Qt5 Qt5
cp -a designer-Qt4Qt5 designer-Qt5
cp -a Python Python-Qt5
%if %{with py2qt5}
cp -a Python Python2-Qt5
%endif

cd Qt5
	%qmake_qt5 qscintilla.pro
	%make_build
cd -

# (fedora) set QMAKEFEATURES to ensure just built lib/feature is found
QMAKEFEATURES=$(pwd)/Qt5/features; export QMAKEFEATURES

cd designer-Qt5
	%qmake_qt5 designer.pro INCLUDEPATH+=../Qt5 LIBS+=-L../Qt5
	%make_build
cd -

%if %{with pyqt5}
cd Python-Qt5
	INCLUDEPATH+="{qt5include}/QtWdgets %{qt5include}/QtPrintSupport" \
	python configure.py \
		--pyqt=PyQt5 \
		--pyqt-sipdir=%{_datadir}/sip/PyQt5 \
		--qsci-incdir=../Qt5 \
		--qsci-libdir=../Qt5 \
		--qmake="%{_qt5_bindir}/qmake" \
		--no-dist-info
	%make_build
cd -
%endif

%if %{with py2qt5}
cd Python2-Qt5
	INCLUDEPATH="%{qt5include}/QtWdgets %{qt5include}/QtPrintSupport" \
	python2 configure.py \
		--pyqt=PyQt5 \
		--pyqt-sipdir=%{_datadir}/sip/PyQt5 \
		--qsci-incdir=../Qt5 \
		--qsci-libdir=../Qt5 \
		--qmake="%{_qt5_bindir}/qmake" \
		--no-dist-info
	%make_build
cd -
%endif

%install
%make_install -C Qt5 INSTALL_ROOT=%{buildroot}
%make_install -C designer-Qt5  INSTALL_ROOT=%{buildroot}
%if %{with pyqt5}
	%make_install -C Python-Qt5 INSTALL_ROOT=%{buildroot} install
%endif
%if %{with py2qt5}
	%make_install -C Python2-Qt5 INSTALL_ROOT=%{buildroot} install
%endif
%if !%{with pyqt5} && !%{with py2qt5}
	rm -rf %{buildroot}%{_datadir}/qt5/qsci
%endif

# locales
%find_lang %{name} --with-qt
