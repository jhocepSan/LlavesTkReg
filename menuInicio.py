#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,registroEstu,Registro

class Example(QMainWindow):    
	def __init__(self):
		super(Example, self).__init__()
		self.dir="F:/LlavesTkReg"
		self.setGeometry(100, 50, 1000, 650)
		self.setWindowTitle('Sequimiento Club')
		self.statusBar().showMessage("Mucho Gusto")
		self.setWindowIcon(QIcon('Imagenes/logo.png'))
		self.mdi=QMdiArea(self)
		self.setCentralWidget(self.mdi)
		self.initUI()
	def initUI(self):
		exitAction = QAction(QIcon('Imagenes/salir.png'), 'Salir App',self,
			shortcut="Ctrl+X",statusTip="Salir de la aplicacion",
			triggered=self.salir)
		initMes=QAction(QIcon('Imagenes/registro.png'),"Registrar Estudiante",
			self,shortcut="Ctrl+R",statusTip="Registrar Estudiante al Club",
			triggered=self.registraEstu)
		asisClub=QAction(QIcon('Imagenes/asistencia.png'),"Control Asistencia",
			self,shortcut="Ctrl+C",statusTip="Controlar Asistencia del Estudiante",
			triggered=self.registraEstu)
		pagoMes=QAction(QIcon('Imagenes/pago.png'),"Registrar Pago",
			self,shortcut="Ctrl+P",statusTip="Registrar Mensualidad del Estudiante",
			triggered=self.registraEstu)
		examenMes=QAction(QIcon('Imagenes/examen.png'),"Examen Estudiante",self,
			shortcut="Ctrl+E",statusTip='Realizar Examen del Club',
			triggered=self.registraEstu)
		listaEst=QAction(QIcon('Imagenes/listaEvento.png'),"Lista Estudiante",self,
			shortcut="Ctrl+L",statusTip='Lista de Estudiantes del Club',
			triggered=self.registraEstu)
		eventoMes=QAction(QIcon('Imagenes/evento.png'),"Evento tk",self,
			shortcut="Ctrl+I",statusTip='Ingreso de estudiates al evento',
			triggered=self.registraEvent)
		self.toolbar = self.addToolBar('Menu')
		self.toolbar.addAction(initMes)
		self.toolbar.addAction(asisClub)
		self.toolbar.addAction(pagoMes)
		self.toolbar.addSeparator()
		self.toolbar.addAction(examenMes)
		self.toolbar.addAction(listaEst)
		self.toolbar.addAction(eventoMes)
		self.toolbar.addSeparator()
		self.toolbar.addAction(exitAction)            
		self.toolbar.setIconSize(QSize(60,60))
		self.toolbar.setOrientation(Qt.Vertical)
		self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
		self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		self.show()
	def registraEstu(self):
		regEst=registroEstu.RegistraEst(self,self.dir)
		self.mdi.addSubWindow(regEst)
		regEst.show()
	def registraEvent(self):
		pass
	def salir(self):
		sys.exit()
def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()