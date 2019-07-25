#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import time
import Mensage,conector
class mesEstu(QWidget):
	"""Vista de pago mensualidad estudiante"""
	def __init__(self,parent,dire):
		super(mesEstu, self).__init__(parent)
		self.dir=dire
		self.setGeometry(0,0,885,630)
		self.msg=Mensage.Msg(self.dir)
		self.db=conector.Conector(self.dir)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.texto()
		self.myLine()
		self.botones()
		self.position()
	def texto(self):
		self.nombrel=QLabel("<h2>Nombre: </h2>",self)
		self.nombre=QLabel('',self)
		self.apellidol=QLabel("<h2>Apellidos: </h2>",self)
		self.apellido=QLabel('',self)
		self.mesPayl=QLabel("<h2>Mensualidad: </h2>",self)
		self.montoL=QLabel("<h2>Pago: </h2>",self)
		self.nomPagol=QLabel("<h2>Tutor: </h2>",self)
		self.fechal=QLabel("<h2>Fecha: </h2>",self)
		self.fotoEl=QLabel(self)
		self.fotoEl.setObjectName("img")
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.fotoEl.setAlignment(Qt.AlignCenter);
		self.conteOption=QGridLayout()
	def myLine(self):
		self.mesPay=QComboBox(self)
		self.mesPay.addItem("Enero",0)
		self.mesPay.addItem("Febrero",1)
		self.mesPay.addItem("Marzo",2)
		self.mesPay.addItem("Abril",3)
		self.mesPay.addItem("Mayo",4)
		self.mesPay.addItem("Junio",5)
		self.mesPay.addItem("Julio",6)
		self.mesPay.addItem("Agosto",7)
		self.mesPay.addItem("Septiembre",8)
		self.mesPay.addItem("Actubre",9)
		self.mesPay.addItem("Noviembre",10)
		self.mesPay.addItem("Diciembre",11)
		self.monto=QSpinBox(self)
		self.monto.setSuffix(" Bs")
		self.nomPago=QLineEdit(self)
		self.fecha=QDateEdit(self)
		self.reloj=QLCDNumber(5,self)
		self.deudor=QTableWidget(self)
		self.deudor.setRowCount(5)
		self.deudor.setColumnCount(3)
		self.deudor.setHorizontalHeaderLabels(["CI","MES","  Bs"])
		self.deudor.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.pospDia=QSpinBox()
		self.pospDia.setSuffix(" Dias")
		self.option=QGroupBox("Opciones",self)
		self.option.setObjectName("busqueda")
		self.option.setCheckable(True)
		self.option.setChecked(False)
	def botones(self):
		self.qrEscaner=QPushButton(QIcon('%s/Imagenes/escaner.png'%self.dir),"",self)
		self.qrEscaner.setIconSize(QSize(70,70))
		self.qrEscaner.setObjectName("redondo")
		self.limpiar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
		self.limpiar.clicked.connect(self.clear)
		self.guardar=QPushButton(QIcon('%s/Imagenes/paymon.png'%self.dir),"Guardar",self)
		self.guardar.clicked.connect(self.save)
		self.guardar.setIconSize(QSize(30,30))
		self.botonSalir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),"",self)
		self.botonSalir.setIconSize(QSize(70,70))
		self.botonSalir.setObjectName("redondo")
		self.botonSalir.clicked.connect(self.salir)
		self.pagar=QPushButton(QIcon('%s/Imagenes/cobrar.png'%self.dir),"Cobrar")
		self.pagar.setIconSize(QSize(30,30))
		self.posponer=QPushButton(QIcon('%s/Imagenes/posponer.png'%self.dir),"Posponer")
		self.posponer.setIconSize(QSize(30,30))
		self.conteOption.addWidget(self.pagar,0,1)
		self.conteOption.addWidget(self.posponer,1,0)
		self.conteOption.addWidget(self.pospDia,1,1)
		self.option.setLayout(self.conteOption)
	def position(self):
		self.fotoEl.setGeometry(40,50,300,300)
		self.nombrel.setGeometry(360,50,150,40)
		self.nombre.setGeometry(510,50,200,40)
		self.apellidol.setGeometry(360,100,150,40)
		self.apellido.setGeometry(510,100,200,40)
		self.qrEscaner.setGeometry(360,150,100,100)
		self.mesPayl.setGeometry(470,150,150,40)
		self.mesPay.setGeometry(630,150,200,40)
		self.montoL.setGeometry(470,200,150,40)
		self.monto.setGeometry(630,200,150,40)
		self.nomPagol.setGeometry(360,260,100,40)
		self.nomPago.setGeometry(470,260,200,40)
		self.fechal.setGeometry(360,310,100,40)
		self.fecha.setGeometry(470,310,200,40)
		self.reloj.setGeometry(680,260,170,90)
		self.deudor.setGeometry(40,360,300,120)
		self.option.setGeometry(360,360,300,120)
		self.guardar.setGeometry(50,500,100,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.botonSalir.setGeometry(735,450,100,100)
	def clear(self):
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
	def save(self):
		pass
	def salir(self):
		self.close()
	def actualizar(self,ide):
		dato=self.db.getEstudiante('Varon',ide)
		if len(dato) is not None:
			self.nombre.setText("<h2>%s</h2>"%dato[1])
			self.apellido.setText("<h2>%s</h2>"%dato[2])
		else:
			dato=self.db.getEstudiante('Mujer',ide)
			if len(dato) is not None:
				self.nombre.setText("<h2>%s</h2>"%dato[1])
				self.apellido.setText("<h2>%s</h2>"%dato[2])