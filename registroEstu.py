#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR,mesR,Persona

class RegistraEst(QMdiSubWindow):
	"""Vista para Registro de Estudiante"""
	def __init__(self, arg,dire):
		super(RegistraEst, self).__init__(arg)
		self.id=Persona.Persona()
		self.setGeometry(0,0,885,630)
		self.setWindowTitle("Registrar Estudiante")
		self.dir=dire
		with open('%s/css/styleMen.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.reg=formR.formR(self,self.dir,self.id)
		self.tec=tecR.tecR(self,self.dir,self.id)
		self.mes=mesR.mesR(self,self.dir,self.id)
		self.tab=QTabWidget(self)
		self.tab.addTab(self.reg,QIcon('%s/Imagenes/reg.png'%self.dir),"Personal")
		self.tab.addTab(self.tec,QIcon('%s/Imagenes/tec.png'%self.dir),"Tecnico")
		self.tab.addTab(self.mes,QIcon('%s/Imagenes/mesI.png'%self.dir),"Mensual")
		self.setWidget(self.tab)