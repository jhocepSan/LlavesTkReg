#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR

class RegistraEst(QMdiSubWindow):
	"""Vista para Registro de Estudiante"""
	def __init__(self, arg,dire):
		super(RegistraEst, self).__init__(arg)
		self.setGeometry(0,0,885,630)
		self.setWindowTitle("Registrar Estudiante")
		self.dir=dire
		self.reg=formR.formR(self,self.dir)
		self.tec=tecR.tecR(self,self.dir)
		self.tab=QTabWidget(self)
		self.tab.addTab(self.reg,QIcon('%s/Imagenes/reg.png'%self.dir),"Personal")
		self.tab.addTab(self.tec,QIcon('%s/Imagenes/tec.png'%self.dir),"Tecnico")
		self.setWidget(self.tab)