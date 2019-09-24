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
		self.fecha=QLabel("Fecha - Dia: %s"%time.strftime("%d-%m-%Y"),self);
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(100)
		self.tabla.setColumnCount(5)
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?","Fecha"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.tabla.itemSelectionChanged.connect(self.activado)
		self.tabla.itemDoubleClicked.connect(self.asistenciaOn)
		self.numDia=QLabel("",self)
		self.activarLicencia=QCheckBox("Activar\nLicencia",self)
	def asistenciaOn(self):
		fila=self.tabla.currentRow()
		if self.tabla.item(fila,0) is not None:
			if self.activarLicencia.isChecked():
				self.tabla.setItem(fila , 3,QTableWidgetItem('L'))
			else:
				self.tabla.setItem(fila , 3,QTableWidgetItem('A'))
			self.tabla.setItem(fila , 4,QTableWidgetItem(time.strftime("%Y-%m-%d %H:%M:%S")))
	def myButton(self):
		self.validar=QPushButton(QIcon("%s/Imagenes/bien.png"%self.dir),"",self)
		self.validar.setIconSize(QSize(60,60))
		self.validar.setObjectName("redondo")
		self.grupo=QComboBox(self)
		self.grupo.setIconSize(QSize(30,30))
		self.grupoLoad()
		self.grupo.activated.connect(self.cargaDato)
		self.porsentage=QPushButton(QIcon('%s/Imagenes/porsentage.png'%self.dir),"Porsentaje de\nAsistencia",self)
		self.porsentage.setIconSize(QSize(30,30))
		self.porsentage.clicked.connect(self.mostrarPorsentaje)
		self.actividad=QPushButton(QIcon('%s/Imagenes/lista.png'%self.dir),"Mostrar\nNormal",self)
		self.actividad.setIconSize(QSize(30,30))
		self.actividad.clicked.connect(self.quitarPorsentaje)
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.botonSave.setIconSize(QSize(30,30))
		self.botonSave.clicked.connect(self.guardar)
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.botonClear.setIconSize(QSize(30,30))
		self.resagados=QPushButton(QIcon('%s/Imagenes/rezagados.png'%self.dir),"Lista de\nRezagados",self)
		self.resagados.setIconSize(QSize(30,30))
	def activado(self):
		self.fila=self.tabla.currentRow()
		self.option.show()
	def grupoLoad(self):
		self.horas=self.db.getHorario()
		for i in self.horas:
			self.grupo.addItem(str(i[0]))
	def cargaDato(self):
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?","Fecha"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		grupo=self.grupo.currentText()
		ndia=self.db.getHorarioG(grupo)
		print ndia
		if ndia is not None:
			self.numDia.setText(str(len(ndia[4].split(','))))
		info=self.db.getDatoMesH(grupo)
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
		self.activarLicencia.setGeometry(10,130,120,60)
		self.numDia.setGeometry(130,70,50,40)
		self.tabla.setGeometry(10,210,1300,390)
		self.buscare.setGeometry(450,10,340,180)
		self.porsentage.setGeometry(810,20,150,60)
		self.actividad.setGeometry(810,100,150,60)
		self.resagados.setGeometry(980,20,150,60)
		self.botonSave.setGeometry(1150,20,120,60)
		self.botonClear.setGeometry(1150,100,120,60)
	def guardar(self):
		if not self.db.exiteAsistencia(self.grupo.currentText(),time.strftime("%Y-%m-%d")):
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
						self.grupo.currentText(),time.strftime("%Y-%m-%d"),
						self.diccionario[dia],self.tabla.item(fila,3).text()]
					else:
						dato=[self.tabla.item(fila,0).text(),self.tabla.item(fila,4).text(),
						self.grupo.currentText(),time.strftime("%Y-%m-%d"),
						self.diccionario[dia],self.tabla.item(fila,3).text()]
					self.db.setAsistencia(dato)
					fila+=1
			self.msg.mensageBueno("<h1>Guardado la informacion de Asistencia</h1>")
		else:
			self.msg.mensageBueno("<h1>Ya fue guardado las asistencias\ndel dia%s</h1>"%time.strftime("%Y-%m-%d"))
	def mostrarPorsentaje(self):
		self.tabla.setColumnCount(6)
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?","Fecha","Porcentaje\nAsistencia"])
		fila=0
		while True:
			if self.tabla.item(fila,0) is None:
				break
			else:
				porsentaje=(len(self.db.getAsistenciaId(self.tabla.item(fila,0).text()))*100)/(int(self.numDia.text())*4)
				self.tabla.setItem(fila,5,QTableWidgetItem(str('%i'%porsentaje)))
				fila+=1
	def quitarPorsentaje(self):
		self.tabla.setColumnCount(5)
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?","Fecha"])