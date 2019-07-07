#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
class ingresos(QWidget):
	"""docstring for ingresos"""
	def __init__(self, parent,dire):
		super(ingresos, self).__init__(parent)
		self.dir=dire
		self.setGeometry(0,0,885,630)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.myText()
		self.myEdit()
		self.myButton()
		self.position()
	def myText(self):
		self.titulo=QLabel("<h1>Ingresos Mensuales</h1>",self)
		self.mesl=QLabel("<h2>Ingero\nMensual</h2>",self)
		self.totall=QLabel("<h2>Ingreso\nTotal</h2>",self)
	def myEdit(self):
		self.fecha=QDateEdit(QDate(12,4,19),self)
		self.mes=QLineEdit(self)
		self.total=QLineEdit(self)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(100)
		self.tabla.setColumnCount(3)
		self.tabla.setHorizontalHeaderLabels(["CI","Nombre","Monto Bs"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
	def myButton(self):
		self.buscar=QPushButton(QIcon("%s/Imagenes/buscar.png"%self.dir),"Buscar",self)
		self.buscar.setIconSize(QSize(30,30))
		self.limpiar=QPushButton(QIcon("%s/Imagenes/limpiar.png"%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
	def position(self):
		self.titulo.setGeometry(292,30,300,40)
		self.fecha.setGeometry(40,90,100,40)
		self.buscar.setGeometry(160,90,100,40)
		self.limpiar.setGeometry(280,90,100,40)
		self.tabla.setGeometry(40,150,400,400)
		self.mesl.setGeometry(460,150,150,40)
		self.mes.setGeometry(630,150,100,40)
		self.totall.setGeometry(460,210,150,40)
		self.total.setGeometry(630,210,100,40)
