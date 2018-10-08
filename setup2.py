from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

DATA=[('imageformats',['C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qjpeg4.dll',
    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qgif4.dll',
    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qico4.dll',
    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qmng4.dll',
    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qsvg4.dll',
    'C:\\Python27/Lib/site-packages/PySide/plugins/imageformats/qtiff4.dll'
    ])]

setup(
    options={"py2exe":{"dll_excludes": ["MSVCP90.dll"]}},
    name="Registro Y Llaves",
    version="0.4",
    windows = [{'script': "Inicio.py",
                "icon_resources": [(1, "%s/icono.ico"%str(os.getcwd()))],}],
    zipfile = None,
    data_files = DATA,
)
