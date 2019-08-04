#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class tutorReg(QGroupBox):
	"""docstring for buscarEst"""
	def __init__(self, parent,dire):
		super(tutorReg, self).__init__(parent)
		self.dir=dire
		self.componentes()
		self.position()
		self.setTitle("Tutores")
	def componentes(self):
		self.nombrel=QLabel("Nombre:",self)
		self.nombre=QLineEdit(self)
		self.telefl=QLabel("Telefono:",self)
		self.telef=QLineEdit(self)
		self.agregar=QPushButton(QIcon('%s/Imagenes/agregar.png'%self.dir),'',self)
		self.reducir=QPushButton(QIcon('%s/Imagenes/reducir.png'%self.dir),'',self)
	def position(self):
		self.nombrel.setGeometry(10,20,100,40)
		self.nombre.setGeometry(120,20,250,40)
		self.telefl.setGeometry(10,70,100,40)
		self.telef.setGeometry(120,70,100,40)
		self.agregar.setGeometry(240,70,40,40)
		self.reducir.setGeometry(300,70,40,40)