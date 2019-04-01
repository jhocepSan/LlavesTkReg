import sqlite3

class Conector(object):
	"""Clase que ara la coneccion de la base de datos"""
	def __init__(self, arg):
		super(Conector, self).__init__()
		self.arg = arg
		self.db=sqlite3.connect(namer)
	def createTable(self):
		cur=self.db.cursor()
		cur.execute('CREATE TABLE Hombre(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Club TEXT,FotoP TEXT,FotoC TEXT)')
                        
	def ingresar(self,datos):
		cur=self.db.cursor()
		cur.execute('INSERT INTO')
		