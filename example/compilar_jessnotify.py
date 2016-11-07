# -*- encoding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(name="jessnotify",
 version="0.1.0",
 description="Mensajeria SMS desde VisualFAC",
 author="Manuel Ordoñez",
 author_email="manuelordonez@openmailbox.org",
 url="www.olesistemas.com",
 license="GPL",
 scripts=["jessnotify.py"],
 console=["jessnotify.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)