from PySide.QtGui import *
from PySide.QtCore import *
import sqlite3,Mensage

class tk(QWidget):
	def __init__(self,dire):
		super(tk,self).__init__()
		self.dir=dire
		self.msgAl=Mensage.Msg(self,self.dir)
		with open('%s/css/styleTk5.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.conte=QGridLayout()
		self.labeGrad()
		self.db=sqlite3.connect('%s/baseData/config.db'%self.dir)
		self.crearTabla()
		self.loadDefault()
		self.setLayout(self.conte)
	def labeGrad(self):
		self.textPr=QLabel("Cantidad de Principales",self)
		self.textSg=QLabel("Cantidad de Suplentes",self)
		self.linePr=QLineEdit(self)
		self.lineSg=QLineEdit(self)
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar")
		self.botonSave.setIconSize(QSize(30,30))
		self.botonSave.clicked.connect(self.guardar)
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar")
		self.botonClear.clicked.connect(self.borrar)
		self.botonClear.setIconSize(QSize(30,30))
		self.conte.addWidget(self.textPr,0,0)
		self.conte.addWidget(self.linePr,0,1)
		self.conte.addWidget(self.textSg,1,0)
		self.conte.addWidget(self.lineSg,1,1)
		self.conte.addWidget(self.botonSave,2,2)
		self.conte.addWidget(self.botonClear,2,3)
	def borrar(self):
		self.lineSg.clear()
		self.linePr.clear()
	def loadDefault(self):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Tk5 WHERE ID=0")
		for i in cur:
			self.linePr.setText(str(i[1]))
			self.lineSg.setText(str(i[2]))
		cur.close()
		self.db.commit()
	def guardar(self):
		datoAu=[int(self.linePr.text()),int(self.lineSg.text())]
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Tk5 WHERE ID=0")
		self.db.commit()
		row=cur.fetchone()
		try:
			if len(row) is not None:
				cur.execute("UPDATE Tk5 SET Principal=?,Suplente=? WHERE ID=0",datoAu)
				self.db.commit()
		except TypeError:
			datoAu=[0,int(self.linePr.text()),int(self.lineSg.text())]
			cur.execute("INSERT INTO Tk5 VALUES (?,?,?)",datoAu)
			self.db.commit()
		cur.close()
		self.msgAl.mensageBueno("<h2>Guardo Correctamente</h2>")
	def crearTabla(self):
		cur=self.db.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Tk5(ID INT,Principal INT,Suplente INT)')
		self.db.commit()
		cur.close()
