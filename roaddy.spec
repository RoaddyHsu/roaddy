# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller 設定檔
用於自訂打包選項
"""

import os
from pathlib import Path

block_cipher = None

# 收集所有資料檔案
datas = [
    ('config', 'config'),
    ('.env.example', '.'),
]

# 隱藏導入
hiddenimports = [
    'anthropic',
    'openai',
    'rich',
    'rich.console',
    'rich.panel',
    'rich.markdown',
    'rich.prompt',
    'prompt_toolkit',
    'prompt_toolkit.history',
    'click',
    'yaml',
    'pyyaml',
    'requests',
    'python-dotenv',
    'dotenv',
]

a = Analysis(
    ['src/main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='弘爺漢堡AI行銷助手',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # True=顯示命令列視窗, False=隱藏
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico' if os.path.exists('icon.ico') else None,
)
