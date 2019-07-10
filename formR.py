#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import pybase64,conector,Mensage
import Base64SIN,prRc4,verhoeff
import qrcode,barcode,time

class formR(QWidget):
	"""docstring for formR"""
	def __init__(self,parent,dire,ide):
		super(formR, self).__init__(parent)
		self.persona=ide
		self.dir=dire
		self.dirBr=""
		self.dirQr=""
		self.setGeometry(0,0,885,630)
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		self.verf=verhoeff.verhoeff()
		self.b64=Base64SIN.base64sin()
		with open('%s/css/stylesMenu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.texto()
		self.inTex()
		self.botones()
		self.position()
	def texto(self):
		self.nombrel=QLabel("Nombre: ",self)
		self.apellidol=QLabel("Apellidos: ",self)
		self.cil=QLabel("CI: ",self)
		self.fechaNl=QLabel("Fecha:\nNacimiento",self)
		self.edadl=QLabel("Edad: ",self)
		self.colegiol=QLabel("Colegio: ",self)
		self.fotoEl=QLabel(self)
		self.fotoEl.setObjectName("img")
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.fotoEl.setAlignment(Qt.AlignCenter);
		self.title=QLabel("Codigo QR",self)
		self.id=QLabel("ID",self)
		self.qr=QLabel(self)
		self.qr.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/qr.png'%self.dir)).scaled(250,200,Qt.KeepAspectRatio))
		self.qr.setObjectName("img")
		self.qr.setAlignment(Qt.AlignCenter);
		self.br=QLabel(self)
		self.br.setObjectName("img")
		self.br.setAlignment(Qt.AlignCenter);
		self.br.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/br.png'%self.dir)).scaled(200,100,Qt.KeepAspectRatio))
	def inTex(self):
		self.nombre=QLineEdit(self)
		self.nombre.editingFinished.connect(lambda:self.formalizar(self.nombre))
		self.eh=QCheckBox("Varon", self)
		self.eh.stateChanged.connect(lambda:self.genero('Varon'))
		self.em=QCheckBox("Mujer",self)
		self.em.stateChanged.connect(lambda:self.genero('Mujer'))
		self.apellido=QLineEdit(self)
		self.apellido.editingFinished.connect(lambda:self.formalizar(self.apellido))
		self.ci=QLineEdit(self)
		self.fechaN=QDateEdit(self)
		self.fechaN.dateChanged.connect(self.setEdad)
		self.edad=QSpinBox(self)
		self.edad.setSuffix(u'  años')
		self.colegio=QLineEdit(self)
		self.colegio.editingFinished.connect(lambda:self.formalizar(self.colegio))
		self.compromiso=QCheckBox("Firma\nDocumento",self)
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.limpiar.clicked.connect(self.clear)
		self.limpiar.setIconSize(QSize(35,35))
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.guardar.clicked.connect(self.save)
		self.guardar.setIconSize(QSize(35,35))
		self.escanQR=QPushButton(QIcon('%s/Imagenes/escanQr.png'%self.dir),"Escanear",self)
		#self.genQR.clicked.connect(self.generarQr)
		self.escanQR.setIconSize(QSize(35,35))
		self.imgE=QPushButton(QIcon('%s/Imagenes/foto.png'%self.dir),"",self)
		self.imgE.setIconSize(QSize(75,75))
		self.imgE.setObjectName("redondo")
		self.loadImg=QPushButton(QIcon('%s/Imagenes/img.png'%self.dir),"",self)
		self.loadImg.setIconSize(QSize(80,80))
		self.loadImg.setObjectName("redondo")
		self.loadImg.clicked.connect(self.cargarFoto)
	def position(self):
		self.nombrel.setGeometry(30,20,100,40)
		self.nombre.setGeometry(140,20,150,40)
		self.apellidol.setGeometry(30,70,100,40)
		self.apellido.setGeometry(140,70,150,40)
		self.cil.setGeometry(30,120,100,40)
		self.ci.setGeometry(140,120,150,40)
		self.fechaNl.setGeometry(30,170,100,40)
		self.fechaN.setGeometry(140,170,150,40)
		self.edadl.setGeometry(30,220,100,40)
		self.edad.setGeometry(140,220,150,40)
		self.colegiol.setGeometry(30,270,100,40)
		self.colegio.setGeometry(140,270,150,40)
		self.qr.setGeometry(30,340,250,200)
		self.fotoEl.setGeometry(310,20,400,300)
		self.title.setGeometry(310,415,100,40)
		self.id.setGeometry(350,330,300,40)
		self.br.setGeometry(420,380,200,100)
		self.eh.setGeometry(730,20,100,40)
		self.em.setGeometry(730,70,100,40)
		self.compromiso.setGeometry(730,120,150,70)
		self.limpiar.setGeometry(720,200,130,40)
		self.guardar.setGeometry(720,250,130,40)
		self.escanQR.setGeometry(720,300,130,50)
		self.loadImg.setGeometry(640,370,100,100)
		self.imgE.setGeometry(750,370,100,100)
	def clear(self):
		self.dirQr=""
		self.dirBr=""
		self.nombre.clear()
		self.apellido.clear()
		self.ci.clear()
		self.fechaN.clear()
		self.edad.clear()
		self.colegio.clear()
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.qr.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/qr.png'%self.dir)).scaled(250,200,Qt.KeepAspectRatio))
		self.br.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/br.png'%self.dir)).scaled(200,100,Qt.KeepAspectRatio))
	def genero(self,gen):
		if gen=='Varon':
			if(self.eh.isChecked()):
				self.em.setCheckState(Qt.CheckState(False))
		else:
			if(self.em.isChecked()):
				self.eh.setCheckState(Qt.CheckState(False))
	def setEdad(self):
		year= self.fechaN.date().toString('MMMM d,yyyy')
		year=int(year[year.find(',')+1:])
		self.edad.setValue(int(time.strftime('%Y'))-year)
	def save(self):
		self.generarQr()
		try:
			info=[self.id.text(),unicode(self.nombre.text()),unicode(self.apellido.text()),
				self.ci.text(),str(self.fechaN.date().toString('MMMM d,yyyy')),self.edad.value(),
				unicode(self.colegio.text())]
			if self.eh.isChecked():
				self.db.setEstudiante('Varon',info)
			elif self.em.isChecked():
				self.db.setEstudiante('Mujer',info)
			self.persona.setId(unicode(self.id.text()))
			self.msg.mensageBueno("<h1>Guardado Correctamente</h1>")
		except:
			self.msg.mensageMalo("<h1>Error Al Guardar</h1>")
	def generarQr(self):
		codigo=prRc4.codigo(str(self.verf.calcsum(str(self.verf.calcsum(self.ci.text()))))*5,self.nombre.text()+self.fechaN.text())
		self.id.setText(codigo)
		img=qrcode.make(codigo)
		self.dirBr="%s/Imagenes/Br/%s.png"%(self.dir,codigo)
		self.dirQr="%s/Imagenes/Qr/%s.png"%(self.dir,codigo)
		f = open(self.dirQr, "wb")
		img.save(f)
		f.close()
		self.crear_code39(codigo,self.dirBr)
		self.br.setPixmap(QPixmap.fromImage(QImage(self.dirBr)).scaled(200,100,Qt.KeepAspectRatio))
		self.qr.setPixmap(QPixmap.fromImage(QImage(self.dirQr)).scaled(250,200,Qt.KeepAspectRatio))
	def crear_code39(self,valor, archivo):
		code39 = barcode.Code39(valor, writer=barcode.writer.ImageWriter())
		filename = code39.save(archivo)
	def formalizar(self,elem):
		elem.setText(elem.text().title())
