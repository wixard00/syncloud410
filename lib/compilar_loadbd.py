# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(name="loadbd",
 version="1.2.1",
 description="Programa de carga de datos para VisualWEB",
 author="Manuel Ordoñez",
 author_email="manuelordonez@openmailbox.org",
 url="www.olesistemas.com",
 license="GPL",
 scripts=["loadbd.py"],
 console=["loadbd.py"],
 options={"py2exe": {"bundle_files": 1}},
 zipfile=None,
)