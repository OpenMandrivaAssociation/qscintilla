%define oldlibqs5 %mklibname qscintilla_qt5 13
%define libqs5 %mklibname qscintilla_qt5
%define libqs5dev %mklibname -d qscintilla_qt5
%define libqs6 %mklibname qscintilla_qt6
%define libqs6dev %mklibname -d qscintilla_qt6

%bcond_without qt6

Summary:	Port to Qt of Neil Hodgson's Scintilla C++ editor class
Name:		qscintilla
Version:	2.14.1
Release:	15
License:	GPLv2+
Group:		System/Libraries
Source0:	https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz
Patch0:		qscintilla-2.12.1-no-underlinking.patch
URL:		https://www.riverbankcomputing.com/software/qscintilla/intro
BuildRequires:	make
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	qmake5
BuildRequires:	qt5-qtbase-macros
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Designer)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(dbus-python)
BuildRequires:	python-qt-builder
BuildRequires:	python-qt5-devel
BuildRequires:	python-sip
BuildRequires:	python-sip-qt5
%if %{with qt6}
BuildRequires:	cmake(Qt6)
BuildRequires:	qmake-qt6
BuildRequires:	pkgconfig(Qt6Core)
BuildRequires:	pkgconfig(Qt6DBus)
BuildRequires:	pkgconfig(Qt6Gui)
BuildRequires:	pkgconfig(Qt6OpenGL)
BuildRequires:	pkgconfig(Qt6PrintSupport)
BuildRequires:	pkgconfig(Qt6Widgets)
BuildRequires:	pkgconfig(Qt6Designer)
BuildRequires:	pkgconfig(Qt6Xml)
BuildRequires:	python-qt6-devel
BuildRequires:	python-sip-qt6
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
Summary:	Port to Qt 5.x of Neil Hodgson's Scintilla C++ editor class
Group:		System/Libraries
%rename %{oldlibqs5}

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

#--------------------------------------------------------------

%package -n %{libqs5dev}
Summary:	Libraries, include and other files to develop with QScintilla for Qt5
Group:		Development/KDE and Qt
Requires:	%{libqs5} = %{version}-%{release}
Provides:	%{name}-qt5-devel = %{version}-%{release}
Provides:	qscintilla-qt5-devel = %{version}-%{release}

%description -n %{libqs5dev}
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %{libqs5dev}
%{_includedir}/qt5/Qsci
%{_libdir}/libqscintilla2_qt5.so
%{_qt5_plugindir}/designer/*
%{_libdir}/qt5/mkspecs/features/qscintilla2.prf

#--------------------------------------------------------------

%package -n python-qt5-qscintilla
Summary:	Python qt5 QScintilla bindings
Group:		Development/KDE and Qt
Requires:	python-qt5-core
Requires:	python-qt5-gui
Requires:	python-qt5-widgets
Requires:	python-qt5-printsupport
Requires:	python-sip
Requires:	python-sip-qt5
Requires:	%{libqs5} = %{EVRD}

%description -n python-qt5-qscintilla
Python qt5 QScintilla bindings.

%files -n python-qt5-qscintilla
%{_libdir}/python*/site-packages/PyQt5/Qsci.abi3.so
%{_libdir}/python*/site-packages/PyQt5/bindings/Qsci
%{_libdir}/python*/site-packages/qscintilla-*.dist-info
%{_datadir}/qt5/qsci/api/python

#--------------------------------------------------------------

%package -n %{libqs6}
Summary:	Port to Qt 6.x of Neil Hodgson's Scintilla C++ editor class
Group:		System/Libraries

%description -n %{libqs6}
As well as features found in standard text editing components,
QScintilla includes features especially useful when editing and
debugging source code. These include support for syntax styling, error
indicators, code completion and call tips. The selection margin can
contain markers like those used in debuggers to indicate breakpoints
and the current line. Styling choices are more open than with many
editors, allowing the use of proportional fonts, bold and italics,
multiple foreground and background colours and multiple fonts.

