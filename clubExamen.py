#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector,Mensage,buscar

class ClubExamen(QWidget):
    """Organizar Examen Club"""
    def __init__(self, arg,dire):
        super(ClubExamen, self).__init__(arg)
        self.dir=dire
        with open('%s/css/stylesAsis.css'%self.dir) as f:
            self.setStyleSheet(f.read())
        self.setGeometry(0,0,1050,670)
        self.setWindowTitle("Lista de Estudiantes Para el Examen Club")
        self.buscare=buscar.buscarEst(self,self.dir)
        self.buscare.mostrar.clicked.connect(self.agregarLista)
        self.msg=Mensage.Msg(self.dir)
        self.db=conector.Conector(self.dir)
        self.myElemeto()
        self.myButon()
        self.position()
    def myElemeto(self):
        self.fechaL=QLabel('Fecha de\nExamen',self)
        self.fecha=QDateEdit(self)
        self.gradoL=QLabel('Grado a\nPostularce',self)
        self.grado=QComboBox(self)
        self.llenarGrado()
        self.tabla=QTableWidget(self)
        self.tabla.setRowCount(1000)
        self.tabla.setColumnCount(9)
        self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","Fecha\nNacimiento","Lugar de\nNacimiento","Grado\nPostulando","Carnet\nIdentidad","Edad","Observacion","Identificador"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
    def llenarGrado(self):
        grado=self.db.getGrado()
        for i in grado:
            if self.grado.findText(i[0])<0:
                self.grado.addItem(i[0])
    def myButon(self):
        self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),'Guardar',self)
        self.guardar.setIconSize(QSize(30,30))
        self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),'Limpiar',self)
        self.limpiar.setIconSize(QSize(30,30))
        self.viewPdf=QPushButton(QIcon('%s/Imagenes/pdf.png'%self.dir),'Lista en\nPDF',self)
        self.viewPdf.setIconSize(QSize(30,30))
    def position(self):
        self.fechaL.setGeometry(20,20,100,40)
        self.fecha.setGeometry(20,80,150,40)
        self.buscare.setGeometry(250,20,320,160)
        self.gradoL.setGeometry(590,20,150,40)
        self.grado.setGeometry(590,80,150,40)
        self.tabla.setGeometry(20,190,1300,410)
        self.guardar.setGeometry(1000,20,100,40)
        self.limpiar.setGeometry(1000,80,100,40)
        self.viewPdf.setGeometry(1000,140,100,40)
    def agregarLista(self):
        fila=0
        while True:
            if self.tabla.item(fila,0) is None:
                datos=self.buscare.getPersona()[0]
                print datos
                self.tabla.setItem(fila,0,QTableWidgetItem(datos[1]))
                self.tabla.setItem(fila,1,QTableWidgetItem(datos[2]))
                self.tabla.setItem(fila,2,QTableWidgetItem(datos[5]))
                self.tabla.setItem(fila,3,QTableWidgetItem(datos[6]))
                self.tabla.setItem(fila,5,QTableWidgetItem(datos[3]))
                break
            else:
                fila+=1
                