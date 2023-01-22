from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3,Mensage

class pumses(QWidget):
	def __init__(self,dire):
		super(pumses,self).__init__()
		self.gradoL=["10mo","9no","8vo","7mo","6to","5to","4to","3ro","2do","1er"]
		self.gradLE=[]
		self.dir=dire
		self.msg=Mensage.Msg(self.dir)
		with open('%s/css/stylePumse.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.conte=QGridLayout()
		self.labeGrad()
		self.db=sqlite3.connect('%s/baseData/config.db'%self.dir)
		self.crearTabla()
		self.loadDefault()
		self.setLayout(self.conte)
	def labeGrad(self):
		tamanio=len(self.gradoL)
		for i in range(tamanio):
			if i<5:
				self.conte.addWidget(QLabel("<h2>%s kup</h2>"%self.gradoL[i]),i,0)
				self.gradLE.append(QLineEdit())
				self.conte.addWidget(self.gradLE[i],i,1)
			else:
				self.conte.addWidget(QLabel("<h2>%s kup</h2>"%self.gradoL[i]),i-5,2)
				self.gradLE.append(QLineEdit())
				self.conte.addWidget(self.gradLE[i],i-5,4)
		self.gradoM=["1er","2do","3ro"]
		for j in range(3): 
			self.conte.addWidget(QLabel("<h2>%s DAN</h2>"%self.gradoM[j]),5+j,0)
			self.gradLE.append(QLineEdit())
			self.conte.addWidget(self.gradLE[10+j],5+j,1)
		for i in range(3):
			self.conte.addWidget(QLabel("<h2>%s POOM</h2>"%self.gradoM[i]),5+i,2)
			self.gradLE.append(QLineEdit())
			self.conte.addWidget(self.gradLE[13+i],5+i,4)
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar")
		self.botonSave.setIconSize(QSize(30,30))
		self.botonSave.clicked.connect(self.guardar)
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar")
		self.botonClear.setIconSize(QSize(30,30))
		self.botonClear.clicked.connect(self.borrar)
		self.conte.addWidget(self.botonSave,6,5)
		self.conte.addWidget(self.botonClear,7,5)
	def borrar(self):
		for i in range(len(self.gradLE)):
			self.gradLE[i].clear()
	def loadDefault(self):
		cur=self.db.cursor()
		cur.execute("SELECT Formas FROM Pumse")
		cont=0
		for i in cur:
			self.gradLE[cont].setText(str(i[0]))
			cont+=1
		cur.close()
		self.db.commit()
	def guardar(self):
		grado=["10kup","9kup","8kup","7kup","6kup","5kup","4kup","3kup",
		"2kup","1kup","1dan","2dan","3dan","1poom","2poom","3poom"]
		cur=self.db.cursor()
		for i in range(len(grado)):
			cur.execute("SELECT * FROM Pumse WHERE Grado=:c ",{"c":str(grado[i])})
			self.db.commit()
			row=cur.fetchone()
			dato=(str(grado[i]),str(self.gradLE[i].text().replace(' ','')))
			try:
				if len(row) is not None:
					datoAu=(str(self.gradLE[i].text().replace(' ','')),str(grado[i]))
					cur.execute("UPDATE Pumse SET Formas=? WHERE Grado=?",datoAu)
					self.db.commit()
			except TypeError:
				cur.execute("INSERT INTO Pumse VALUES(?,?)", dato)
				self.db.commit()
		cur.close()
		self.msg.mensageBueno("<h2>Grados Guardado\nCorrectamente</h2>")
	def crearTabla(self):
		cur=self.db.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Pumse(Grado TEXT,Formas TEXT)')
		self.db.commit()
		cur.close()
