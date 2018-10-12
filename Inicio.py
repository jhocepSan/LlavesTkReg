#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import sys,os,Mensage,Registro

class dialogo(QDialog):
        def __init__(self,ruta):
                super(dialogo,self).__init__()
                self.cerro=False
                self.resize(350,170)
                self.setWindowTitle("Nombre del EVENTO")
                self.nombrel=QLabel("Nombre: ",self)
                self.nombrela=QLabel("Eventos\nAnteriores:",self)
                self.dir=ruta
                self.msg=Mensage.Msg(self,self.dir)
                self.setWindowIcon(QIcon('%s/Imagenes/Logo.png'%self.dir))
                self.nombre=QLineEdit(self)
                self.nombre.editingFinished.connect(self.comprobar)
                self.eventos=QComboBox(self)
                self.eventos.currentIndexChanged.connect(self.cargarDbD)
                self.botonA=QPushButton("Aceptar",self)
                self.botonA.setIcon(QIcon('%s/Imagenes/aceptar.png'%self.dir))
                self.botonA.setIconSize(QSize(30,30))
                self.botonA.clicked.connect(lambda:self.salire('b'))
                self.botonS=QPushButton("Salir",self)
                self.botonS.setIcon(QIcon('%s/Imagenes/cancelar.png'%self.dir))
                self.botonS.setIconSize(QSize(30,30))
                self.botonS.clicked.connect(lambda:self.salire('a'))
                with open('%s/css/styleDialog.css'%self.dir) as f:
                        self.setStyleSheet(f.read()) 
                self.buscarListas()
                self.position()
        def buscarListas(self):
                file_list=[]
                folders=None
                for root,folders,files in os.walk("%s/baseData/Evento/"%self.dir):
                        file_list.extend(os.path.join(root,fi) for fi in files if fi.endswith(".db"))
                for row,filepath in enumerate(file_list,start=1):
                        (ruta,filename)=os.path.split(filepath)
                        self.eventos.addItem(str(filename[:filename.find(".")]))
        def cargarDbD(self):
                self.nombre.setText(str(self.eventos.currentText()))
        def position(self):
                self.nombrel.setGeometry(10,10,100,40)
                self.nombre.setGeometry(130,10,200,40)
                self.nombrela.setGeometry(10,70,100,40)
                self.eventos.setGeometry(130,70,200,40)
                self.botonA.setGeometry(60,120,100,40)
                self.botonS.setGeometry(200,120,100,40)
        def comprobar(self):
                nombre=self.nombre.text()
                if nombre.find(" ")>=0:
                        self.msg.mensageMalo("<h2>El Nombre Contiene Espacion\nNo es permitido</h2>")
                else:
                        self.nombre.setText(str(nombre.upper()))
        def salire(self,tipo):
                if tipo=='b':
                        nombre=str(self.nombre.text())
                        if nombre!='':
                                self.close()
                                vent=Registro.ventanaR(nombre,self.dir)
                                vent.show()
                elif tipo=='a':
                        sys.exit()
def main():
        app=QApplication(sys.argv)
        screen_resolution = app.desktop().screenGeometry()
        width, height = screen_resolution.width(), screen_resolution.height()
        ruta="."
        #ruta="C:/Registro"
        msgSaludo=QMessageBox()
        with open('%s/css/styleDialog.css'%ruta) as f:
                msgSaludo.setStyleSheet(f.read()) 
        msgSaludo.setIcon(QMessageBox.Information)
        msgSaludo.setWindowTitle("Bienvenido")
        msgSaludo.setWindowIcon(QIcon('%s/Imagenes/propiedad.png'%ruta))
        msgSaludo.setText("<h1>::::Programa Registro:::</h1>")
        msgSaludo.setInformativeText("<h2>Desarrollado en BOLIVIA</h2>\n<h2>Cel: 60790682 Bottan HSoft</h2>\n<h3>Desarrollador: Juan Jose Sanchez Ch.</h3>")
        msgSaludo.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        inf=msgSaludo.exec_()
        if inf==QMessageBox.Ok:
                evt=dialogo(ruta)
                evt.show()
                sys.exit(app.exec_())
        elif inf==QMessageBox.Cancel:
                sys.exit(0)     

if __name__ == '__main__':
        main()