%files -n %{libqs6} -f %{name}.lang
%{_qtdir}/lib/libqscintilla2_qt6.so.*

#--------------------------------------------------------------

%package -n %{libqs6dev}
Summary:	Libraries, include and other files to develop with QScintilla for Qt6
Group:		Development/KDE and Qt
Requires:	%{libqs6} = %{version}-%{release}
Provides:	%{name}-qt6-devel = %{version}-%{release}
Provides:	qscintilla-qt6-devel = %{version}-%{release}

%description -n %{libqs6dev}
This packages contains the libraries, include and other files
you can use to develop applications with QScintilla.

%files -n %{libqs6dev}
%{_qtdir}/include/Qsci
%{_qtdir}/lib/libqscintilla2_qt6.so
%{_qtdir}/plugins/designer/*
%{_qtdir}/mkspecs/features/qscintilla2.prf

#--------------------------------------------------------------

%package -n python-qt6-qscintilla
Summary:	Python qt6 QScintilla bindings
Group:		Development/KDE and Qt
Requires:	python-qt6-core
Requires:	python-qt6-gui
Requires:	python-qt6-widgets
Requires:	python-qt6-printsupport
Requires:	python-sip
Requires:	python-sip-qt6
Requires:	%{libqs6} = %{EVRD}

%description -n python-qt6-qscintilla
Python qt5 QScintilla bindings.

%files -n python-qt6-qscintilla
%{_libdir}/python*/site-packages/PyQt6/Qsci.abi3.so
%{_libdir}/python*/site-packages/PyQt6/bindings/Qsci
%{_libdir}/python*/site-packages/pyqt6_qscintilla-*.dist-info
%{_qtdir}/qsci

#--------------------------------------------------------------

%package doc
Summary:	QScintilla docs
Group:		Development/KDE and Qt

%description doc
QScintilla doc.

%files doc
%defattr(644,root,root,755)
%doc NEWS doc

#--------------------------------------------------------------

%prep
%autosetup -n QScintilla_src-%{version} -p1

%build
PATH=%{_qt5_bindir}:$PATH; export PATH

cd src
	%qmake_qt5 qscintilla.pro
	%make_build
cd -

# (fedora) set QMAKEFEATURES to ensure just built lib/feature is found
QMAKEFEATURES=$(pwd)/Qt4Qt5/features; export QMAKEFEATURES

cd designer
	%qmake_qt5 designer.pro INCLUDEPATH+=../src LIBS+=-L../src
	%make_build
cd -

cd Python
	ln -s pyproject-qt5.toml pyproject.toml
	sip-build --qsci-library-dir `pwd`/../src --qsci-include-dir `pwd`/../src --qsci-features-dir `pwd`/../src/features --no-make
	%make_build -C build
cd -

%install
%make_install -C src INSTALL_ROOT=%{buildroot}
%make_install -C designer INSTALL_ROOT=%{buildroot}
%make_install -C Python/build INSTALL_ROOT=%{buildroot}

%if %{with qt6}
cd src
make clean
qmake-qt6 qscintilla.pro
%make_build
%make_install INSTALL_ROOT=%{buildroot}

cd ../designer
make clean
qmake-qt6 designer.pro INCLUDEPATH+=../src LIBS+=-L../src
%make_build
%make_install INSTALL_ROOT=%{buildroot}

cd ../Python
rm -rf build
ln -sf pyproject-qt6.toml pyproject.toml
sip-build --qsci-library-dir `pwd`/../src --qsci-include-dir `pwd`/../src --qsci-features-dir `pwd`/../src/features --no-make --qmake=%{_bindir}/qmake-qt6
%make_build -C build
%make_install -C build INSTALL_ROOT=%{buildroot}
cd ..
%endif

# locales
%find_lang %{name} --with-qt
