from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Msg(QMessageBox):
	"""docstring for Msg"""
	def __init__(self,dire):
		super(Msg, self).__init__()
		self.dir=dire
		self.imgBueno=QPixmap('%s/Imagenes/bien.png'%self.dir)
		self.imgMalo=QPixmap('%s/Imagenes/error.png'%self.dir)
	def mensageBueno(self,msg):
		self.setWindowTitle("CORRECTO")
		self.setWindowIcon(QIcon('%s/Imagenes/bien.png'%self.dir))
		self.setIconPixmap(self.imgBueno.scaled(50, 50,Qt.KeepAspectRatio))
		self.setText(str(msg))
		self.exec_()
	def mensageMalo(self,msg):
		self.setWindowTitle("ERROR")
		self.setWindowIcon(QIcon('%s/Imagenes/error.png'%self.dir))
		self.setIconPixmap(self.imgMalo.scaled(50, 50,Qt.KeepAspectRatio))
		self.setText(str(msg))
		self.exec_()
		