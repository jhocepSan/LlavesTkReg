#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector

class NombreExamen(QWidget):
    def __init__(self,dire):
        super(NombreExamen, self).__init__()
        self.dir=dire
        self.db=conector.Conector(self.dir)
        self.setWindowTitle("Nombre del Examen del club")
        self.myComponente()
        self.position()
    def myComponente(self):
        self.nuevol=QLabel("Nuevo Nombre",self)
        self.nuevo=QLineEdit(self)
        self.cargarl=QLabel("Antiguo",self)
        self.cargar=QComboBox(self)
        self.loadLista()
        self.aceptar=QPushButton(QIcon('%s/Imagenes/aceptar.png'%self.dir),'Aceptar',self)
        self.aceptar.setIconSize(QSize(30,30))
        self.cancelar=QPushButton(QIcon('%s/Imagenes/salir.png'%self.dir),'Cancelar',self)
        self.cancelar.setIconSize(QSize(30,30))
        self.cancelar.clicked.connect(self.salir)
    def loadLista(self):
        lista=self.db.getExamenClub()
        print lista
        for i in lista:
            self.cargar.addItem(i[0]+i[1])
    def position(self):
        self.nuevol.setGeometry(10,10,200,40)
        self.nuevo.setGeometry(10,70,150,40)
        self.cargarl.setGeometry(10,130,150,40)
        self.cargar.setGeometry(10,190,150,40)
        self.cancelar.setGeometry(200,70,150,40)
        self.aceptar.setGeometry(200,190,150,40)
    def guardar(self,dato):
        self.db.setExamenClub(dato)
    def salir(self):
        self.close()