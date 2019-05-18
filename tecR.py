#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class tecR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire):
		super(tecR, self).__init__(parent)
		self.dir=dire
		self.setGeometry(0,0,885,630)
		self.setStyleSheet("background-color: green; color: white;")
		self.texto()
		self.line()
		self.botones()
		self.position()
	def texto(self):
		self.clubl=QLabel("Club:",self)
		self.gradoL=QLabel("Grado:",self)
		self.alturaL=QLabel("Altura:",self)
		self.pesol=QLabel("Peso:",self)
		self.phoneL=QLabel("Telefono:",self)
		self.homeL=QLabel("Domicilio:",self)
		self.tutorl=QLabel("Tutor:",self)
		self.phonetl=QLabel("Telefono:\nTutor",self)
		self.sangrel=QLabel("Sangre:",self)
		self.fotoC=QLabel(self)
	def line(self):
		self.club=QLineEdit(self)
		self.grado=QLineEdit(self)
		self.altura=QLineEdit(self)
		self.peso=QSpinBox(self)
		self.phone=QLineEdit(self)
		self.tutor=QLineEdit(self)
		self.phonet=QLineEdit(self)
		self.home=QLineEdit(self)
		self.sangre=QLineEdit(self)
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Limpiar",self)
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.imgC=QPushButton(QIcon('%s/Imagenes/img.png'%self.dir),"Imagen\nClub",self)
	def position(self):
		self.clubl.setGeometry(50,50,100,40)
		self.gradoL.setGeometry(50,100,100,40)
		self.alturaL.setGeometry(50,150,100,40)
		self.pesol.setGeometry(50,200,100,40)
		self.phoneL.setGeometry(50,250,100,40)
		self.tutorl.setGeometry(50,300,100,40)
		self.phonetl.setGeometry(50,350,100,40)
		self.homeL.setGeometry(50,400,100,40)
		self.fotoC.setGeometry(300,50,400,300)
		self.sangrel.setGeometry(300,360,100,40)
		self.sangre.setGeometry(410,360,100,40)
		self.club.setGeometry(160,50,100,40)
		self.grado.setGeometry(160,100,100,40)
		self.altura.setGeometry(160,150,100,40)
		self.peso.setGeometry(160,200,100,40)
		self.phone.setGeometry(160,250,100,40)
		self.tutor.setGeometry(160,300,100,40)
		self.phonet.setGeometry(160,350,100,40)
		self.home.setGeometry(160,400,200,40)
		self.limpiar.setGeometry(50,500,100,40)
		self.guardar.setGeometry(200,500,100,40)
		self.imgC.setGeometry(450,500,100,40)