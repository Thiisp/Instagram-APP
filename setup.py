import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None

if sys.platform == 'win32':
    base = 'Win32GUI'

setup (
    name = 'Menu Instagram',
    version = '3.0',
    description = 'Menu Hack Instagram by @thiisp',
    options = {'build_exe': build_exe_options},
    executables = [Executable('app.py', base = base)]
)

# python setup.py build