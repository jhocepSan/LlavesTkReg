#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector,os,Mensage,shutil
import os.path as path

class HorarioClub(QWidget):
	"""Nomina de estudiantes del club"""
	def __init__(self, arg,dire):
		super(HorarioClub, self).__init__(arg)
		self.dir=dire
		self.msges=Mensage.Msg(self.dir)
		self.db=conector.Conector(self.dir)
		self.dirImg=""
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.myLabel()
		self.myButton()
		self.agregarOption()
		self.actualizar()
		self.position()
	def myLabel(self):
		self.titulo=QLabel("Horarios del Club",self)
		self.horaInil=QLabel("Hora Inicio",self)
		self.horaIni=QTimeEdit(self)
		self.horaIni.setDisplayFormat("HH:mm")
		self.horaFin=QTimeEdit(self)
		self.horaFinl=QLabel("Hora Fin",self)
		self.horaFin.setDisplayFormat("HH:mm")
		self.clubl=QLabel("Club",self)
		self.club=QComboBox(self)
		self.insL=QLabel('Instructor',self)
		self.ins=QComboBox(self)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(20)
		self.tabla.setColumnCount(11)
		self.tabla.setHorizontalHeaderLabels(["Grupo","Instructor","Inicio","Fin","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.tabla.itemSelectionChanged.connect(self.activado)
		self.imgClb=QLabel(self)
		self.imgClb.setObjectName("img")
		img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(100,100,Qt.KeepAspectRatio)
		self.imgClb.setPixmap(img)
		self.imgClb.setAlignment(Qt.AlignCenter)
	def activado(self):
		fila=self.tabla.currentRow()
		if self.tabla.item(fila,0) is not None:
			for i in [4,5,6,7,8,9,10]:
				self.tabla.setItem(fila , i,QTableWidgetItem('n'))
	def myButton(self):
		self.agregar=QPushButton(QIcon("%s/Imagenes/agregar.png"%self.dir),"Agregar",self)
		self.agregar.setIconSize(QSize(30,30))
		self.agregar.clicked.connect(self.agregarHora)
		self.guardar=QPushButton(QIcon("%s/Imagenes/save.png"%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(30,30))
		self.guardar.clicked.connect(self.save)
		self.limpiar=QPushButton(QIcon("%s/Imagenes/limpiar.png"%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
		self.limpiar.clicked.connect(self.limpiarI)
		self.imprimir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),"",self)
		self.imprimir.setIconSize(QSize(70,70))
		self.imprimir.setObjectName("redondo")
		self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Eliminar",self)
		self.eliminar.setIconSize(QSize(30,30))
		self.eliminar.clicked.connect(self.borrarBd)
	def agregarHora(self):
		fila=0
		while self.tabla.item(fila,0) is not None:
			fila+=1
		self.tabla.setItem(fila,0,QTableWidgetItem('Grupo %d'%fila))
		self.tabla.setItem(fila,1,QTableWidgetItem(self.ins.currentText()))
		self.tabla.setItem(fila,2,QTableWidgetItem(self.horaIni.time().toString('HH:mm')))
		self.tabla.setItem(fila,3,QTableWidgetItem(self.horaFin.time().toString('HH:mm')))
	def position(self):
		self.titulo.setGeometry(292,30,300,40)
		self.tabla.setGeometry(50,90,600,400)
		self.clubl.setGeometry(670,30,60,40)
		self.club.setGeometry(750,30,150,40)
		self.imgClb.setGeometry(700,90,100,100)
		self.horaInil.setGeometry(670,210,100,40)
		self.horaIni.setGeometry(790,210,100,40)
		self.horaFinl.setGeometry(670,270,100,40)
		self.horaFin.setGeometry(790,270,100,40)
		self.insL.setGeometry(670,330,100,40)
		self.ins.setGeometry(790,330,100,40)
		self.agregar.setGeometry(670,390,100,40)
		self.guardar.setGeometry(50,500,100,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.eliminar.setGeometry(625,500,100,40)
		self.imprimir.setGeometry(735,450,100,100)
	def agregarOption(self):
		club=self.db.getClub()
		for i in club:
			if self.club.findText(i[0])<0:
				self.club.addItem(i[0])
		instructor=self.db.getInstructor()
		for i in instructor:
			if self.ins.findText(i[1])<0:
				self.ins.addItem(i[1])
	def save(self):
		self.db.delHorario()
		cont=0
		try:
			while self.tabla.item(cont,0)is not None:
				dias=str(self.buscarDias(cont))
				dataHor=[str(self.tabla.item(cont,0).text()).replace(' ',''),
				str(self.tabla.item(cont,1).text()).title(),
				str(self.tabla.item(cont,2).text()).replace(' ',''),
				str(self.tabla.item(cont,3).text()).replace(' ',''),dias]
				self.db.setHorario(dataHor)
				cont+=1
			self.msges.mensageBueno("<h1>Se guardo Correctamente</h1>")
		except:
			self.msges.mensageMalo("<h1>Un Problema al guardar La información</h1>")
	def buscarDias(self,cont):
		diaT=""
		dia=4
		for i in ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]:
			d=self.tabla.item(cont,dia).text().replace(' ','')
			if d=='y'or d=='Y':
				diaT+="%s,"%i
			dia+=1
		return diaT[:len(diaT)-1]
	def limpiarI(self):
		img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
		self.imgClb.setPixmap(img)
		self.imgClb.setAlignment(Qt.AlignCenter)
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["Grupo","Instructor","Inicio","Fina","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.dirImg=""
	def actualizar(self):
		datos=self.db.getHorario()
		cont=0
		for i in datos:
			self.tabla.setItem(cont , 0,QTableWidgetItem(str(i[0])))
			self.tabla.setItem(cont , 1,QTableWidgetItem(str(i[1])))
			self.tabla.setItem(cont , 2,QTableWidgetItem(str(i[2])))
			self.tabla.setItem(cont , 3,QTableWidgetItem(str(i[3])))
			self.cargarDia(cont,i[4])
			cont+=1
	def cargarDia(self,fila,dato):
		dia=4;
		for i in ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]:
			if dato.find(i)>=0:
				self.tabla.setItem(fila , dia,QTableWidgetItem('y'))
			else:
				self.tabla.setItem(fila , dia,QTableWidgetItem('n'))
			dia+=1
	def borrarBd(self):
		try:
			self.db.delHorario()
			self.msges.mensageBueno("<h1>Eliminado Correctamente</h1>")
		except:
			self.msges.mensageMalo("<h1>No se Pudo Eliminar los Dato</h1>")