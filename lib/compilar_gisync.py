# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(name="gisync",
 version="1.2.1",
 description="Servicio de SynCloud",
 author="Manuel Ordoñez",
 author_email="manuelordonez@openmailbox.org",
 url="www.olesistemas.com",
 license="GPL",
 scripts=["gisync.py"],
 windows=["gisync.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)