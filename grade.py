from PySide.QtGui import *
from PySide.QtCore import *
import sqlite3,os,Mensage

class grades(QWidget):
	def __init__(self):
		super(grades,self).__init__()
		self.dir='C:/Registro'
		self.datos=sqlite3.connect('%s/baseData/config.db'%self.dir)
		self.createTabla()
		with open('%s/css/styleGrad.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.msgAl=Mensage.Msg(self)
		self.contenedor=QGridLayout()
		self.labe=["Principiantes","Novatos","Avanzados","Poom","Dan"]
		self.texts=[]
		self.element()
		self.setLayout(self.contenedor)
		self.loadInfo()
	def element(self):
		for i in range(len(self.labe)):
			self.contenedor.addWidget(QLabel("<h2>%s</h2>"%str(self.labe[i])),i,0)
			self.texts.append(QLineEdit())
			self.contenedor.addWidget(self.texts[i],i,1)
		self.saveB=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar")
		self.saveB.clicked.connect(self.savedb)
		self.saveB.setIconSize(QSize(30,30))
		self.cleanB=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar")
		self.cleanB.clicked.connect(self.cleanT)
		self.cleanB.setIconSize(QSize(30,30))
		self.contenedor.addWidget(self.saveB,4,2)
		self.contenedor.addWidget(self.cleanB,3,2)
	def savedb(self):
		cursor=self.datos.cursor()
		for i in range(len(self.labe)):
			try:
				cursor.execute("SELECT nombre FROM grados WHERE nombre=:nom",
					{"nom": str(self.labe[i])})
				self.datos.commit()
				inf=[str(self.texts[i].text()).replace(" ",''),str(self.labe[i])]
				row=cursor.fetchone()
				if len(row) is not None:
					cursor.execute("UPDATE grados SET cinturon=? WHERE nombre=?",inf)
					self.datos.commit()
			except TypeError:
				inf=[str(self.labe[i]),str(self.texts[i].text()).replace(" ",'')]
				cursor.execute("INSERT INTO grados VALUES(?, ?)", inf)
				self.datos.commit()
		cursor.close()
		self.msgAl.mensageBueno("<h2>Guardo Correctamente</h2>")
	def infodb(self):
		for i in range(len(self.labe)):
			dato=[]
			dato.append(self.labe[i])
			partition=True
			conf=self.texts[i].text()
			while partition:
				if conf[conf.find(';')]==';':
					dato.append(str(conf[0:conf.find(';')]))
					conf=conf[conf.find(';')+1:]
				else:
					dato.append(str(conf[0:]))
					partition=False
	def cleanT(self):
		for i in range(len(self.texts)):
			self.texts[i].clear()
	def createTabla(self):
		cur=self.datos.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Grados(nombre TEXT,cinturon TEXT)')
		cur.close()
		self.datos.commit()
	def loadInfo(self):
		cursor=self.datos.cursor()
		cursor.execute("SELECT * FROM Grados")
		cont=0
		for i in cursor:
			self.texts[cont].setText(i[1])
			cont+=1
		cursor.close()
	def salir(self):
		self.datos.close()
		self.close()
