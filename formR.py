#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class formR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire):
		super(formR, self).__init__(parent)
		self.dir=dire
		self.setGeometry(0,0,885,630)
		self.texto()
		self.inTex()
		self.botones()
		self.position()
	def texto(self):
		self.nombrel=QLabel("Nombre: ",self)
		self.apellidol=QLabel("Apellidos: ",self)
		self.cil=QLabel("CI: ",self)
		self.fechaNl=QLabel("Fecha:\nNacimiento",self)
		self.edadl=QLabel("Edad: ",self)
		self.colegiol=QLabel("Colegio: ",self)
		self.fotoEl=QLabel(self)
		self.title=QLabel("Codigo QR",self)
		self.id=QLabel("ID",self)
		self.qr=QLabel(self)
		self.br=QLabel(self)
	def inTex(self):
		self.nombre=QLineEdit(self)
		self.apellido=QLineEdit(self)
		self.ci=QLineEdit(self)
		self.fechaN=QDateEdit(self)
		self.edad=QSpinBox(self)
		self.colegio=QLineEdit(self)
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Limpiar",self)
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.genQR=QPushButton(QIcon('%s/Imagenes/qr.png'%self.dir),"Generar\nCodigo",self)
	def position(self):
		self.nombrel.setGeometry(50,50,100,40)
		self.nombre.setGeometry(160,50,100,40)
		self.apellidol.setGeometry(50,100,100,40)
		self.apellido.setGeometry(160,100,100,40)
		self.cil.setGeometry(50,150,100,40)
		self.ci.setGeometry(160,150,100,40)
		self.fechaNl.setGeometry(50,200,100,40)
		self.fechaN.setGeometry(160,200,100,40)
		self.edadl.setGeometry(50,250,100,40)
		self.edad.setGeometry(160,250,100,40)
		self.colegiol.setGeometry(50,300,100,40)
		self.colegio.setGeometry(160,300,100,40)
		self.qr.setGeometry(50,350,250,250)
		self.fotoEl.setGeometry(300,50,400,300)
		self.title.setGeometry(310,445,100,40)
		self.id.setGeometry(450,360,100,40)
		self.br.setGeometry(450,410,200,100)
		self.limpiar.setGeometry(720,100,100,40)
		self.guardar.setGeometry(720,150,100,40)
		self.genQR.setGeometry(720,200,100,40)