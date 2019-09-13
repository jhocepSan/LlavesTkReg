#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR,mesR,Persona
import time,conector,optionTabla,buscar,Mensage

class RegistraAsis(QWidget):
	"""Vista para Registro de Estudiante"""
	def __init__(self,arg,dire):
		super(RegistraAsis, self).__init__(arg)
		self.diccionario={'Monday':'Lunes','Tuesday':'Martes','Wednesday':'Miercoles',
		'Thursday':'Jueves','Friday':'Viernes','Saturday':'Sabado','Sunday':'Domingo',
		'January':'Enero','February':'Febrero','March':'Marzo','April':'Abril','May':'Mayo',
		'June':'Junio','July':'Julio','August':'Agosto','September':'Septiembre',
		'October':'Octubre','November':'Noviembre','December':'Diciembre'}
		self.dir=dire
		self.msg=Mensage.Msg(self.dir)
		self.db=conector.Conector(self.dir)
		self.option=optionTabla.OptionTabla(self.dir)
		self.timer=QTimer(self)
		self.timer.timeout.connect(self.runOption)
		self.buscare=buscar.buscarEst(self,self.dir)
		self.buscare.mostrar.clicked.connect(self.actualiza)
		self.setGeometry(0,0,1050,670)
		self.setWindowTitle("Control de Asistencia")
		self.myLabel()
		self.myButton()
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.position()
	def myLabel(self):
		self.fecha=QLabel("Fecha - Dia: %s"%time.strftime("%d / %m / %Y"),self);
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
		self.porsentage=QPushButton(QIcon('%s/Imagenes/porsentage.png'%self.dir),"Porsentaje de Asistencia",self)
		self.porsentage.setIconSize(QSize(30,30))
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.botonSave.setIconSize(QSize(30,30))
		self.botonSave.clicked.connect(self.guardar)
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.botonClear.setIconSize(QSize(30,30))
	def activado(self):
		self.fila=self.tabla.currentRow()
		self.timer.start(1000)
		self.option.show()
	def runOption(self):
		if self.option.salio():
			self.tabla.setItem(self.fila , 3,QTableWidgetItem(str(self.option.getTipo())))
			self.tabla.setItem(self.fila , 4,QTableWidgetItem(time.strftime("%Y-%m-%d %H:%M:%S")))
			self.timer.stop()
	def grupoLoad(self):
		self.horas=self.db.getHorario()
		for i in self.horas:
			self.grupo.addItem(str(i[0]))
	def cargaDato(self):
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?","Fecha"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		print self.grupo.currentText()
		info=self.db.getDatoMesH(self.grupo.currentText())
		cont=0
		for i in info:
			self.llenarTabla(cont,i[0])
			cont+=1
	def llenarTabla(self,cont,ide):
		man=self.db.getEstudiant(ide)[0]
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
		self.fecha.setGeometry(10,10,300,40)
		self.validar.setGeometry(330,10,100,100)
		self.grupo.setGeometry(10,70,120,40)
		self.tabla.setGeometry(10,210,1000,400)
		self.buscare.setGeometry(450,10,340,180)
		self.botonSave.setGeometry(810,10,120,40)
		self.botonClear.setGeometry(810,70,120,40)
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
		self.msg.mensageBueno("<h1>Guardado la informacion de Asistencia</h1>")