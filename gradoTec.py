#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector

class GradoTec(QWidget):
	"""Nomina de estudiantes del club"""
	def __init__(self, arg,dire):
		super(GradoTec, self).__init__(arg)
		self.setGeometry(0,0,885,630)
		self.dir=dire
		self.db=conector.Conector(self.dir)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.myLabel()
		self.myButton()
		self.position()
	def myLabel(self):
		self.titulo=QLabel("<h1>Configuracion de Grados</h1>",self)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(10)
		self.tabla.setColumnCount(3)
		self.tabla.setHorizontalHeaderLabels(["Cinturon","Sigla","Denominacion"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
	def myButton(self):
		self.guardar=QPushButton(QIcon("%s/Imagenes/save.png"%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(30,30))
		self.guardar.clicked.connect(self.save)
		self.limpiar=QPushButton(QIcon("%s/Imagenes/limpiar.png"%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
		self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"",self)
		self.eliminar.setIconSize(QSize(70,70))
		self.eliminar.setObjectName("redondo")
		self.eliminar.clicked.connect(self.borrarBd)
		self.imprimir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),"",self)
		self.imprimir.setIconSize(QSize(70,70))
		self.imprimir.setObjectName("redondo")
	def position(self):
		self.titulo.setGeometry(292,20,300,40)
		self.tabla.setGeometry(50,70,400,300)
		self.guardar.setGeometry(50,500,100,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.eliminar.setGeometry(605,450,100,100)
		self.imprimir.setGeometry(735,450,100,100)
	def save(self):
		pass
	def borrarBd(self):
		pass