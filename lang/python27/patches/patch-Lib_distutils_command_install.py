$NetBSD: patch-Lib_distutils_command_install.py,v 1.1 2018/06/17 19:21:21 adam Exp $

Add a knob (enviroment variable) for disabling installation of egg metadata
in extensions until we have infrastructure in place for dealing w/ it.

--- Lib/distutils/command/install.py.orig	2017-09-16 17:38:35.000000000 +0000
+++ Lib/distutils/command/install.py
@@ -666,7 +666,7 @@ class install (Command):
                     ('install_headers', has_headers),
                     ('install_scripts', has_scripts),
                     ('install_data',    has_data),
-                    ('install_egg_info', lambda self:True),
+                    ('install_egg_info', lambda self : not os.environ.has_key('PKGSRC_PYTHON_NO_EGG')),
                    ]
 
 # class install
