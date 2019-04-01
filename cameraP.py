#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import cv2
class camaraCap(QMainWindow):
	"""docstring for camaraCap"""
	def __init__(self,dire):
		super(camaraCap, self).__init__()
		self.dir=dire
		self.setWindowTitle("Capturar Foto")
		self.setGeometry(100,100,400,450)
		self.setWindowIcon(QIcon('%s/Imagenes/foto.png'%self.dir))
		self.captura=QPushButton(QIcon('%s/Imagenes/foto.png'%self.dir),'',self)
		self.captura.clicked.connect(self.guardar)
		self.cancelar=QPushButton(QIcon('%s/Imagenes/cancelar.png'%self.dir),'',self)
		self.cancelar.clicked.connect(self.salir)
		self.labelf=QLabel('',self)
		self.position()
		self.timer=QTimer(self)
		self.connect(self.timer,SIGNAL("timeout()"),self.capturar)
		self.timer.start(1000)
	def position(self):
		self.labelf.setGeometry(10,10,380,380)
		self.captura.setGeometry(50,390,100,50)
		self.cancelar.setGeometry(250,390,100,50)
	def capturar(self):
		pass
	def guardar(self):
		print "Capturar la foto"
	def salir(self):
		self.timer.stop()
		self.close()
