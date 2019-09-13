#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import Mensage,conector,tutores,pagoMes
class tecR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire,ide):
		super(tecR, self).__init__(parent)
		self.elementos=False
		self.persona=ide
		self.dir=dire
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
		self.sangrel=QLabel("Tipo de\nSangre:",self)
		self.alergial=QLabel("Alergia\nPatologia:",self)
		self.mesInil=QLabel("Fecha\nInicio:",self)
		self.gradoInil=QLabel("Grado\nInicial:",self)
		self.clubAnl=QLabel("Club\nAnterio:",self)
		self.tipoEsl=QLabel("Modalidad",self)
		self.horariol=QLabel("Horario",self)
		self.fotoC=QLabel(self)
		self.fotoC.setObjectName("img")
		self.fotoC.setAlignment(Qt.AlignCenter);
		self.fotoC.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(200,200,Qt.KeepAspectRatio))
	def line(self):
		self.club=QComboBox(self)
		self.club.setIconSize(QSize(30,30))
		self.grado=QComboBox(self)
		self.grado.setIconSize(QSize(30,30))
		self.altura=QDoubleSpinBox(self)
		self.altura.setSuffix("  [m]")
		self.altura.setSingleStep(0.01)
		self.altura.setMaximum(5)
		self.altura.setMinimum(0)
		self.peso=QDoubleSpinBox(self)
		self.peso.setSuffix(" [Kgr]")
		self.peso.setSingleStep(0.01)
		self.peso.setMaximum(200)
		self.peso.setMinimum(0)
		self.phone=QLineEdit(self)
		self.mesIni=QDateEdit(self)
		self.tipoEs=QComboBox(self)
		self.home=QLineEdit(self)
		self.home.editingFinished.connect(lambda:self.formalizar(self.home))
		self.alergia=QLineEdit(self)
		self.alergia.editingFinished.connect(lambda:self.formalizar(self.alergia))
		self.sangre=QComboBox(self)
		self.sangre.setIconSize(QSize(30,30))
		self.sangre.addItem("O+")
		self.sangre.addItem("O-")
		self.sangre.addItem("A+")
		self.sangre.addItem("A-")
		self.sangre.addItem("B+")
		self.sangre.addItem("B-")
		self.sangre.addItem("AB+")
		self.sangre.addItem("AB-")
		self.horario=QComboBox(self)
		self.gradoIni=QComboBox(self)
		self.clubAn=QLineEdit(self)
		self.clubAn.editingFinished.connect(lambda:self.formalizar(self.clubAn))
		self.tutor=tutores.tutorReg(self,self.dir,self.persona)
	def formalizar(self,elem):
		elem.setText(elem.text().title())
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(40,40))
		self.limpiar.clicked.connect(self.clear)
		self.limpiar.setStatusTip("Limpiar Informacion del formulario")
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(40,40))
		self.guardar.clicked.connect(self.save)
		self.guardar.setStatusTip("Guardar Informacion")
		self.irPago=QPushButton(QIcon('%s/Imagenes/pago.png'%self.dir),'',self)
		self.irPago.setIconSize(QSize(80,80))
		self.irPago.setObjectName("redondo")
		self.irPago.setStatusTip("Ir a pago Mensualidad para el Estudiante")
	def position(self):
		self.tutor.setGeometry(560,180,400,180)
		self.ide.setGeometry(300,10,200,40)
		self.clubl.setGeometry(50,60,100,40)
		self.gradoL.setGeometry(50,110,100,40)
		self.alturaL.setGeometry(50,160,100,40)
		self.pesol.setGeometry(50,210,100,40)
		self.phoneL.setGeometry(50,260,100,40)
		self.mesInil.setGeometry(50,310,100,40)
		self.tipoEsl.setGeometry(50,360,100,40)
		self.homeL.setGeometry(50,410,100,40)
		self.home.setGeometry(160,410,300,40)
		self.alergial.setGeometry(50,470,100,40)
		self.alergia.setGeometry(160,470,300,40)
		self.fotoC.setGeometry(340,60,200,200)
		self.gradoInil.setGeometry(560,60,100,40)
		self.gradoIni.setGeometry(680,60,150,40)
		self.clubAnl.setGeometry(560,120,100,40)
		self.clubAn.setGeometry(680,120,150,40)
		self.irPago.setGeometry(840,60,100,100)
		self.sangrel.setGeometry(340,280,100,40)
		self.sangre.setGeometry(450,280,90,30)
		self.horariol.setGeometry(340,340,100,40)
		self.horario.setGeometry(450,340,100,40)
		self.club.setGeometry(160,60,150,40)
		self.grado.setGeometry(160,110,150,40)
		self.altura.setGeometry(160,160,150,40)
		self.peso.setGeometry(160,210,150,40)
		self.phone.setGeometry(160,260,150,40)
		self.mesIni.setGeometry(160,310,150,40)
		self.tipoEs.setGeometry(160,360,150,40)
		self.guardar.setGeometry(500,470,130,40)
		self.limpiar.setGeometry(650,470,130,40)
	def save(self):
		try:
			datos=[self.ide.text(),unicode(self.club.currentText()),self.grado.currentText(),
			self.altura.value(),self.peso.value(),int(self.phone.text()),
			unicode(self.home.text()),self.sangre.currentText(),unicode(self.alergia.text())]
			self.db.setDatoTec(datos)
			datos=[self.ide.text(),self.mesIni.date().toString('yyyy-M-d'),
			self.gradoIni.currentText(),self.clubAn.text(),self.tipoEs.currentText(),
			self.horario.currentText()]
			self.db.setDatoMes(datos)
			self.msg.mensageBueno("<h1>Datos Guardados Correctamente</h1>")
		except:
			self.msg.mensageMalo("<h1>Error Al Guardar</h1>")
	def clear(self):
		self.ide.setText('')
		self.peso.clear()
		self.altura.clear()
		self.home.clear()
		self.phone.clear()
		#self.tutor.clear()
		self.alergia.clear()
		self.persona.setId('')
	def actualizar(self):
		self.ide.setText(self.persona.getId())
		if not self.elementos:
			datos=self.db.getClub()
			for i in datos:
				if self.club.findText(i[0])<0:
					self.club.addItem(QIcon(i[5]),i[0])
			grado=self.db.getGrado()
			for i in grado:
				if self.grado.findText(i[0])<0:
					self.grado.addItem(i[0])
				if self.gradoIni.findText(i[0])<0:
					self.gradoIni.addItem(i[0])
			modalidad=self.db.getModalidad()
			for i in modalidad:
				if self.tipoEs.findText(i[0])<0:
					self.tipoEs.addItem(i[0])
			datos=self.db.getHorario()
			rown=0
			for i in datos:
				rown+=1
				self.horario.addItem(i[0])
			self.elementos=True
		if self.ide.text()!='':
			info=self.db.getDatosTec(self.persona.getId())
			if len(info)!=0:
				self.grado.setCurrentIndex(self.grado.findText(info[2]))
				self.altura.setValue(info[3])
				self.peso.setValue(info[4])
				self.phone.setText(unicode(info[5]))
				self.home.setText(info[6])
				self.sangre.setCurrentIndex(self.sangre.findText(info[7]))
				self.alergia.setText(info[8])
			info=self.db.getDatoMes(self.persona.getId())
			if len(info)!=0:
				fecha=info[1].split('-')
				self.mesIni.setDate(QDate(int(fecha[0]),int(fecha[1]),int(fecha[2])))
				self.gradoIni.setCurrentIndex(self.gradoIni.findText(info[2]))
				self.clubAn.setText(info[3])
				self.tipoEs.setCurrentIndex(self.tipoEs.findText(info[4]))
				self.horario.setCurrentIndex(self.horario.findText(info[5]))
			self.tutor.viewTutor(self.persona.getId())
