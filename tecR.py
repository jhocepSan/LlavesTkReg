#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class tecR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire,ide):
		super(tecR, self).__init__(parent)
		self.persona=ide
		self.dir=dire
		self.setGeometry(0,0,885,630)
		with open('%s/css/stylesMenu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		#self.setStyleSheet("background-color: green; color: white;")
		self.texto()
		self.line()
		self.botones()
		self.position()
	def texto(self):
		self.ide=QLabel("%s"%self.persona.getId(),self)
		self.clubl=QLabel("Club:",self)
		self.gradoL=QLabel("Grado:",self)
		self.alturaL=QLabel("Altura:",self)
		self.pesol=QLabel("Peso:",self)
		self.phoneL=QLabel("Telefono:",self)
		self.homeL=QLabel("Domicilio:",self)
		self.tutorl=QLabel("Tutor:",self)
		self.phonetl=QLabel("Telefono:\nTutor",self)
		self.sangrel=QLabel("Sangre:",self)
		self.alergial=QLabel("Alergia:",self)
		self.fotoC=QLabel(self)
		self.fotoC.setObjectName("img")
		self.fotoC.setAlignment(Qt.AlignCenter);
		self.fotoC.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
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
		self.alergia=QLineEdit(self)
	def botones(self):
		self.timer=QTimer(self)
		self.timer.start(1000)
		self.timer.timeout.connect(self.actualizar)
		self.limpiar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Limpiar",self)
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.imgC=QPushButton(QIcon('%s/Imagenes/img.png'%self.dir),"Imagen\nClub",self)
	def actualizar(self):
		self.ide.setText(self.persona.getId())
		print self.persona.getId()
	def position(self):
		self.ide.setGeometry(340,50,100,40)
		self.clubl.setGeometry(50,100,100,40)
		self.gradoL.setGeometry(50,150,100,40)
		self.alturaL.setGeometry(50,200,100,40)
		self.pesol.setGeometry(50,250,100,40)
		self.phoneL.setGeometry(50,300,100,40)
		self.tutorl.setGeometry(50,350,100,40)
		self.phonetl.setGeometry(50,400,100,40)
		self.homeL.setGeometry(50,450,100,40)
		self.fotoC.setGeometry(340,100,400,300)
		self.sangrel.setGeometry(400,410,100,40)
		self.sangre.setGeometry(520,410,100,40)
		self.alergial.setGeometry(400,450,100,40)
		self.alergia.setGeometry(520,450,100,40)
		self.club.setGeometry(160,100,150,40)
		self.grado.setGeometry(160,150,150,40)
		self.altura.setGeometry(160,200,150,40)
		self.peso.setGeometry(160,250,150,40)
		self.phone.setGeometry(160,300,150,40)
		self.tutor.setGeometry(160,350,150,40)
		self.phonet.setGeometry(160,400,150,40)
		self.home.setGeometry(160,450,200,40)
		self.limpiar.setGeometry(50,500,100,40)
		self.guardar.setGeometry(200,500,100,40)
		self.imgC.setGeometry(450,500,100,40)