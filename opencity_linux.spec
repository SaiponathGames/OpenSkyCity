# -*- mode: python ; coding: utf-8 -*-

from kivy.tools.packaging.pyinstaller_hooks import get_deps_all, hookspath, runtime_hooks
block_cipher = None


a = Analysis(['main.py'],
             pathex=['/mnt/f/OpenCity_Dev/OpenCity'],
             datas=[],
			 hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
			 **get_deps_all())
a.datas += Tree('./src', 'src')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='opencity-linux',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='mnt/f/OpenCity_Dev/OpenCity/src/front_ui_display/opencity_kivy/OpenCity_Icon_photoshop.png')
