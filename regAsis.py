#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR,mesR,Persona
import time,conector,optionTabla

class RegistraAsis(QMdiSubWindow):
	"""Vista para Registro de Estudiante"""
	def __init__(self,arg,dire):
		super(RegistraAsis, self).__init__(arg)
		self.dir=dire
		self.db=conector.Conector(self.dir)
		self.option=optionTabla.OptionTabla(self.dir)
		self.timer=QTimer(self)
		self.timer.timeout.connect(self.runOption)
		self.setGeometry(0,0,885,630)
		self.setWindowTitle("Control de Asistencia")
		self.myLabel()
		self.myButton()
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.position()
	def myLabel(self):
		self.fecha=QLabel("<h2>Fecha - Dia: %s</h2>"%time.strftime("%d / %m / %Y"),self)
		self.fotoEl=QLabel("",self)
		self.fotoEl.setObjectName("img")
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(300,300,Qt.KeepAspectRatio))
		self.fotoEl.setAlignment(Qt.AlignCenter);
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(100)
		self.tabla.setColumnCount(4)
		self.tabla.setHorizontalHeaderLabels(["ID","Nombre","Apellido","Presente?"])
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
		man=self.db.getEstudiante(ide)
		self.tabla.setItem(cont , 0,QTableWidgetItem(str(man[0])))
		self.tabla.setItem(cont , 1,QTableWidgetItem(str(man[1])))
		self.tabla.setItem(cont , 2,QTableWidgetItem(str(man[2])))
	def position(self):
		self.fecha.setGeometry(40,50,300,40)
		self.fotoEl.setGeometry(40,100,300,300)
		self.tabla.setGeometry(360,50,500,500)
		self.validar.setGeometry(50,410,100,100)
		self.grupo.setGeometry(160,410,150,40)
		self.botonSave.setGeometry(50,570,100,40)
		self.botonClear.setGeometry(390,570,100,40)
		self.botonSalir.setGeometry(735,570,100,40)