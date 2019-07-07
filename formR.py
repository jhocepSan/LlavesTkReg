#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import pybase64

class formR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire,ide):
		super(formR, self).__init__(parent)
		self.persona=ide
		self.dir=dire
		self.setGeometry(0,0,885,630)
		with open('%s/css/stylesMenu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
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
		self.fotoEl.setObjectName("img")
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.fotoEl.setAlignment(Qt.AlignCenter);
		self.title=QLabel("Codigo QR",self)
		self.id=QLabel("ID",self)
		self.qr=QLabel(self)
		self.qr.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/qr.png'%self.dir)).scaled(250,200,Qt.KeepAspectRatio))
		self.qr.setObjectName("img")
		self.qr.setAlignment(Qt.AlignCenter);
		self.br=QLabel(self)
		self.br.setObjectName("img")
		self.br.setAlignment(Qt.AlignCenter);
		self.br.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/br.png'%self.dir)).scaled(200,100,Qt.KeepAspectRatio))
	def inTex(self):
		self.nombre=QLineEdit(self)
		self.eh=QCheckBox("Masculino", self)
		self.em=QCheckBox("Femenino",self)
		self.apellido=QLineEdit(self)
		self.ci=QLineEdit(self)
		self.fechaN=QDateEdit(self)
		self.edad=QSpinBox(self)
		self.colegio=QLineEdit(self)
		self.compromiso=QCheckBox("Firma\nDocumento",self)
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Limpiar",self)
		self.limpiar.clicked.connect(self.clear)
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.guardar.clicked.connect(self.save)
		self.genQR=QPushButton(QIcon('%s/Imagenes/qr.png'%self.dir),"Generar\nCodigo",self)
		self.genQR.clicked.connect(self.generarQr)
	def position(self):
		self.nombrel.setGeometry(50,50,100,40)
		self.nombre.setGeometry(160,50,150,40)
		self.apellidol.setGeometry(50,100,100,40)
		self.apellido.setGeometry(160,100,150,40)
		self.cil.setGeometry(50,150,100,40)
		self.ci.setGeometry(160,150,150,40)
		self.fechaNl.setGeometry(50,200,100,40)
		self.fechaN.setGeometry(160,200,150,40)
		self.edadl.setGeometry(50,250,100,40)
		self.edad.setGeometry(160,250,150,40)
		self.colegiol.setGeometry(50,300,100,40)
		self.colegio.setGeometry(160,300,150,40)
		self.qr.setGeometry(50,350,250,200)
		self.fotoEl.setGeometry(320,50,400,300)
		self.title.setGeometry(310,445,100,40)
		self.id.setGeometry(350,360,300,40)
		self.br.setGeometry(450,410,200,100)
		self.compromiso.setGeometry(670,410,200,70)
		self.eh.setGeometry(740,100,100,40)
		self.em.setGeometry(740,150,100,40)
		self.limpiar.setGeometry(740,200,100,40)
		self.guardar.setGeometry(740,250,100,40)
		self.genQR.setGeometry(740,300,100,40)
	def clear(self):
		self.nombre.clear()
		self.apellido.clear()
		self.ci.clear()
		self.fechaN.clear()
		self.edad.clear()
		self.colegio.clear()
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.qr.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/qr.png'%self.dir)).scaled(250,200,Qt.KeepAspectRatio))
		self.br.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/br.png'%self.dir)).scaled(200,100,Qt.KeepAspectRatio))
	def save(self):
		info=[unicode(self.nombre.text()),unicode(self.apellido.text()),
			self.ci.text(),self.fechaN.date(),self.edad.value(),
			unicode(self.colegio.text())]
		self.persona.setId(unicode(self.nombre.text()))
		print self.fechaN.date().day()
	def generarQr(self):
		codigo=pybase64.b64encode(' '.join(format(ord(x), 'b') for x in self.ci.text()))
		self.id.setText(codigo)
		print pybase64.b64decode(codigo)