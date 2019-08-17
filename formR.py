#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import pybase64,conector,Mensage
import Base64SIN,prRc4,verhoeff
import qrcode,barcode,time,buscar

class formR(QWidget):
	"""Formulario de registro del estudiante"""
	def __init__(self,parent,dire,ide):
		super(formR, self).__init__(parent)
		self.persona=ide
		self.dir=dire
		self.dirBr=""
		self.dirQr=""
		self.dirFoto=""
		self.db=conector.Conector(self.dir)
		self.msg=Mensage.Msg(self.dir)
		self.verf=verhoeff.verhoeff()
		self.b64=Base64SIN.base64sin()
		with open('%s/css/stylesMenu.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.buscare=buscar.buscarEst(self,self.dir)
		self.buscare.clicked.connect(self.actualizar)
		self.timer=QTimer(self)
		self.texto()
		self.inTex()
		self.botones()
		self.position()
	def texto(self):
		self.nombrel=QLabel("Nombre: ",self)
		self.nombrel.setStatusTip("Nombre del Estudiante")
		self.apellidol=QLabel("Apellidos: ",self)
		self.apellidol.setStatusTip("Apellido del Estudiante")
		self.cil=QLabel("# Carnet : ",self)
		self.cil.setStatusTip("Cedula de Identidad")
		self.fechaNl=QLabel("Fecha\nNacimiento:",self)
		self.fechaNl.setStatusTip("Fecha de Nacimiento del Estudiante")
		self.edadl=QLabel("Edad: ",self)
		self.edadl.setStatusTip("Edad del Estudiante")
		self.lugarl=QLabel("Lugar\nNacimiento: ",self)
		self.lugarl.setStatusTip("Colegio del Estudiante")
		self.fotoEl=QLabel(self)
		self.fotoEl.setStatusTip("Foto del Estudiante")
		self.fotoEl.setObjectName("img")
		self.fotoEl.setPixmap(QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(400,300,Qt.KeepAspectRatio))
		self.fotoEl.setAlignment(Qt.AlignCenter);
		self.title=QLabel("Codigo QR",self)
		self.id=QLabel("",self)
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
		self.lugar=QLineEdit(self)
		self.lugar.editingFinished.connect(lambda:self.formalizar(self.lugar))
		self.edad=QSpinBox(self)
		self.edad.setSuffix(u' años')
		self.compromiso=QCheckBox("Firma\nDocumento",self)
	def botones(self):
		self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),"Limpiar",self)
		self.limpiar.clicked.connect(self.clear)
		self.limpiar.setIconSize(QSize(35,35))
		self.limpiar.setStatusTip("Borrar todos los campos")
		self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),"Guardar",self)
		self.guardar.clicked.connect(self.save)
		self.guardar.setIconSize(QSize(35,35))
		self.guardar.setStatusTip("Guardar la Informacion")
		self.escanQR=QPushButton(QIcon('%s/Imagenes/escanQr.png'%self.dir),"Escanear",self)
		self.escanQR.clicked.connect(self.escanear)
		self.escanQR.setIconSize(QSize(35,35))
		self.escanQR.setStatusTip("Escanear el codigo del Estudiante")
		self.imgE=QPushButton(QIcon('%s/Imagenes/foto.png'%self.dir),"",self)
		self.imgE.setIconSize(QSize(75,75))
		self.imgE.setObjectName("redondo")
		self.imgE.setStatusTip("Sacar foto con la camara")
		self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Eliminar",self)
		self.eliminar.setIconSize(QSize(35,35))
		self.eliminar.clicked.connect(self.eliminarE)
		self.loadImg=QPushButton(QIcon('%s/Imagenes/img.png'%self.dir),"",self)
		self.loadImg.setIconSize(QSize(80,80))
		self.loadImg.setObjectName("redondo")
		self.loadImg.clicked.connect(self.cargarFoto)
		self.loadImg.setStatusTip("Cargar Imagen para el Estudiante")
	def position(self):
		self.nombrel.setGeometry(20,20,120,40)
		self.nombre.setGeometry(150,20,200,40)
		self.apellidol.setGeometry(20,70,120,40)
		self.apellido.setGeometry(150,70,200,40)
		self.cil.setGeometry(20,120,120,40)
		self.ci.setGeometry(150,120,200,40)
		self.fechaNl.setGeometry(20,170,120,40)
		self.fechaN.setGeometry(150,170,200,40)
		self.lugarl.setGeometry(20,220,120,40)
		self.lugar.setGeometry(150,220,200,40)
		self.edadl.setGeometry(20,270,120,40)
		self.edad.setGeometry(150,270,200,40)
		self.eh.setGeometry(370,20,100,40)
		self.em.setGeometry(370,70,100,40)
		self.compromiso.setGeometry(370,110,150,70)
		self.fotoEl.setGeometry(520,20,200,200)
		self.loadImg.setGeometry(370,240,100,100)
		self.escanQR.setGeometry(490,265,130,50)
		self.imgE.setGeometry(640,240,100,100)
		self.id.setGeometry(370,360,300,40)
		self.qr.setGeometry(70,340,250,200)
		self.title.setGeometry(110,360,120,40)
		self.buscare.setGeometry(370,420,400,150)
		self.guardar.setGeometry(740,30,130,40)
		self.limpiar.setGeometry(740,90,130,40)
		self.eliminar.setGeometry(740,150,130,40)
		self.br.setGeometry(760,210,200,100)
	def clear(self):
		self.dirQr=""
		self.dirBr=""
		self.dirFoto=""
		self.id.setText('')
		self.nombre.clear()
		self.apellido.clear()
		self.ci.clear()
		self.fechaN.clear()
		self.lugar.clear()
		self.edad.clear()
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
		year=int(self.fechaN.date().toString('yyyy'))
		self.edad.setValue(int(time.strftime('%Y'))-year)
	def save(self):
		self.generarQr()
		try:
			info=[self.id.text(),unicode(self.nombre.text()),unicode(self.apellido.text()),
				self.ci.text(),self.fechaN.date().toString('yyyy-M-d'),
				unicode(self.lugar.text()),self.edad.value()]
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
	def cargarFoto(self):
		fileName,_ = QFileDialog.getOpenFileName(self,u"Buscar Imagen",QDir.currentPath())
		nombre=unicode(self.id.text().replace(" ",""))
		if (fileName and nombre!=""):
			image = QImage(fileName)
			if image.isNull():
				QMessageBox.information(self, "Seleccione Una Imagen","error %s." % fileName)
				return
			else:
				img=QPixmap.fromImage(image).scaled(400, 300,Qt.KeepAspectRatio)
				self.fotoEl.setPixmap(img)
				self.fotoEl.setAlignment(Qt.AlignCenter)
				extencion=fileName[fileName.find('.'):]
				direccion="%s/Imagenes/imgEstudiante/%s"%(str(os.getcwd()),str(nombre+extencion))
				shutil.copyfile(fileName,direccion)
				self.dirFoto=str(direccion)
		else:
			self.msg.mensageMalo("<h1>Intente Nuevamente\nColoque los datos personales</h1>")
	def escanear(self):
		pass
	def eliminarE(self):
		genero=''
		if self.em.isChecked():
			genero='Mujer'
		else:
			genero='Varon'
		try:
			self.db.delEstudiante(self.id.text(),genero)
			self.msg.mensageBueno("<h1>Se elimino el Estudiante:\n%s</h1>"%str(self.id.text()))
		except :
			self.msg.mensageMalo("<h1>Ocurrio un Problema al\neliminar estudiante</h1>")
	def actualizar(self):
		datos=self.buscare.getPersona()
		if len(datos)!=0:
			persona=datos[0]
			self.timer.stop()
			if datos[1]=='Varon':
				self.eh.setChecked(True)
			else:
				self.em.setChecked(True)
			self.id.setText(persona[0])
			self.nombre.setText(persona[1])
			self.apellido.setText(persona[2])
			self.ci.setText(unicode(persona[3]))
			fecha=persona[4].split('-')
			self.fechaN.setDate(QDate(int(fecha[0]),int(fecha[1]),int(fecha[2])))
			self.lugar.setText(persona[5])
			self.edad.setValue(int(persona[6]))
			self.persona.setId(unicode(self.id.text()))
		else:
			self.timer.start(1000)
			self.timer.timeout.connect(self.actualizar)