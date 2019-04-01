from PySide.QtGui import *
from PySide.QtCore import *
import sqlite3,os,Mensage

class kyruguis(QWidget):
	def __init__(self,ruta):
		super(kyruguis,self).__init__()
		self.dir=ruta
		with open('%s/css/styleKiu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.datos=sqlite3.connect("%s/baseData/config.db"%self.dir)
		self.createTabla()
		self.contenedor=QHBoxLayout()
		self.conteText=QGridLayout()
		self.conteBuscar=QVBoxLayout()
		self.msg=Mensage.Msg(self.dir)
		self.vistMenu()
		self.cargarText()
		self.cargarEdit()
		self.groopBus()
	def vistMenu(self):
		self.infUser=QTableWidget(20,3)
		self.infUser.setObjectName("tablaU")
		self.infUser.setHorizontalHeaderLabels(['Sub-Categ','Peso-ini','Peso-fin'])
		self.contenedor.addWidget(self.infUser)
		self.setLayout(self.contenedor)
	def cargarText(self):
		self.genery=QLabel("Genero")
		self.yearIni=QLabel("Edad Ini")
		self.yearMax=QLabel("Edad Fin")
		self.category1=QLabel("Categoria")
		self.conteText.addWidget(self.genery,0,0)
		self.conteText.addWidget(self.yearIni,1,0)
		self.conteText.addWidget(self.yearMax,2,0)
		self.conteText.addWidget(self.category1,3,0)
	def cargarEdit(self):
		self.genero=QComboBox()
		self.genero.addItem(QIcon('%s/Imagenes/hombre.png'%self.dir),"Hombre",0)
		self.genero.addItem(QIcon('%s/Imagenes/mujer.png'%self.dir),"Mujer",1)
		self.genero.setIconSize(QSize(30,30))
		self.edadIni=QSpinBox()
		self.edadIni.setMinimum(4)
		self.edadIni.setMaximum(100)
		self.edadMax=QSpinBox()
		self.edadMax.setMinimum(4)
		self.edadMax.setMaximum(100)
		self.categoria=QLineEdit()
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar")
		self.botonSave.setIconSize(QSize(30,30))
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar")
		self.botonClear.setIconSize(QSize(30,30))
		self.conteText.addWidget(self.genero,0,1)
		self.conteText.addWidget(self.edadIni,1,1)
		self.conteText.addWidget(self.edadMax,2,1)
		self.conteText.addWidget(self.categoria,3,1)
		self.conteText.addWidget(self.botonSave,4,1)
		self.conteText.addWidget(self.botonClear,5,1)
		self.conteBuscar.addLayout(self.conteText)
		self.contenedor.addLayout(self.conteBuscar)
		self.botonSave.clicked.connect(self.save)
		self.botonClear.clicked.connect(self.limpiar)
	def limpiar(self):
		self.infUser.clear()
		self.edadIni.clear()
		self.edadMax.clear()
		self.categoria.clear()
		self.lineBus.clear()
		self.infUser.setHorizontalHeaderLabels(['Sub-Categ','Peso-ini','Peso-fin'])
	def groopBus(self):
		self.config=QGroupBox("Buscar")
		self.config.setObjectName("busqueda")
		self.config.setCheckable(True)
		self.config.setChecked(False)
		self.botonLoad=QPushButton(QIcon('%s/Imagenes/buscar.png'%self.dir),"Buscar")
		self.botonLoad.setIconSize(QSize(30,30))
		self.botonClear=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Borrar")
		self.botonClear.setIconSize(QSize(30,30))
		self.gridBus=QGridLayout()
		self.lineBus=QLineEdit()
		self.category=QLabel("Categoria")
		self.genH=QCheckBox("Hombre")
		self.genM=QCheckBox("Mujer")
		self.gridBus.addWidget(self.genH,0,2)
		self.gridBus.addWidget(self.genM,0,1)
		self.gridBus.addWidget(self.category,1,0)
		self.gridBus.addWidget(self.lineBus,1,1)
		self.gridBus.addWidget(self.botonLoad,2,1)
		self.gridBus.addWidget(self.botonClear,2,2)
		self.config.setLayout(self.gridBus)
		self.conteBuscar.addWidget(self.config)
		self.botonLoad.clicked.connect(self.load)
		self.botonClear.clicked.connect(self.borrar)
		self.genH.clicked.connect(self.verificarGenH)
		self.genM.clicked.connect(self.verificarGenM)
	def borrar(self):
		if self.genH.isChecked() and self.lineBus.text()!='':
			self.borrarInf('CategoriaH','Hombre')
		if self.genM.isChecked()and self.lineBus.text()!='':
			self.borrarInf('CategoriaM','Mujer')
		if self.lineBus.text()=='':
			self.msg.mensageMalo("coloque <h3>Categoria</h3> para borrar\nPor que NO existe")
	def borrarInf(self,cat,gen):
		name=str(self.lineBus.text()).replace(' ','')
		try:
			cur=self.datos.cursor()
			cur.execute("DELETE FROM %s WHERE Categoria=:cat"%cat,{'cat':name})
			cur.execute("DROP TABLE IF EXISTS %s "%str(name+gen))
			cur.close()
			self.datos.commit()
			self.msg.mensageBueno("<h3>la categoria fue\nBORRADO con exito</h3>")
		except sqlite3.OperationalError:
			self.msg.mensageMalo("<h3>No Pudo BORRAR categoria</h3>\nPor que NO existe")
			cur.close()
	def verificarGenM(self):
		if self.genH.isChecked():
			self.genH.setChecked(False)
	def verificarGenH(self):
		if self.genM.isChecked():
			self.genM.setChecked(False)
	def save(self):
		genero=self.genero.currentText()
		if self.categoria.text().isalnum():
			if genero=='Hombre' and self.categoria.text()!='':
				self.saveData('CategoriaH')
			elif genero=='Mujer' and self.categoria.text()!='':
				self.saveData('CategoriaM')
			elif self.categoria.text()=='':
				self.msg.mensageMalo("coloque la <h3>CATEGORIA</h3>")
		else:
			self.msg.mensageMalo(u"<h1>Ingrese puro texto\nsin SIMBOLOS ni ESPACIOS</h1>")
	def saveData(self,category):
		cur=self.datos.cursor()
		nombre=str(self.categoria.text()).replace(' ','')
		datos=(nombre,self.edadIni.value(),self.edadMax.value())
		datoAu=(self.edadIni.value(),self.edadMax.value(),nombre)
		cat=str(self.categoria.text()).replace(' ','')
		try:
			cur.execute("SELECT Categoria FROM %s WHERE Categoria=:cat"%str(category),
				{"cat":cat})
			self.datos.commit()
			row=cur.fetchone()
			if len(row) is not None:
				cur.execute("UPDATE %s SET EdadIni=?,EdadFin=? WHERE Categoria=?"%str(category),
				 datoAu)
				self.datos.commit()
				self.updateSubCat(str(cat+str(self.genero.currentText())))			
		except TypeError:
			cur.execute("INSERT INTO %s VALUES(?, ?, ?)"%str(category), datos)
			try:
				cur.execute('CREATE TABLE %s(SubCat TEXT,PesoIni REAL,PesoFin REAL)'
					%(str(cat+str(self.genero.currentText()))))
				self.datos.commit()
				cur.close()
				self.crearSubCat(str(cat+str(self.genero.currentText())))
			except sqlite3.OperationalError:
				self.datos.commit()
				cur.close()
				self.updateSubCat(str(cat+str(self.genero.currentText())))
	def crearSubCat(self,subCate):
		cur=self.datos.cursor()
		cont=0
		try:
			while self.infUser.item(cont,0).text()!= "":
				subt=str(self.infUser.item(cont,0).text())
				dataSub=[subt.replace(' ',''),
				float(self.infUser.item(cont,1).text()),
				float(self.infUser.item(cont,2).text())]
				cur.execute("INSERT INTO %s VALUES(?,?,?)"%subCate,dataSub)
				self.datos.commit()
				cont+=1
		except AttributeError:
			cur.close()
			self.msg.mensageBueno("<h1>Se termino de GUARDAR</h1>")
	def updateSubCat(self,subCat):
		cur=self.datos.cursor()
		cont=0
		cur.execute("DELETE from %s WHERE PesoFin<=100"%str(subCat))
		try:
			while self.infUser.item(cont,0).text()!= "":
				sbt=str(self.infUser.item(cont,0).text()).replace(' ','')
				dataSub=[sbt,
				float(self.infUser.item(cont,1).text()),
				float(self.infUser.item(cont,2).text())]
				try:
					cur.execute("SELECT SubCat FROM %s WHERE SubCat=:subCa"%subCat,
						{"subCa":str(self.infUser.item(cont,0).text())})
					self.datos.commit()
					row=cur.fetchone()
					if len(row) is not None:
						dataSubm=(float(self.infUser.item(cont,1).text()),
						float(self.infUser.item(cont,2).text()),sbt)
						cur.execute("UPDATE %s SET PesoIni=?,PesoFin=? WHERE SubCat=?"%subCat,dataSubm)
						self.datos.commit()
						cont+=1
				except TypeError:
					cur.execute("INSERT INTO %s VALUES(?,?,?)"%subCat,dataSub)
					self.datos.commit()
					cont+=1
			cur.close()
			self.msg.mensageBueno("<h3>Termino de Guardar</h3>")
		except AttributeError:
			cur.close()
			self.msg.mensageBueno("<h3>Termino de Guardar</h3>")
	def load(self):
		try:
			if self.genH.isChecked():
				self.loadInf("CategoriaH","Hombre")
				self.genero.setCurrentIndex(0)
			elif self.genM.isChecked():
				self.loadInf("CategoriaM","Mujer")
				self.genero.setCurrentIndex(1)
			else:
				self.msg.mensageMalo("<h1>Seleccione un <h3>Genero</h3>\nPara la busqueda</h1>")
		except TypeError:
			self.msg.mensageMalo("<h3>No se encuentra\nregistrado la categoria <h3>")
	def loadInf(self,category,genero):
		nombre=str(self.lineBus.text()).replace(' ','')
		self.lineBus.setText(nombre)
		cur=self.datos.cursor()
		cur.execute("SELECT Categoria FROM %s WHERE Categoria=:cat"%category,
			{"cat":nombre})
		self.datos.commit()
		row=cur.fetchone()
		if len(row) is not None:
			cur.execute("SELECT EdadIni,EdadFin FROM %s WHERE Categoria=:cat"%category,
				{"cat":nombre})
			loadD=cur.fetchone()
			self.categoria.setText(nombre)
			self.edadIni.setValue(int(loadD[0]))
			self.edadMax.setValue(int(loadD[1]))
			cur.execute("SELECT subCat,PesoIni,PesoFin FROM %s"%str(nombre+genero))
			rown=0
			self.infUser.clear()
			for i in cur:
				self.infUser.setItem(rown,0,QTableWidgetItem(i[0]))
				self.infUser.setItem(rown,1,QTableWidgetItem(str(i[1])))
				self.infUser.setItem(rown,2,QTableWidgetItem(str(i[2])))
				rown+=1
			self.infUser.setHorizontalHeaderLabels(['Sub-Categ','Peso-ini','Peso-fin'])
			cur.close()
			self.datos.commit()
	def createTabla(self):
		cur=self.datos.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS CategoriaM(Categoria TEXT,EdadIni INT,EdadFin INT)')
		cur.execute('CREATE TABLE IF NOT EXISTS CategoriaH(Categoria TEXT,EdadIni INT,EdadFin INT)')
		self.datos.commit()
		cur.close()
