#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,horario,gradoTec,club,regIns,modPago

class ToolsClub(QWidget):
	"""Vista para Registro de Estudiante"""
	def __init__(self, arg,dire):
		super(ToolsClub, self).__init__(arg)
		self.setGeometry(0,0,1050,670)
		self.setWindowTitle("Configuraciones Club")
		self.dir=dire
		with open('%s/css/styleMen.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.club=club.Club(self,self.dir)
		self.grado=gradoTec.GradoTec(self,self.dir)
		self.instructo=regIns.RegIns(self,self.dir)
		self.horario=horario.HorarioClub(self,self.dir)
		self.modIns=modPago.ModoPago(self,self.dir)
		#self.mes=mesR.mesR(self,self.dir)
		self.tab=QTabWidget(self)
		self.tab.currentChanged.connect(self.actividad)
		self.tab.addTab(self.club,QIcon('%s/Imagenes/clb.png'%self.dir),"Clubes")
		self.tab.addTab(self.grado,QIcon('%s/Imagenes/tecnico.png'%self.dir),"Grados")
		self.tab.addTab(self.instructo,QIcon('%s/Imagenes/instructor.png'%self.dir),"Instructor")
		self.tab.addTab(self.horario,QIcon('%s/Imagenes/horario.png'%self.dir),"Horarios")
		self.tab.addTab(self.modIns,QIcon('%s/Imagenes/pago.png'%self.dir),'Modo de\nInscripcion')
		self.tab.setIconSize(QSize(40,40))
		#self.tab.addTab(self.mes,QIcon('%s/Imagenes/mesI.png'%self.dir),"Mensual")
		self.tab.setGeometry(0,0,1333,605)
	def actividad(self):
		tab=self.tab.currentIndex()
		if tab==3:
			self.horario.actualizar()
		elif tab==1:
			self.grado.actualizar()
		elif tab==4:
			self.modIns.actualizar()