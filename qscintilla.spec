%define with_qt3 0
%{?_with_qt3: %{expand: %%global with_qt3 1}}

Name: qscintilla
Summary: Port to Qt of Neil Hodgson's Scintilla C++ editor class
Version: 2.7
Release: 1
License: GPLv2+
Group: System/Libraries
Source0: http://switch.dl.sourceforge.net/project/pyqt/QScintilla2/QScintilla-%version/QScintilla-gpl-%version.tar.gz
Patch0: QScintilla-gpl-2.2-libdir.patch
Patch1: QScintilla-gpl-2.4-fix-linkage.patch
URL: http://www.riverbankcomputing.co.uk/software/qscintilla/intro
%if %{with_qt3}
BuildRequires: qt3-devel
BuildRequires: python-qt >= 1:3.16.0
%endif # with_qt3
BuildRequires: qt4-devel >= 2:4.3.1
BuildRequires: python-sip >= 1:4.7.10
BuildRequires: python-qt4-devel
BuildRequires: python-devel

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

%files -n %libqs3
%defattr(644,root,root,755)
%attr(755,root,root) %{qt3lib}/*.so.*
%{qt3dir}/translations/qscintilla*.qm

#--------------------------------------------------------------

%define libqs3dev %mklibname -d qscintilla-qt3

%package -n %libqs3dev
Summary: Libraries, headers and other files to develop with QScintilla for Qt3
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
%doc NEWS README doc	

#--------------------------------------------------------------

%prep 
%setup -qn QScintilla-gpl-%{version}
%patch0 -p1 -b .libbuild
%patch1 -p0 -b .linkage

%build
%if %{with_qt3}
pushd Qt3 
    export QTDIR=%qt3dir
    %qmake_qt3 DESTDIR=%buildroot/%{qt3lib} qscintilla.pro
    %make 
popd
%endif

pushd Qt4Qt5
    export QTDIR=%qt4dir
    %qmake_qt4 DESTDIR=%buildroot/%{qt4lib} qscintilla.pro
    %make 
popd

pushd designer-Qt4
    echo "INCLUDEPATH += ../Qt4Qt5" >> designer.pro
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

pushd Qt4Qt5
    make INSTALL_ROOT=%buildroot install
popd

pushd designer-Qt4
    make INSTALL_ROOT=%buildroot install
popd

pushd Python
    export QTDIR=%qt4dir
    export PATH=%qt4dir/bin:$PATH
    python configure.py \
        -n ../Qt4Qt5 \
        -o %buildroot/%{qt4lib} 
    %make 
    make DESTDIR=%buildroot install
popd

%clean
rm -rf %{buildroot}




%changelog
* Mon May 09 2011 Funda Wang <fwang@mandriva.org> 2.5.1-2mdv2011.0
+ Revision: 672654
- rebuild

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 2.5.1-1
+ Revision: 654066
- New version 2.5.1

* Sat Apr 02 2011 Funda Wang <fwang@mandriva.org> 2.5-1
+ Revision: 649923
- update to new version 2.5

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 2.4.6-1mdv2011.0
+ Revision: 624706
- update to new version 2.4.6

* Sat Dec 25 2010 Funda Wang <fwang@mandriva.org> 2.4.5-3mdv2011.0
+ Revision: 624705
- rebuild

* Sun Oct 31 2010 Funda Wang <fwang@mandriva.org> 2.4.5-2mdv2011.0
+ Revision: 590744
- rebuild for py2.7

* Wed Sep 01 2010 Funda Wang <fwang@mandriva.org> 2.4.5-1mdv2011.0
+ Revision: 575017
- new version 2.4.5

* Thu Jul 15 2010 Funda Wang <fwang@mandriva.org> 2.4.4-1mdv2011.0
+ Revision: 553427
- new version 2.4.4

* Thu Mar 18 2010 Funda Wang <fwang@mandriva.org> 2.4.3-1mdv2010.1
+ Revision: 524770
- new version 2.4.3

* Thu Jan 21 2010 Funda Wang <fwang@mandriva.org> 2.4.2-1mdv2010.1
+ Revision: 494593
- New version 2.4.2

* Sat Jan 09 2010 Funda Wang <fwang@mandriva.org> 2.4-6mdv2010.1
+ Revision: 488141
- rebuild for new sip

* Mon Sep 28 2009 Helio Chissini de Castro <helio@mandriva.com> 2.4-5mdv2010.0
+ Revision: 450614
- Recompile to fix Mandriva bug #54120

* Mon Sep 28 2009 Funda Wang <fwang@mandriva.org> 2.4-3mdv2010.0
+ Revision: 450603
- rebuild for new python-sip

* Wed Jul 22 2009 Helio Chissini de Castro <helio@mandriva.com> 2.4-2mdv2010.0
+ Revision: 398522
- Rebuild against current python-qt4

* Sat Jun 06 2009 Funda Wang <fwang@mandriva.org> 2.4-1mdv2010.0
+ Revision: 383208
- New version 2.4

* Sat Dec 27 2008 Funda Wang <fwang@mandriva.org> 2.3.2-2mdv2009.1
+ Revision: 319759
- rebuild for new python

* Tue Nov 18 2008 Funda Wang <fwang@mandriva.org> 2.3.2-1mdv2009.1
+ Revision: 304176
- New version 2.3.2

* Sun Nov 09 2008 Funda Wang <fwang@mandriva.org> 2.3.1-1mdv2009.1
+ Revision: 301228
- New version 2.3.1

* Sat Oct 11 2008 Funda Wang <fwang@mandriva.org> 2.3-1mdv2009.1
+ Revision: 292162
- New version 2.3

* Tue Sep 30 2008 Helio Chissini de Castro <helio@mandriva.com> 2.2-5mdv2009.0
+ Revision: 290245
- Broken repository plus still valid qt3 plugins are causing segfaults in qt4 designer and python qt4 apps depending on qscintilla

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 2.2-4mdv2009.0
+ Revision: 265589
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jun 04 2008 Helio Chissini de Castro <helio@mandriva.com> 2.2-3mdv2009.0
+ Revision: 215017
- No more qt3 build, added a switch
- Added easy provides for build

* Thu May 22 2008 Funda Wang <fwang@mandriva.org> 2.2-2mdv2009.0
+ Revision: 209983
- rediff libdir patch
- New version 2.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Sep 21 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 2.1-3mdv2008.0
+ Revision: 91997
- Rebuild for missing packages

* Wed Aug 22 2007 Helio Chissini de Castro <helio@mandriva.com> 2.1-2mdv2008.0
+ Revision: 68766
- Fix designer plugin build
- New upstream release
- Qt3 and Qt4 builds
- Need take a little more care with package naming
- New qscintilla release. With both qt 3 and 4 bindings, a small package name change was needed.
  Until new python-qt build against new scintilla, luma and eric3 will be broken. With python-qt4,
  eric3 will be obsoleted in favour of eric4.

* Tue May 22 2007 Helio Chissini de Castro <helio@mandriva.com> 1.7.1-2mdv2008.0
+ Revision: 29892
- Easy upgrade on qscintilla

* Tue May 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7.1-1mdv2008.0
+ Revision: 25028
- fix build on x86_64
- spec file clean
- update to the latest version
- drop P0
- Import qscintilla



* Sun Jun 25 2006 Laurent MONTEL <lmontel@mandriva.com> 1.6-6
- Rebuild with new libpng

* Fri Dec 16 2005 Austin Acton <austin@mandriva.org> 1.6-5mdk
- mkrel

* Wed Nov 16 2005 Austin Acton <austin@mandriva.org> 1.6-4mdk
- ease upgrades (thanks Buchan)

* Thu Nov 10 2005 Austin Acton <austin@mandriva.org> 1.6-3mdk
- more install fixing

* Wed Nov 9 2005 Austin Acton <austin@mandriva.org> 1.6-2mdk
- split off translations
- fix install

* Tue Nov 8 2005 Austin Acton <austin@mandriva.org> 1.6-1mdk
- 1.6

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 1.5.1-1mdk
- 1.5.1

* Mon Aug 22 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.5-2mdk
- lib64 fixes + let qmake decide the right QMAKESPEC

* Sun Feb 20 2005 Austin Acton <austin@mandrake.org> 1.5-1mdk
- 1.5

* Tue Sep 21 2004 Austin Acton <austin@mandrake.org> 1.4-2mdk
- major 5

* Mon Sep 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.4-1mdk
- 1.4

* Tue Jul 06 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-3mdk
- Fix ldconfig

* Fri Jun 18 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 1.3-2mdk
- Rebuild

* Tue Jun 1 2004 Austin Acton <austin@mandrake.org> 1.2-1mdk
- 1.3
- major 4
- try to make it more sane and less linty

* Wed Aug 20 2003 Austin Acton <aacton@yorku.ca> 1.2-1mdk
- 1.2
- major 3

* Tue Jul 15 2003 Austin Acton <aacton@yorku.ca> 1.1-2mdk
- rebuild for rpm

* Fri May 23 2003 Austin Acton <aacton@yorku.ca> 1.1-1mdk
- new URL
- new version
- new major

* Fri May 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- more mklibname
- from Jérôme Martin <jerome.f.martin@free.fr> :
	- Version 1.0 (for sip/pyqt 3.6)

* Sat Mar  8 2003 Jerome Martin <jerome.f.martin@free.fr> 0.3-2mdk
- Fix pb

* Mon Dec  2 2002 Jerome Martin <jerome.f.martin@free.fr> 0.3-1mdk
- First release
