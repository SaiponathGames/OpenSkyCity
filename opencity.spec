# -*- mode: python ; coding: utf-8 -*-

from kivy.tools.packaging.pyinstaller_hooks import get_deps_all, hookspath, runtime_hooks
from kivy_deps import sdl2, glew, gstreamer
block_cipher = None


a = Analysis(['main.py'],
             pathex=['F:/OpenCity_Dev/OpenCity'],
             datas=[],
             hookspath=hookspath(),
             runtime_hooks=runtime_hooks(),
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False,
			 **get_deps_all())
a.datas += Tree('./src', prefix='src')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz, *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='opencity',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='F:/OpenCity_Dev/OpenCity/src/front_ui_display/opencity_kivy/opencityicon_1_64.ico')
