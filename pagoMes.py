#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,mesEstu,regIngre

class MenuPago(QWidget):
	"""Vista para el registro de mensualidad del club"""
	def __init__(self, arg,dire):
		super(MenuPago, self).__init__(arg)
		self.setWindowTitle("Registrar Mensualidad")
		self.dir=dire
		with open('%s/css/styleMen.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.mesEs=mesEstu.mesEstu(self,self.dir)
		self.regiIng=regIngre.ingresos(self,self.dir)
		self.tab=QTabWidget(self)
		self.tab.addTab(self.mesEs,QIcon('%s/Imagenes/reg.png'%self.dir),"Mensualidad")
		self.tab.addTab(self.regiIng,QIcon('%s/Imagenes/ingreso.png'%self.dir),"Ingresos")
		self.tab.setIconSize(QSize(30,30))
		self.tab.setGeometry(0,0,1333,605)
	def actualizar(self,ide):
		self.mesEs.actualizar(ide);