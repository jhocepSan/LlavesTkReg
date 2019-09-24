#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector
class ingresos(QWidget):
	"""docstring for ingresos"""
	def __init__(self, parent,dire):
		super(ingresos, self).__init__(parent)
		self.dir=dire
		self.setGeometry(0,0,885,630)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.db=conector.Conector(self.dir)
		self.myText()
		self.myEdit()
		self.myButton()
		self.position()
	def myText(self):
		self.titulo=QLabel("<h1>Ingresos Mensuales</h1>",self)
		self.mesl=QLabel("Ingreso Mensual",self)
	def myEdit(self):
		self.mes=QLineEdit(self)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(1)
		self.tabla.setColumnCount(6)
		self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","CI","Grado","Grupo","Monto Bs"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
	def myButton(self):
		self.selectMes=QComboBox(self)
		self.selectMes.activated.connect(self.ingresarMonto)
		self.selectMes.addItem("Enero",0)
		self.selectMes.addItem("Febrero",1)
		self.selectMes.addItem("Marzo",2)
		self.selectMes.addItem("Abril",3)
		self.selectMes.addItem("Mayo",4)
		self.selectMes.addItem("Junio",5)
		self.selectMes.addItem("Julio",6)
		self.selectMes.addItem("Agosto",7)
		self.selectMes.addItem("Septiembre",8)
		self.selectMes.addItem("Actubre",9)
		self.selectMes.addItem("Noviembre",10)
		self.selectMes.addItem("Diciembre",11)
	def position(self):
		self.titulo.setGeometry(292,10,400,60)
		self.selectMes.setGeometry(20,90,150,40)
		self.tabla.setGeometry(20,150,1200,400)
		self.mesl.setGeometry(190,90,150,40)
		self.mes.setGeometry(360,90,150,40)
	def ingresarMonto(self):
		monto=0
		mes=self.selectMes.currentText()
		datos=self.db.getPagoMes(mes)
		fila=0
		for i in datos:
			nombre=self.db.getEstudiant(i[0])[0]
			grado=self.db.getDatosTec(i[0])
			grupo=self.db.getDatoMes(i[0])
			self.tabla.setItem(fila,0,QTableWidgetItem(str(nombre[1])))
			self.tabla.setItem(fila,1,QTableWidgetItem(str(nombre[2])))
			self.tabla.setItem(fila,2,QTableWidgetItem(str(nombre[3])))
			self.tabla.setItem(fila,3,QTableWidgetItem(str(grado[2])))
			self.tabla.setItem(fila,4,QTableWidgetItem(str(grupo[5])))
			self.tabla.setItem(fila,5,QTableWidgetItem(str(i[4])))
			monto+=int(i[4])
			fila+=1
			self.tabla.insertRow(fila)
		self.mes.setText(str(monto)+" Bs")
