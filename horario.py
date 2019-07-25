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
		self.setGeometry(0,0,885,630)
		self.dir=dire
		self.msges=Mensage.Msg(self.dir)
		self.db=conector.Conector(self.dir)
		self.dirImg=""
		with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.myLabel()
		self.myButton()
		self.position()
	def myLabel(self):
		self.titulo=QLabel("<h1>Horarios del Club</h1>",self)
		self.nomClubl=QLabel("<h2>Nombre Del club</h2>",self)
		self.siglal=QLabel("<h2>Sigla</h2>",self)
		self.tabla=QTableWidget(self)
		self.tabla.setRowCount(20)
		self.tabla.setColumnCount(11)
		self.tabla.setHorizontalHeaderLabels(["Grupo","Instructor","Inicio","Fina","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.tabla.itemSelectionChanged.connect(self.activado)
		self.imgClb=QLabel(self)
		self.imgClb.setObjectName("img")
		img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
		self.imgClb.setPixmap(img)
		self.imgClb.setAlignment(Qt.AlignCenter)
		self.nomClub=QLineEdit(self)
		self.nomClub.editingFinished.connect(self.formalClub)
		self.sigla=QLineEdit(self)
		self.sigla.editingFinished.connect(self.formalSigla)
	def activado(self):
		fila=self.tabla.currentRow()
		if self.tabla.item(fila,4) is None:
			for i in [0,1,2,3,4,5,6,7,8,9,10]:
				if i>=4:
					self.tabla.setItem(fila , i,QTableWidgetItem('n'))
				else: 
					self.tabla.setItem(fila , i,QTableWidgetItem('-'))
	def myButton(self):
		self.guardar=QPushButton(QIcon("%s/Imagenes/save.png"%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(30,30))
		self.guardar.clicked.connect(self.save)
		self.limpiar=QPushButton(QIcon("%s/Imagenes/limpiar.png"%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(30,30))
		self.limpiar.clicked.connect(self.limpiarI)
		self.imprimir=QPushButton(QIcon('%s/Imagenes/print.png'%self.dir),"",self)
		self.imprimir.setIconSize(QSize(70,70))
		self.imprimir.setObjectName("redondo")
		self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"",self)
		self.eliminar.setIconSize(QSize(70,70))
		self.eliminar.setObjectName("redondo")
		self.eliminar.clicked.connect(self.borrarBd)
		self.loadImg=QPushButton(QIcon('%s/Imagenes/foto.png'%self.dir),"",self)
		self.loadImg.setIconSize(QSize(70,70))
		self.loadImg.setObjectName("redondo")
		self.loadImg.clicked.connect(self.cargarImg)
	def position(self):
		self.titulo.setGeometry(292,30,300,40)
		self.tabla.setGeometry(50,90,400,400)
		self.imgClb.setGeometry(460,90,200,200)
		self.loadImg.setGeometry(680,140,100,100)
		self.nomClubl.setGeometry(460,310,150,40)
		self.nomClub.setGeometry(620,310,150,40)
		self.siglal.setGeometry(460,370,150,40)
		self.sigla.setGeometry(620,370,150,40)
		self.guardar.setGeometry(50,500,100,40)
		self.limpiar.setGeometry(390,500,100,40)
		self.eliminar.setGeometry(625,450,100,100)
		self.imprimir.setGeometry(735,450,100,100)
	def save(self):
		self.db.delHorarioClub()
		cont=0
		#try:
		club=[unicode(self.nomClub.text()),self.sigla.text(),self.dirImg]
		self.db.setClub(club)
		while self.tabla.item(cont,0).text()!=' ':
			dias=str(self.buscarDias(cont))
			dataHor=[str(self.tabla.item(cont,0).text()).replace(' ',''),
			str(self.tabla.item(cont,1).text()).title(),
			str(self.tabla.item(cont,2).text()).replace(' ',''),
			str(self.tabla.item(cont,3).text()).replace(' ',''),dias]
			self.db.setHorario(dataHor)
			cont+=1
		self.msges.mensageBueno("<h1>Se Guardo Correctamente</h1>")
		#except:
		#	self.msges.mensageMalo("<h1>Un Problema al guardar La información</h1>")
	def buscarDias(self,cont):
		diaT=""
		dia=4
		for i in ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]:
			d=self.tabla.item(cont,dia).text().replace(' ','')
			if d=='y'or d=='Y':
				diaT+="%s,"%i
			dia+=1
		return diaT[:len(diaT)-1]
	def formalClub(self):
		self.nomClub.setText(unicode(self.nomClub.text()).title())
	def formalSigla(self):
		self.sigla.setText(unicode(self.sigla.text()).upper())
	def cargarImg(self):
		fileName,_ = QFileDialog.getOpenFileName(self,u"Buscar Imagen",QDir.currentPath())
		nombre=unicode(self.nomClub.text().replace(" ","_")).title()
		if (fileName and nombre!=""):
			image = QImage(fileName)
			if image.isNull():
				QMessageBox.information(self, "Seleccione Una Imagen","error %s." % fileName)
				return
			else:
				img=QPixmap.fromImage(image).scaled(180, 180,Qt.KeepAspectRatio)
				self.imgClb.setPixmap(img)
				self.imgClb.setAlignment(Qt.AlignCenter)
				extencion=fileName[fileName.find('.'):]
				direccion="%s/Imagenes/imgClub/%s"%(str(os.getcwd()),str(self.nomClub.text()+extencion))
				shutil.copyfile(fileName,direccion)
				self.dirImg=str(direccion)
		else:
			self.msges.mensageMalo("<h1>Intente Nuevamente\nColoque el Nombre del Club</h1>")
	def limpiarI(self):
		self.nomClub.clear()
		self.sigla.clear()
		img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
		self.imgClb.setPixmap(img)
		self.imgClb.setAlignment(Qt.AlignCenter)
		self.tabla.clear()
		self.tabla.setHorizontalHeaderLabels(["Grupo","Instructor","Inicio","Fina","Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"])
		self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
		self.dirImg=""
	def actualizar(self):
		pass
	def borrarBd(self):
		try:
			self.db.delHorarioClub()
			self.msges.mensageBueno("<h1>Eliminado Correctamente</h1>")
		except:
			self.msges.mensageMalo("<h1>No se Pudo Eliminar los Dato</h1>")