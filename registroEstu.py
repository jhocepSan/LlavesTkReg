#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,formR,tecR,mesR,Persona

class RegistraEst(QWidget):
	"""Vista para Registro de Estudiante"""
	def __init__(self, arg,dire):
		super(RegistraEst, self).__init__(arg)
		self.id=Persona.Persona()
		self.setWindowTitle("Registrar Estudiante")
		self.dir=dire
		with open('%s/css/styleMen.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.reg=formR.formR(self,self.dir,self.id)
		self.tec=tecR.tecR(self,self.dir,self.id)
		self.tab=QTabWidget(self)
		self.tab.currentChanged.connect(self.actividad)
		self.tab.addTab(self.reg,QIcon('%s/Imagenes/reg.png'%self.dir),"Datos\nPersonales")
		self.tab.addTab(self.tec,QIcon('%s/Imagenes/tec.png'%self.dir),"Informacion\nAvanzada")
		self.tab.setIconSize(QSize(30,30))
		self.tab.setGeometry(0,0,1333,605)
	def actividad(self):
		tab=self.tab.currentIndex()
		if self.id.getId()!='':
			if tab==1:
				self.tec.actualizar()
			elif tab==2:
				self.mes.actualizar()
		else:
			self.tab.setCurrentIndex(0)