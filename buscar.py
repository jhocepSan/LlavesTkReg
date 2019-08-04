#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class buscarEst(QGroupBox):
	"""docstring for buscarEst"""
	def __init__(self, parent):
		super(buscarEst, self).__init__(parent)
		self.componentes()
		self.position()
		self.setTitle("Buscar")
	def componentes(self):
		self.buscar=QLineEdit(self)
		self.id=QCheckBox("ID",self)
		self.ci=QCheckBox("CI",self)
		self.name=QCheckBox("Nombre",self)
		self.selection=QPushButton('hola',self)
	def position(self):
		self.buscar.setGeometry(10,20,200,40)
		self.id.setGeometry(10,70,60,40)
		self.ci.setGeometry(90,70,60,40)
		self.name.setGeometry(160,70,60,40)
		self.selection.setGeometry(240,70,60,40)