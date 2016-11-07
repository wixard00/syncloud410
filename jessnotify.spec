# -*- mode: python -*-
a = Analysis(['jessnotify.py'],
             pathex=['F:\\proyectos_python\\syncloud3'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='jessnotify.exe',
          debug=False,
          strip=None,
          upx=True,
          console=False )
