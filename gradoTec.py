#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector,Mensage

class GradoTec(QWidget):
	"""Nomina de estudiantes del club"""
	def __init__(self, arg,dire):
		super(GradoTec, self).__init__(arg)
		self.setGeometry(0,0,885,630)
		self.dir=dire
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.myLabel()
		self.myButton()
		self.position()
	def myLabel(self):
		self.titulo=QLabel("Configuracion de Grados",self)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(30)
		self.tabla.setColumnCount(3)
		self.tabla.setHorizontalHeaderLabels(["Cinturon","Sigla","Denominacion"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
	def myButton(self):
		self.guardar=QPushButton(QIcon("%s/Imagenes/save.png"%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(30,30))
		self.guardar.clicked.connect(self.save)
		self.limpiar=QPushButton(QIcon("%s/Imagenes/limpiar.png"%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
		self.limpiar.clicked.connect(self.clear)
		self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Eliminar",self)
		self.eliminar.setIconSize(QSize(30,30))
		self.eliminar.clicked.connect(self.borrarBd)
		self.imprimir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),"",self)
		self.imprimir.setIconSize(QSize(70,70))
		self.imprimir.setObjectName("redondo")
	def position(self):
		self.titulo.setGeometry(292,20,300,40)
		self.tabla.setGeometry(50,70,400,400)
		self.guardar.setGeometry(50,500,100,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.eliminar.setGeometry(605,500,100,40)
		self.imprimir.setGeometry(735,450,100,100)
	def save(self):
		try:
			cont=0
			self.db.delGrado()
			while self.tabla.item(cont,0)is not None:
				datos=[str(self.tabla.item(cont,0).text()).title().replace(' ',''),
				str(self.tabla.item(cont,1).text()).upper().replace(' ',''),
				str(self.tabla.item(cont,2).text()).title().replace(' ','')]
				self.db.setGrado(datos)
				cont+=1
			self.msg.mensageBueno("<h1>Datos Guardados Correctamente</h1>")
		except:
			self.msg.mensageMalo("<h1>Error al Guardar Informacion</h1>")
	def borrarBd(self):
		try:
			self.db.delGrado()
			self.msg.mensageBueno("<h1>Borrado Correctamente</h1>")
		except:
			self.msg.mensageMalo("<h1>Error al Borrar</h1>")
	def actualizar(self):
		datos=self.db.getGrado()
		cont=0
		for i in datos:
			self.tabla.setItem(cont , 0,QTableWidgetItem(str(i[0])))
			self.tabla.setItem(cont , 1,QTableWidgetItem(str(i[1])))
			self.tabla.setItem(cont , 2,QTableWidgetItem(str(i[2])))
			cont+=1
	def clear(self):
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["Cinturon","Sigla","Denominacion"])
