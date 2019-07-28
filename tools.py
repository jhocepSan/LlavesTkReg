#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,horario,gradoTec

class ToolsClub(QMdiSubWindow):
	"""Vista para Registro de Estudiante"""
	def __init__(self, arg,dire):
		super(ToolsClub, self).__init__(arg)
		self.setGeometry(0,0,885,630)
		self.setWindowTitle("Configuraciones Club")
		self.dir=dire
		with open('%s/css/styleMen.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.horario=horario.HorarioClub(self,self.dir)
		self.grado=gradoTec.GradoTec(self,self.dir)
		#self.mes=mesR.mesR(self,self.dir)
		self.tab=QTabWidget(self)
		self.tab.currentChanged.connect(self.actividad)
		self.tab.addTab(self.horario,QIcon('%s/Imagenes/horario.png'%self.dir),"Horarios")
		self.tab.addTab(self.grado,QIcon('%s/Imagenes/tecnico.png'%self.dir),"Tecnico")
		#self.tab.addTab(self.mes,QIcon('%s/Imagenes/mesI.png'%self.dir),"Mensual")
		self.setWidget(self.tab)
	def actividad(self):
		tab=self.tab.currentIndex()
		if tab==0:
			self.horario.actualizar()
		elif tab==1:
			self.grado.actualizar()