#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import Mensage,conector,tutores
class tecR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire,ide):
		super(tecR, self).__init__(parent)
		self.elementos=False
		self.persona=ide
		self.dir=dire
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		with open('%s/css/stylesAsis.css'%self.dir) as f:
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
		self.fotoC.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.tablaH=QTableWidget(self)
		self.tablaH.setRowCount(20)
		self.tablaH.setColumnCount(5)
		self.tablaH.setHorizontalHeaderLabels(["Grupo","Instructor","Inicio","Fin","Dias"])
		self.tablaH.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
	def line(self):
		self.club=QComboBox(self)
		self.club.setIconSize(QSize(30,30))
		self.grado=QComboBox(self)
		self.grado.setIconSize(QSize(30,30))
		self.altura=QDoubleSpinBox(self)
		self.altura.setSuffix("  [m]")
		self.altura.setSingleStep(0.01)
		self.peso=QDoubleSpinBox(self)
		self.peso.setSuffix(" [Kgr]")
		self.peso.setSingleStep(0.01)
		self.phone=QLineEdit(self)
		self.home=QLineEdit(self)
		self.home.editingFinished.connect(lambda:self.formalizar(self.home))
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
		self.alergia=QLineEdit(self)
		self.mesIni=QDateEdit(self)
		self.gradoIni=QComboBox(self)
		self.clubAn=QLineEdit(self)
		self.clubAn.editingFinished.connect(lambda:self.formalizar(self.clubAn))
		self.tipoEs=QComboBox(self)
		self.tipoEs.addItem("Normal")
		self.tipoEs.addItem("Media Beca")
		self.tipoEs.addItem("Becado")
		self.horario=QComboBox(self)
		self.tutor=tutores.tutorReg(self,self.dir,self.persona)
	def formalizar(self,elem):
		elem.setText(elem.text().title())
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.limpiar.setIconSize(QSize(40,40))
		self.limpiar.clicked.connect(self.clear)
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.guardar.setIconSize(QSize(40,40))
		self.guardar.clicked.connect(self.save)
		self.irPago=QPushButton(QIcon('%s/Imagenes/pago.png'%self.dir),'',self)
		self.irPago.setIconSize(QSize(80,80))
		self.irPago.setObjectName("redondo")
		self.irPago.setStatusTip("Ir a pago Mensualidad")
		#self.irPago.clicked.connect(self.iraPago)
	def position(self):
		self.tutor.setGeometry(560,200,400,140)
		self.ide.setGeometry(300,30,200,40)
		self.clubl.setGeometry(50,80,100,40)
		self.gradoL.setGeometry(50,130,100,40)
		self.alturaL.setGeometry(50,180,100,40)
		self.pesol.setGeometry(50,230,100,40)
		self.phoneL.setGeometry(50,280,100,40)
		self.mesInil.setGeometry(50,330,100,40)
		self.tipoEsl.setGeometry(50,380,100,40)
		self.homeL.setGeometry(50,430,100,40)
		self.home.setGeometry(160,430,300,40)
		self.alergial.setGeometry(50,490,100,40)
		self.alergia.setGeometry(160,490,300,40)
		self.fotoC.setGeometry(340,80,200,200)
		self.gradoInil.setGeometry(560,80,100,40)
		self.gradoIni.setGeometry(680,80,150,40)
		self.clubAnl.setGeometry(560,140,100,40)
		self.clubAn.setGeometry(680,140,150,40)
		self.irPago.setGeometry(840,80,100,100)
		self.sangrel.setGeometry(340,300,100,40)
		self.sangre.setGeometry(450,300,90,30)
		self.horariol.setGeometry(340,360,100,40)
		self.horario.setGeometry(460,360,100,40)
		self.club.setGeometry(160,80,150,40)
		self.grado.setGeometry(160,130,150,40)
		self.altura.setGeometry(160,180,150,40)
		self.peso.setGeometry(160,230,150,40)
		self.phone.setGeometry(160,280,150,40)
		self.mesIni.setGeometry(160,330,150,40)
		self.tipoEs.setGeometry(160,380,150,40)
		self.tablaH.setGeometry(480,430,500,150)
		self.guardar.setGeometry(50,550,100,40)
		self.limpiar.setGeometry(300,550,100,40)
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
		self.peso.clear()
		self.altura.clear()
		self.home.clear()
		self.phone.clear()
		self.tutor.clear()
		self.phonet.clear()
		self.alergia.clear()
	def actualizar(self):
		self.ide.setText(self.persona.getId())
		if not self.elementos:
			datos=self.db.getClub()
			self.club.addItem(QIcon(datos[2]),datos[0])
			self.fotoC.setPixmap(QPixmap.fromImage(QImage(datos[2])).scaled(400,300,Qt.KeepAspectRatio))
			grado=self.db.getGrado()
			for i in grado:
				self.grado.addItem(i[0])
				self.gradoIni.addItem(i[0])
			datos=self.db.getHorario()
			rown=0
			for i in datos:
				self.tablaH.setItem(rown,0,QTableWidgetItem(str(i[0])))
				self.tablaH.setItem(rown,1,QTableWidgetItem(str(i[1])))
				self.tablaH.setItem(rown,2,QTableWidgetItem(str(i[2])))
				self.tablaH.setItem(rown,3,QTableWidgetItem(str(i[3])))
				self.tablaH.setItem(rown,4,QTableWidgetItem(str(i[4])))
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
