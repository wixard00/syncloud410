# HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\MySQL AB\MySQL Server 5.1

import _winreg
import monolib
import platform

#obtiene la ruta a la carpeta "data" de mysql
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def _mysqldata():
    value = ""
    sisversion = platform.machine()
    if sisversion == "AMD64":
        try:
            regpath = "SOFTWARE\\Wow6432Node\\MySQL AB\\MySQL Server 5.1"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "DataLocation")
            value = monolib.validapath(value) + "data/"
        except:
            value = ""
    if sisversion == "x86":
        try:
            regpath = "SOFTWARE\\MySQL AB\\MySQL Server 5.1"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "DataLocation")
            value = monolib.validapath(value) + "data/"
        except:
            value = ""
    return(value)

#obtiene la ruta a la carpeta "bin" de mysql
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


def _mysqlbin():
    value = ""
    sisversion = platform.machine()
    if sisversion == "AMD64":
        try:
            regpath = "SOFTWARE\\Wow6432Node\\MySQL AB\\MySQL Server 5.1"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "Location")
            value = monolib.validapath(value) + "bin/"
        except:
            value = ""
    return(value)


#obtiene la ruta del archivo 7z.exe
def _7zpath():
    value = ""
    try:
        regpath = "SOFTWARE\\7-Zip"
        reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
        value, type = _winreg.QueryValueEx(reg, "Path")
        value = monolib.validapath(value)
    except:
        value = ""
    return(value)


#busca la ubicacion de syncloud en el sistema
def _locatesyncloud():
    value = ""
    sisversion = platform.machine()
    if sisversion == "AMD64":
        try:
            regpath = "SOFTWARE\\Wow6432Node\\Olesistemas\\syncloud"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "Location")
            value = monolib.validapath(value)
        except:
            value = ""
    else:
        try:
            regpath = "SOFTWARE\\Olesistemas\\syncloud"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "Location")
            value = monolib.validapath(value)
        except:
            value = ""
    return(value)

#busca la ubicacion de loadbd en el sistema
def _locatelbd():
    value = ""
    sisversion = platform.machine()
    if sisversion == "AMD64":
        try:
            regpath = "SOFTWARE\\Wow6432Node\\Olesistemas\\syncloud"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "loadbd")
            value = monolib.validapath(value)
        except:
            value = ""
    else:
        try:
            regpath = "SOFTWARE\\Olesistemas\\syncloud"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "loadbd")
            value = monolib.validapath(value)
        except:
            value = ""
    return(value)


#busca la ubicacion de syncloud en el sistema
def _locateupdatebase():
    value = ""
    sisversion = platform.machine()
    if sisversion == "AMD64":
        try:
            regpath = "SOFTWARE\\Wow6432Node\\Olesistemas\\visualweb"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "updatebase")
            value = monolib.validapath(value)
        except:
            value = ""
    else:
        try:
            regpath = "SOFTWARE\\Olesistemas\\visualweb"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "updatebase")
            value = monolib.validapath(value)
        except:
            value = ""
    return(value)


#busca la ubicacion de updatebase en el sistema
def _updatebase():
    value = ""
    sisversion = platform.machine()
    if sisversion == "AMD64":
        try:
            regpath = "SOFTWARE\\Wow6432Node\\Olesistemas\\visualweb"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "updatebase")
            value = monolib.validapath(value)
        except:
            value = ""
    else:
        try:
            regpath = "SOFTWARE\\Olesistemas\\visualweb"
            reg = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, regpath)
            value, type = _winreg.QueryValueEx(reg, "updatebase")
            value = monolib.validapath(value)
        except:
            value = ""
    return(value)
