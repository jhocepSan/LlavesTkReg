#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import Mensage,conector,pagoMes

class mesR(QWidget):
	"""docstring for mesR"""
	def __init__(self,parent,dire,ide,mdi):
		super(mesR, self).__init__(parent)
		self.setGeometry(0,0,885,630)
		self.dir=dire
		self.persona=ide
		self.mdi=mdi
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.texto()
		self.linText()
		self.botones()
		self.position()
	def texto(self):
		self.ide=QLabel("%s"%self.persona.getId(),self)
		self.mesInil=QLabel("<h1>Fecha Inicio</h1>",self)
		self.gradoInil=QLabel("<h1>Grado Inicial</h1>",self)
		self.clubAnl=QLabel("<h1>Club Anterio</h1>",self)
		self.tipoEsl=QLabel("<h1>Modalidad</h1>",self)
		self.horariol=QLabel("<h1>Horario</h1>",self)
	def botones(self):
		self.save=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.save.clicked.connect(self.guardar)
		self.save.setStatusTip("Guardar la Informacion del Estudiante")
		self.clean=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.clean.clicked.connect(self.limpiar)
		self.clean.setStatusTip("Limpiar los campos de entrada")
		self.salir=QPushButton(QIcon('%s/Imagenes/salir.png'%self.dir),"Salir",self)
		self.imprimir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),'',self)
		self.imprimir.setIconSize(QSize(80,80))
		self.imprimir.setObjectName("redondo")
		self.imprimir.setStatusTip("Imprimir los carnet de los Estudiantes")
		self.irPago=QPushButton(QIcon('%s/Imagenes/pago.png'%self.dir),'',self)
		self.irPago.setIconSize(QSize(80,80))
		self.irPago.setObjectName("redondo")
		self.irPago.setStatusTip("Ir a pago Mensualidad")
		self.irPago.clicked.connect(self.iraPago)
	def linText(self):
		self.mesIni=QDateEdit(self)
		self.gradoIni=QComboBox(self)
		self.clubAn=QLineEdit(self)
		self.clubAn.editingFinished.connect(self.formal)
		self.tipoEs=QComboBox(self)
		self.tipoEs.addItem("Normal")
		self.tipoEs.addItem("Media Veca")
		self.tipoEs.addItem("Vecado")
		self.horario=QComboBox(self)
		self.tablaH=QTableWidget(self)
		self.tablaH.setRowCount(20)
		self.tablaH.setColumnCount(4)
		self.tablaH.setHorizontalHeaderLabels(["Grupo","Instructor","Inicio [24H]","Fin [24H]"])
		self.tablaH.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
	def position(self):
		self.ide.setGeometry(300,50,200,40)
		self.mesInil.setGeometry(50,100,160,40)
		self.gradoInil.setGeometry(50,150,160,40)
		self.clubAnl.setGeometry(50,200,160,40)
		self.tipoEsl.setGeometry(50,250,160,40)
		self.horariol.setGeometry(50,300,160,40)
		self.mesIni.setGeometry(260,100,150,40)
		self.gradoIni.setGeometry(260,150,150,40)
		self.clubAn.setGeometry(260,200,150,40)
		self.tipoEs.setGeometry(260,250,150,40)
		self.horario.setGeometry(260,300,150,40)
		self.tablaH.setGeometry(430,100,400,200)
		self.save.setGeometry(50,500,100,40)
		self.clean.setGeometry(200,500,100,40)
		self.salir.setGeometry(400,500,100,40)
		self.imprimir.setGeometry(580,450,100,100)
		self.irPago.setGeometry(700,450,100,100)
	def guardar(self):
		try:
			dato=[self.ide.text(),self.mesIni.date().toString("d/M/yyyy"),self.gradoIni.currentText(),
			unicode(self.clubAn.text()),self.tipoEs.currentText(),self.horario.currentText()]
			self.db.setDatoMes(dato)
			self.msg.mensageBueno("<h1>Se Guardo los datos Correctamente</h1>")
		except:
			self.msg.mensageMalo("<h1>Error al Guardar</h1>")
	def formal(self):
		self.clubAn.setText(self.clubAn.text().title())
	def limpiar(self):
		self.clubAn.clear()
		self.ide.clear()
	def actualizar(self):
		self.ide.setText(self.persona.getId())
		dato=self.db.getGrado()
		for i in dato:
			self.gradoIni.addItem(i[0])
		dato=self.db.getHorario()
		rown=0
		for i in dato:
			self.tablaH.setItem(rown,0,QTableWidgetItem(str(i[0])))
			self.tablaH.setItem(rown,1,QTableWidgetItem(str(i[1])))
			self.tablaH.setItem(rown,2,QTableWidgetItem(str(i[2])))
			self.tablaH.setItem(rown,3,QTableWidgetItem(i[3]))
			self.horario.addItem(i[0])
			rown+=1
		dato=self.db.getDatoMes(self.persona.getId())
		fecha=dato[1].split('/')
		self.mesIni.setDate(QDate(int(fecha[2]),int(fecha[1]),int(fecha[0])))
		self.gradoIni.setCurrentIndex(self.gradoIni.findText(dato[2]))
		self.clubAn.setText(dato[3])
		self.tipoEs.setCurrentIndex(self.tipoEs.findText(dato[4]))
		self.horario.setCurrentIndex(self.horario.findText(dato[5]))
	def iraPago(self):
		if self.ide.text()!='':
			payMes=pagoMes.MenuPago(self,self.dir)
			self.mdi.addSubWindow(payMes)
			payMes.show()
			payMes.actualizar(self.persona.getId())