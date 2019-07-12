#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,registroEstu,Registro,regAsis,pagoMes,tools

class Example(QMainWindow):    
	def __init__(self):
		super(Example, self).__init__()
		self.dir="F:/LlavesTkReg"
		self.setGeometry(100, 50, 1000, 650)
		self.setWindowTitle('Sequimiento Club')
		self.statusBar().showMessage("Mucho Gusto")
		self.setWindowIcon(QIcon('%s/Imagenes/Logo.png'%self.dir))
		self.mdi=QMdiArea(self)
		self.setCentralWidget(self.mdi)
		self.initUI()
	def initUI(self):
		exitAction = QAction(QIcon('%s/Imagenes/salir.png'%self.dir), 'Salir App',self,
			shortcut="Ctrl+X",statusTip="Salir de la aplicacion",
			triggered=self.salir)
		initMes=QAction(QIcon('%s/Imagenes/registro.png'%self.dir),"Registrar Estudiante",
			self,shortcut="Ctrl+R",statusTip="Registrar Estudiante al Club",
			triggered=self.registraEstu)
		asisClub=QAction(QIcon('%s/Imagenes/asistencia.png'%self.dir),"Control Asistencia",
			self,shortcut="Ctrl+C",statusTip="Controlar Asistencia del Estudiante",
			triggered=self.registraAsis)
		pagoMes=QAction(QIcon('%s/Imagenes/pago.png'%self.dir),"Registrar Pago",
			self,shortcut="Ctrl+P",statusTip="Registrar Mensualidad del Estudiante",
			triggered=self.pagarMes)
		examenMes=QAction(QIcon('%s/Imagenes/examen.png'%self.dir),"Examen Estudiante",self,
			shortcut="Ctrl+E",statusTip='Realizar Examen del Club',
			triggered=self.registraEstu)
		listaEst=QAction(QIcon('%s/Imagenes/listaEvento.png'%self.dir),"Lista Estudiante",self,
			shortcut="Ctrl+L",statusTip='Lista de Estudiantes del Club',
			triggered=self.nominaEstu)
		eventoMes=QAction(QIcon('%s/Imagenes/evento.png'%self.dir),"Evento tk",self,
			shortcut="Ctrl+I",statusTip='Ingreso de estudiates al evento',
			triggered=self.registraEvent)
		configurar=QAction(QIcon('%s/Imagenes/config.png'%self.dir),"Configurar",self,
			shortcut="Ctrl+T",statusTip='Configuracion Del Programa',
			triggered=self.verConfig)
		self.toolbar = self.addToolBar('Menu')
		self.toolbar.addAction(initMes)
		self.toolbar.addAction(asisClub)
		self.toolbar.addAction(pagoMes)
		self.toolbar.addSeparator()
		self.toolbar.addAction(examenMes)
		self.toolbar.addAction(listaEst)
		self.toolbar.addAction(eventoMes)
		self.toolbar.addSeparator()
		self.toolbar.addAction(configurar)
		self.toolbar.addAction(exitAction)            
		self.toolbar.setIconSize(QSize(60,60))
		self.toolbar.setOrientation(Qt.Vertical)
		self.addToolBar(Qt.LeftToolBarArea, self.toolbar)
		self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
		self.show()
	def registraEstu(self):
		regEst=registroEstu.RegistraEst(self,self.dir,self.mdi)
		self.mdi.addSubWindow(regEst)
		regEst.show()
	def registraAsis(self):
		regAsi=regAsis.RegistraAsis(self,self.dir)
		self.mdi.addSubWindow(regAsi)
		regAsi.show()
	def pagarMes(self):
		payMes=pagoMes.MenuPago(self,self.dir)
		self.mdi.addSubWindow(payMes)
		payMes.show()
	def nominaEstu(self):
		listEs=nomina.ListaEstu(self,self.dir)
		self.mdi.addSubWindow(listEs)
		listEs.show()
	def verConfig(self):
		config=tools.ToolsClub(self,self.dir)
		self.mdi.addSubWindow(config)
		config.show()
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