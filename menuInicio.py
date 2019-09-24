#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,registroEstu,Registro,regAsis,pagoMes,tools
import os,nomina,clubExamen

class Example(QMainWindow):    
	def __init__(self):
		super(Example, self).__init__()
		self.dir="F:/LlavesTkReg"
		with open('%s/css/styleMenuInicio.css'%self.dir) as f:
			self.setStyleSheet(f.read())
		self.setGeometry(10, 30, 1350, 690)
		self.setWindowTitle('Sistema CHOBYT ....!')
		self.statusBar().showMessage("Mucho Gusto disfrute Usando")
		self.setWindowIcon(QIcon('%s/Imagenes/Logo.png'%self.dir))
		self.tabM=QTabWidget(self)
		self.setCentralWidget(self.tabM)
		self.initUI()
	def initUI(self):
		self.regEstu=registroEstu.RegistraEst(self,self.dir)
		self.regEstu.tec.irPago.clicked.connect(lambda:self.irPagos(self.regEstu.tec.persona))
		self.regAsi=regAsis.RegistraAsis(self,self.dir)
		self.payMes=pagoMes.MenuPago(self,self.dir)
		self.examen=clubExamen.ClubExamen(self,self.dir)
		self.listEs=nomina.ListaEstu(self,self.dir)
		self.config=tools.ToolsClub(self,self.dir)
		self.tabM.addTab(self.regEstu,QIcon('%s/Imagenes/registro.png'%self.dir),"Registrar\nEstudiante")
		self.tabM.addTab(self.regAsi,QIcon('%s/Imagenes/asistencia.png'%self.dir),"Control\nAsistencia")
		self.tabM.addTab(self.payMes,QIcon('%s/Imagenes/pago.png'%self.dir),"Registrar Pago")
		self.tabM.addTab(self.examen,QIcon('%s/Imagenes/examen.png'%self.dir),"Examen\nEstudiante")
		self.tabM.addTab(self.listEs,QIcon('%s/Imagenes/listaEvento.png'%self.dir),"Lista de\nEstudiante")
		self.tabM.addTab(self.config,QIcon('%s/Imagenes/config.png'%self.dir),"Configurar")
		self.tabM.currentChanged.connect(self.activo)
		self.tabM.setIconSize(QSize(50,50))
		self.show()
	def salir(self):
		sys.exit()
	def irPagos(self,persona):
		self.tabM.setCurrentIndex(2)
		self.payMes.actualizar(persona.getId())
	def activo(self):
		if(self.tabM.currentIndex()==3):
			self.examen.showMsg()
def main():
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()