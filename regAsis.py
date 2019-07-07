#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR,mesR,Persona
import time

class RegistraAsis(QMdiSubWindow):
	"""Vista para Registro de Estudiante"""
	def __init__(self,arg,dire):
		super(RegistraAsis, self).__init__(arg)
		self.dir=dire
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
		self.tabla.setColumnCount(3)
		self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","Grupo"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		#self.tabla.cellClicked.connect(self.accionTabla)
	def myButton(self):
		self.validar=QPushButton(QIcon("%s/Imagenes/bien.png"%self.dir),"",self)
		self.validar.setIconSize(QSize(60,60))
		self.validar.setObjectName("redondo")
		self.grupo=QComboBox(self)
		self.grupo.addItem("Grupo 1",0)
		self.grupo.addItem("Grupo 2",1)
		self.grupo.addItem("Grupo 3",2)
		self.grupo.addItem("Grupo 4",3)
		self.grupo.setIconSize(QSize(30,30))
		self.botonSave=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.botonSave.setIconSize(QSize(30,30))
		self.botonClear=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.botonClear.setIconSize(QSize(30,30))
		self.botonSalir=QPushButton(QIcon('%s/Imagenes/salir.png'%self.dir),"Salir",self)
		self.botonSalir.setIconSize(QSize(30,30))
	def position(self):
		self.fecha.setGeometry(40,50,300,40)
		self.fotoEl.setGeometry(40,100,300,300)
		self.tabla.setGeometry(360,50,500,500)
		self.validar.setGeometry(50,410,100,100)
		self.grupo.setGeometry(160,410,150,40)
		self.botonSave.setGeometry(50,570,100,40)
		self.botonClear.setGeometry(390,570,100,40)
		self.botonSalir.setGeometry(735,570,100,40)