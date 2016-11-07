# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(name="SynCloud",
 version="3.1.0",
 description="Servicio Integrado de SynCloud",
 author="Manuel Ordoñez",
 author_email="manuelordonez@openmailbox.org",
 url="www.olesistemas.com",
 license="GPL",
 scripts=["syncloud.py"],
 console=["syncloud.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)