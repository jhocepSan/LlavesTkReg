#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class mesR(QWidget):
	"""docstring for mesR"""
	def __init__(self,parent,dire,ide):
		super(mesR, self).__init__(parent)
		self.dir=dire
		self.persona=ide
		with open('%s/css/stylesMenu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.texto()
		self.linText()
		self.botones()
		self.position()
	def texto(self):
		self.ide=QLabel("%s"%self.persona.getId(),self)
		self.mesInil=QLabel("Fecha Inicio",self)
		self.gradoInil=QLabel("Grado Inicial",self)
		self.clubAnl=QLabel("Club Anterio",self)
		self.tipoEsl=QLabel("Modalidad",self)
		self.horariol=QLabel("Horario",self)
	def botones(self):
		self.save=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.clean=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.salir=QPushButton(QIcon('%s/Imagenes/salir.png'%self.dir),"Salir",self)
	def linText(self):
		self.mesIni=QDateEdit(self)
		self.gradoIni=QLineEdit(self)
		self.clubAn=QLineEdit(self)
		self.tipoEs=QComboBox(self)
		self.horario=QLineEdit(self)
	def position(self):
		self.ide.setGeometry(300,50,200,40)
		self.mesInil.setGeometry(50,100,150,40)
		self.gradoInil.setGeometry(50,150,150,40)
		self.clubAnl.setGeometry(50,200,150,40)
		self.tipoEsl.setGeometry(50,250,150,40)
		self.horariol.setGeometry(50,300,150,40)
		self.mesIni.setGeometry(260,100,150,40)
		self.gradoIni.setGeometry(260,150,150,40)
		self.clubAn.setGeometry(260,200,150,40)
		self.tipoEs.setGeometry(260,250,150,40)
		self.horario.setGeometry(260,300,150,40)
		self.save.setGeometry(50,500,100,40)
		self.clean.setGeometry(200,500,100,40)
		self.salir.setGeometry(400,500,100,40)
	def actualizar(self):
		self.ide.setText(self.persona.getId())