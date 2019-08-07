#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR,mesR,Persona
import time,conector,optionTabla,buscar

class RegistraAsis(QMdiSubWindow):
	"""Vista para Registro de Estudiante"""
	def __init__(self,arg,dire):
		super(RegistraAsis, self).__init__(arg)
		self.diccionario={'Monday':'Lunes','Tuesday':'Martes','Wednesday':'Miercoles',
		'Thursday':'Jueves','Friday':'Viernes','Saturday':'Sabado','Sunday':'Domingo',
		'January':'Enero','February':'Febrero','March':'Marzo','April':'Abril','May':'Mayo',
		'June':'Junio','July':'Julio','August':'Agosto','September':'Septiembre',
		'October':'Octubre','November':'Noviembre','December':'Diciembre'}
		self.dir=dire
		self.db=conector.Conector(self.dir)
		self.option=optionTabla.OptionTabla(self.dir)
		self.timer=QTimer(self)
		self.timer.timeout.connect(self.runOption)
		self.reloj=QTimer(self)
		self.reloj.timeout.connect(self.actualiza)
		self.reloj.start(1000)
		self.buscare=buscar.buscarEst(self,self.dir)
		self.setGeometry(0,0,1050,670)
		self.setWindowTitle("Control de Asistencia")
		self.myLabel()
		self.myButton()
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.position()
	def myLabel(self):
		self.fecha=QLabel("Fecha - Dia: %s"%time.strftime("%d / %m / %Y"),self)
		self.fotoEl=QLabel("",self)
		self.fotoEl.setObjectName("img")
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(300,300,Qt.KeepAspectRatio))
		self.fotoEl.setAlignment(Qt.AlignCenter);
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(100)
		self.tabla.setColumnCount(5)
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?","Fecha"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.tabla.itemSelectionChanged.connect(self.activado)
	def myButton(self):
		self.validar=QPushButton(QIcon("%s/Imagenes/bien.png"%self.dir),"",self)
		self.validar.setIconSize(QSize(60,60))
		self.validar.setObjectName("redondo")
		self.grupo=QComboBox(self)
		self.grupo.setIconSize(QSize(30,30))
		self.grupoLoad()
		self.grupo.activated.connect(self.cargaDato)
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.botonSave.setIconSize(QSize(30,30))
		self.botonSave.clicked.connect(self.guardar)
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.botonClear.setIconSize(QSize(30,30))
		self.botonSalir=QPushButton(QIcon('%s/Imagenes/salir.png'%self.dir),"Salir",self)
		self.botonSalir.setIconSize(QSize(30,30))
	def activado(self):
		self.fila=self.tabla.currentRow()
		self.timer.start(1000)
		self.option.show()
	def runOption(self):
		if self.option.salio():
			self.tabla.setItem(self.fila , 3,QTableWidgetItem(str(self.option.getTipo())))
			self.timer.stop()
	def grupoLoad(self):
		self.horas=self.db.getHorario()
		for i in self.horas:
			self.grupo.addItem(str(i[0]))
	def cargaDato(self):
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		info=self.db.getDatoMesH(self.grupo.currentText())
		cont=0
		for i in info:
			self.llenarTabla(cont,i[0])
			cont+=1
	def llenarTabla(self,cont,ide):
		man=self.db.getEstudiante(ide)[0]
		self.tabla.setItem(cont , 0,QTableWidgetItem(str(man[0])))
		self.tabla.setItem(cont , 1,QTableWidgetItem(str(man[1])))
		self.tabla.setItem(cont , 2,QTableWidgetItem(str(man[2])))
	def actualiza(self):
		dato=self.buscare.getPersona()
		if len(dato)!=0:
			dato=dato[0]
			fila=0
			while True:
				if self.tabla.item(fila,0)is None:
					self.tabla.setItem(fila,0,QTableWidgetItem(str(dato[0])))
					self.tabla.setItem(fila,1,QTableWidgetItem(str(dato[1])))
					self.tabla.setItem(fila,2,QTableWidgetItem(str(dato[2])))
					self.tabla.setItem(fila,3,QTableWidgetItem(str('A')))
					self.tabla.setItem(fila,4,QTableWidgetItem(time.strftime("%Y-%m-%d %H:%M:%S")))
					break
				if self.tabla.item(fila,0).text()==dato[0]:
					self.tabla.setItem(fila,3,QTableWidgetItem(str('A')))
					self.tabla.setItem(fila,4,QTableWidgetItem(time.strftime("%Y-%m-%d %H:%M:%S")))
					break
				fila+=1
			self.buscare.cleanPersona()
	def position(self):
		self.fecha.setGeometry(40,50,300,40)
		self.fotoEl.setGeometry(40,100,200,200)
		self.validar.setGeometry(260,100,100,100)
		self.grupo.setGeometry(260,220,150,40)
		self.tabla.setGeometry(440,50,550,500)
		self.buscare.setGeometry(40,350,270,130)
		self.botonSave.setGeometry(390,570,100,40)
		self.botonClear.setGeometry(510,570,100,40)
		self.botonSalir.setGeometry(735,570,100,40)
	def guardar(self):
		dia=time.strftime("%A")
		fila=0
		while True:
			if self.tabla.item(fila,0) is None:
				break
			else:
				if self.tabla.item(fila,3) is None:
					self.tabla.setItem(fila,3,QTableWidgetItem(str('F')))
					self.tabla.setItem(fila,4,QTableWidgetItem(time.strftime("%Y-%m-%d %H:%M:%S")))
					dato=[self.tabla.item(fila,0).text(),self.tabla.item(fila,4).text(),
					self.diccionario[dia],self.tabla.item(fila,3).text()]
				else:
					dato=[self.tabla.item(fila,0).text(),self.tabla.item(fila,4).text(),
					self.diccionario[dia],self.tabla.item(fila,3).text()]
				self.db.setAsistencia(dato)
				fila+=1