#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import Mensage,conector
class tecR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire,ide):
		super(tecR, self).__init__(parent)
		self.persona=ide
		self.dir=dire
		self.setGeometry(0,0,885,630)
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		with open('%s/css/stylesMenu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
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
		self.club=QComboBox(self)
		self.club.setIconSize(QSize(30,30))
		self.grado=QComboBox(self)
		self.grado.setIconSize(QSize(30,30))
		self.altura=QDoubleSpinBox(self)
		self.altura.setSuffix("  [m]")
		self.altura.setSingleStep(0.01)
		self.peso=QDoubleSpinBox(self)
		self.peso.setSuffix(" [Kgr]")
		self.peso.setSingleStep(0.01)
		self.phone=QLineEdit(self)
		self.tutor=QLineEdit(self)
		self.tutor.editingFinished.connect(lambda:self.formalizar(self.tutor))
		self.phonet=QLineEdit(self)
		self.home=QLineEdit(self)
		self.home.editingFinished.connect(lambda:self.formalizar(self.home))
		self.sangre=QComboBox(self)
		self.sangre.setIconSize(QSize(30,30))
		self.sangre.addItem(QIcon("%s/Imagenes/op.png"%self.dir),"O+")
		self.sangre.addItem(QIcon("%s/Imagenes/on.png"%self.dir),"O-")
		self.sangre.addItem(QIcon("%s/Imagenes/ap.png"%self.dir),"A+")
		self.sangre.addItem(QIcon("%s/Imagenes/an.png"%self.dir),"A-")
		self.sangre.addItem(QIcon("%s/Imagenes/bp.png"%self.dir),"B+")
		self.sangre.addItem(QIcon("%s/Imagenes/bn.png"%self.dir),"B-")
		self.sangre.addItem(QIcon("%s/Imagenes/abp.png"%self.dir),"AB+")
		self.sangre.addItem(QIcon("%s/Imagenes/abn.png"%self.dir),"AB-")
		self.alergia=QLineEdit(self)
	def formalizar(self,elem):
		elem.setText(elem.text().title())
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(40,40))
		self.limpiar.clicked.connect(self.clear)
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(40,40))
		self.guardar.clicked.connect(self.save)
		self.imgC=QPushButton(QIcon('%s/Imagenes/img.png'%self.dir),"",self)
		self.imgC.setIconSize(QSize(80,80))
		self.imgC.setObjectName("redondo")
	def position(self):
		self.ide.setGeometry(300,30,200,40)
		self.clubl.setGeometry(50,80,100,40)
		self.gradoL.setGeometry(50,130,100,40)
		self.alturaL.setGeometry(50,180,100,40)
		self.pesol.setGeometry(50,230,100,40)
		self.phoneL.setGeometry(50,280,100,40)
		self.tutorl.setGeometry(50,330,100,40)
		self.phonetl.setGeometry(50,380,100,40)
		self.homeL.setGeometry(50,430,100,40)
		self.fotoC.setGeometry(340,80,400,300)
		self.sangrel.setGeometry(400,390,100,40)
		self.sangre.setGeometry(520,390,100,30)
		self.alergial.setGeometry(400,430,100,40)
		self.alergia.setGeometry(520,430,100,30)
		self.club.setGeometry(160,80,150,40)
		self.grado.setGeometry(160,130,150,40)
		self.altura.setGeometry(160,180,150,40)
		self.peso.setGeometry(160,230,150,40)
		self.phone.setGeometry(160,280,150,40)
		self.tutor.setGeometry(160,330,150,40)
		self.phonet.setGeometry(160,380,150,40)
		self.home.setGeometry(160,430,200,40)
		self.guardar.setGeometry(50,500,100,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.imgC.setGeometry(735,450,100,100)
	def save(self):
		try:
			datos=[self.ide.text(),unicode(self.club.currentText()),self.grado.currentText(),
			self.altura.value(),self.peso.value(),int(self.phone.text()),unicode(self.tutor.text()),
			int(self.phonet.text()),unicode(self.home.text()),self.sangre.currentText(),unicode(self.alergia.text())]
			self.db.setDatoTec(datos)
			self.msg.mensageBueno("<h1>Datos Guardados Correctamente</h1>")
		except:
			self.msg.mensageMalo("<h1>Error Al Guardar</h1>")
	def clear(self):
		self.peso.clear()
		self.altura.clear()
		self.home.clear()
		self.phone.clear()
		self.tutor.clear()
		self.phonet.clear()
		self.alergia.clear()
	def actualizar(self):
		self.ide.setText(self.persona.getId())
		datos=self.db.getClub()
		self.club.addItem(QIcon(datos[2]),datos[0])
		self.fotoC.setPixmap(QPixmap.fromImage(QImage(datos[2])).scaled(400,300,Qt.KeepAspectRatio))
		grado=self.db.getGrado()
		for i in grado:
			self.grado.addItem(i[0])
		info=self.db.getDatosTec(self.persona.getId())
		if len(info) is not None:
			self.altura.setValue(info[3])
			self.peso.setValue(info[4])
			self.phone.setText(unicode(info[5]))
			self.tutor.setText(info[6])
			self.phonet.setText(unicode(info[7]))
			self.home.setText(info[8])
			self.alergia.setText(info[10])