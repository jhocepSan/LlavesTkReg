#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class OptionTabla(QWidget):
	def __init__(self,dire):
		super(OptionTabla, self).__init__()
		self.dir=dire
		self.tipo=''
		self.salioE=False
		self.setGeometry(500,100,120,200)
		self.botones()
		self.setPosition()
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
	def botones(self):
		self.licencia=QPushButton('Licencia',self)
		self.licencia.clicked.connect(lambda:self.operacion('L'))
		self.ingreso=QPushButton('Asistio',self)
		self.ingreso.clicked.connect(lambda:self.operacion('A'))
		self.pagoMes=QPushButton('Mensualidad',self)
		self.pagoMes.clicked.connect(lambda:self.operacion('MES'))
	def setPosition(self):
		self.licencia.setGeometry(10,10,100,40)
		self.ingreso.setGeometry(10,70,100,40)
		self.pagoMes.setGeometry(10,140,100,40)
	def operacion(self,tipo):
		self.tipo=tipo
		self.salioE=True
		self.close()
	def salio(self):
		return self.salioE
	def getTipo(self):
		self.salioE=False
		return self.tipo