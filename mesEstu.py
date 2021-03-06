#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import time,buscar
import Mensage,conector
class mesEstu(QWidget):
	"""Vista de pago mensualidad estudiante"""
	def __init__(self,parent,dire):
		super(mesEstu, self).__init__(parent)
		self.dir=dire
		self.msg=Mensage.Msg(self.dir)
		self.db=conector.Conector(self.dir)
		self.buscare=buscar.buscarEst(self,self.dir)
		self.buscare.mostrar.clicked.connect(self.colocarEst)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.texto()
		self.myLine()
		self.botones()
		self.position()
	def texto(self):
		self.nombrel=QLabel("Nombre: ",self)
		self.nombre=QLabel('',self)
		self.apellidol=QLabel("Apellidos: ",self)
		self.apellido=QLabel('',self)
		self.mesPayl=QLabel("Mes a Pagar: ",self)
		self.montoL=QLabel("Mensualidad: ",self)
		self.nomPagol=QLabel("Responsable: ",self)
		self.fechal=QLabel("Fecha: ",self)
		self.ide=QLabel('',self)
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
		self.monto.setMaximum(1000)
		self.nomPago=QLineEdit(self)
		self.nomPago.editingFinished.connect(self.formal)
		self.fecha=QDateEdit(self)
		fecha=time.strftime('%Y-%m-%d').split('-')
		self.fecha.setDate(QDate(int(fecha[0]),int(fecha[1]),int(fecha[2])))
		self.deudor=QTableWidget(self)
		self.deudor.setRowCount(5)
		self.deudor.setColumnCount(3)
		self.deudor.setHorizontalHeaderLabels(["CI","MES","  Bs"])
		self.deudor.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.pospDia=QSpinBox()
		self.pospDia.setSuffix(" Dias")
	def formal(self):
		self.nomPago.setText(self.nomPago.text().title())
	def botones(self):
		self.qrEscaner=QPushButton(QIcon('%s/Imagenes/escaner.png'%self.dir),"",self)
		self.qrEscaner.setIconSize(QSize(70,70))
		self.qrEscaner.setObjectName("redondo")
		self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
		self.limpiar.clicked.connect(self.clear)
		self.guardar=QPushButton(QIcon('%s/Imagenes/paymon.png'%self.dir),'Guardar',self)
		self.guardar.clicked.connect(self.save)
		self.guardar.setIconSize(QSize(30,30))
		self.botonSalir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),"",self)
		self.botonSalir.setIconSize(QSize(70,70))
		self.botonSalir.setObjectName("redondo")
	def position(self):
		self.qrEscaner.setGeometry(250,30,100,100)
		self.buscare.setGeometry(30,150,320,180)
		self.deudor.setGeometry(30,390,300,150)
		self.nombrel.setGeometry(390,50,150,40)
		self.nombre.setGeometry(560,50,200,40)
		self.apellidol.setGeometry(390,100,150,40)
		self.apellido.setGeometry(560,100,200,40)
		self.mesPayl.setGeometry(390,150,150,40)
		self.mesPay.setGeometry(560,150,200,40)
		self.montoL.setGeometry(390,200,150,40)
		self.monto.setGeometry(560,200,150,40)
		self.nomPagol.setGeometry(390,260,150,40)
		self.nomPago.setGeometry(560,260,200,40)
		self.fechal.setGeometry(390,310,150,40)
		self.fecha.setGeometry(560,310,200,40)
		self.guardar.setGeometry(780,250,120,40)
		self.ide.setGeometry(390,370,150,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.botonSalir.setGeometry(735,450,100,100)
	def clear(self):
		self.ide.setText('')
		self.nombre.setText('')
		self.apellido.setText('')
		self.monto.value(0)
		self.buscare.limpiarBusqueda()
	def save(self):
		if self.nomPago.text()!=''and self.monto.value()!=0 and self.ide.text()!='':
			datos=[self.ide.text(),self.mesPay.currentText(),self.fecha.date().toString("d/M/yyyy"),
			self.nomPago.text(),self.monto.value()]
			if not self.db.pagoMes(datos):
				self.db.setPago(datos)
				self.msg.mensageBueno("<h1>Datos del Pago Guardados Correctamente</h1>")
			else:
				self.msg.mensageMalo("<h1>El Estudiante ya pago del mes seleccionado</h1>")
		else:
			self.msg.mensageMalo("<h1>Complete la informacion Faltante</h1>")
	def actualizar(self,ide):
		self.ide.setText(ide)
		dato=self.db.getEstudiante('Varon',ide)
		self.loadMensualidad(ide)
		if len(dato) is not None:
			self.nombre.setText(dato[1])
			self.apellido.setText(dato[2])
		else:
			dato=self.db.getEstudiante('Mujer',ide)
			if len(dato) is not None:
				self.nombre.setText(dato[1])
				self.apellido.setText(dato[2])
	def colocarEst(self):
		persona=self.buscare.getPersona()[0]
		if len(persona)!=0:
			self.ide.setText(persona[0])
			self.nombre.setText(persona[1])
			self.apellido.setText(persona[2])
			self.loadMensualidad(persona[0])
			self.buscare.cleanPersona()
	def loadMensualidad(self,ide):
		mes=self.db.getDatoMes(ide)
		costo=self.db.getModalidadId(mes[4])
		self.monto.setValue(int(costo[0][1]))