# -*- coding: utf-8 -*-

from distutils.core import setup
import py2exe

setup(name="mensaje",
 version="0.5.0",
 description="Servicio de Mensajeria SMS de VisualFAC",
 author="Manuel Ordoñez",
 author_email="manuelordonez@openmailbox.org",
 url="www.olesistemas.com",
 license="GPL",
 scripts=["mensaje.py"],
 console=["mensaje.py"],
 options={"py2exe": {"bundle_files": 3}},
 zipfile="mensaje.dll",
)