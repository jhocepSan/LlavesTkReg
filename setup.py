from distutils.core import setup
import py2exe
 
setup(
    name="Registro Y Llaves",
    version="0.2",
    windows = [
        {
            "script": "Registro.py",
            "icon_resources": [(1, "icono.ico")],
        }
    ],
)
