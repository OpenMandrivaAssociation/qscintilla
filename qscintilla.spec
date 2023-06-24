%define libqs5 %mklibname qscintilla_qt5 13
%define libqs5dev %mklibname -d qscintilla_qt5

Summary:	Port to Qt of Neil Hodgson's Scintilla C++ editor class
Name:		qscintilla
Version:	2.14.1
Release:	1
License:	GPLv2+
Group:		System/Libraries
Source0:	https://www.riverbankcomputing.com/static/Downloads/QScintilla/%{version}/QScintilla_src-%{version}.tar.gz
Patch0:		qscintilla-2.12.1-no-underlinking.patch
URL:		http://www.riverbankcomputing.co.uk/software/qscintilla/intro
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
Requires:	python-qt5
Requires:	python-sip
Requires:	python-sip-qt5
Requires:	%{libqs5}

%description -n python-qt5-qscintilla
Python qt5 QScintilla bindings.

%files -n python-qt5-qscintilla
%{_libdir}/python*/site-packages/PyQt5/Qsci.abi3.so
%{_libdir}/python*/site-packages/PyQt5/bindings/Qsci
%{_libdir}/python*/site-packages/QScintilla-*.dist-info
%{_datadir}/qt5/qsci/api/python

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
%make_install -C Python/build INSTALL_ROOT=%{buildroot} install

# locales
%find_lang %{name} --with-qt
