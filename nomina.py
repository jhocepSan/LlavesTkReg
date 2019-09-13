#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector,Mensage

class ListaEstu(QWidget):
	"""Nomina de estudiantes del club"""
	def __init__(self, arg,dire):
		super(ListaEstu, self).__init__(arg)
		self.setGeometry(0,0,1050,670)
		self.setWindowTitle("Lista de Estudiantes")
		self.dir=dire
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		self.myLista()
		self.myButon()
		self.position()
	def myLista(self):
		self.genero=QComboBox(self)
		self.genero.addItem('Varon')
		self.genero.addItem('Mujer')
		self.genero.activated.connect(self.llenarTabla)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(1000)
		self.tabla.setColumnCount(5)
		self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","Grado","Carnet\nIdentidad","Identificador"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		#self.tabla.itemSelectionChanged.connect(self.activado)
	def myButon(self):
		self.imprimir=QPushButton(QIcon('%s/Imagenes/pdf.png'%self.dir),'Imprimir',self)
		self.imprimir.setIconSize(QSize(30,30))
		self.salir=QPushButton(QIcon('%s/Imagenes/salir.png'%self.dir),'Salir',self)
		self.salir.setIconSize(QSize(30,30))
		self.salir.clicked.connect(self.salirNomina)
	def position(self):
		self.tabla.setGeometry(30,60,880,580)
		self.genero.setGeometry(920,60,100,40)
		self.imprimir.setGeometry(920,540,110,40)
		self.salir.setGeometry(920,600,110,40)
	def salirNomina(self):
		self.close()
	def llenarTabla(self):
		self.limpiarTabla()
		estudiantes=self.db.getAllEstudent(str(self.genero.currentText()))
		fila=0
		for d in estudiantes:
			self.tabla.setItem(fila,0,QTableWidgetItem(unicode(d[1])))
			self.tabla.setItem(fila,1,QTableWidgetItem(unicode(d[2])))
			self.tabla.setItem(fila,3,QTableWidgetItem(unicode(d[3])))
			self.tabla.setItem(fila,4,QTableWidgetItem(unicode(d[0])))
			grado=self.db.getDatosTec(d[0])
			self.tabla.setItem(fila,2,QTableWidgetItem(grado[2]))
			fila+=1
	def limpiarTabla(self):
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","Grado","Carnet\nIdentidad","Identificador"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)