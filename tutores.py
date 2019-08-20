#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector
class tutorReg(QGroupBox):
	"""docstring for buscarEst"""
	def __init__(self, parent,dire,ide):
		super(tutorReg, self).__init__(parent)
		self.dir=dire
		self.ide=ide
		self.db=conector.Conector(self.dir)
		self.dataTutores=[]
		self.componentes()
		self.position()
		self.setTitle("Tutores")
	def componentes(self):
		self.nombrel=QLabel("Nombre:",self)
		self.nombre=QLineEdit(self)
		self.nombre.editingFinished.connect(self.formalizar)
		self.telefl=QLabel("Telefono:",self)
		self.telef=QLineEdit(self)
		self.agregar=QPushButton(QIcon('%s/Imagenes/agregar.png'%self.dir),'Agregar',self)
		self.agregar.setIconSize(QSize(35,35))
		self.agregar.clicked.connect(self.guardar)
		self.reducir=QPushButton(QIcon('%s/Imagenes/reducir.png'%self.dir),'Eliminar',self)
		self.reducir.setIconSize(QSize(35,35))
		self.reducir.clicked.connect(self.eliminar)
		self.next=QPushButton(QIcon('%s/Imagenes/next.png'%self.dir),'Siquiente',self)
		self.next.setIconSize(QSize(35,35))
		self.next.clicked.connect(self.siquiente)
	def position(self):
		self.nombrel.setGeometry(10,20,100,40)
		self.nombre.setGeometry(120,20,250,40)
		self.telefl.setGeometry(10,70,100,40)
		self.telef.setGeometry(120,70,100,40)
		self.agregar.setGeometry(240,70,130,40)
		self.reducir.setGeometry(100,130,120,40)
		self.next.setGeometry(240,130,130,40)
	def guardar(self):
		dato=[self.ide.getId(),self.nombre.text(),int(self.telef.text())]
		self.db.setTutor(dato)
	def eliminar(self):
		self.db.delTutor([self.ide.getId(),int(self.telef.text())])
	def siquiente(self):
		print self.ide.getId()
	def formalizar(self):
		self.nombre.setText(self.nombre.text().title())
	def viewTutor(self,ide):
		self.dataTutores=self.db.getTutor(ide)
		if len(self.dataTutores)!=0:
			self.nombre.setText(self.dataTutores[0][1])
			self.telef.setText(unicode(self.dataTutores[0][2]))