#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector,os,Mensage,shutil
import os.path as path

class ModoPago(QWidget):
    """Tipo de Estudiantes"""
    def __init__(self, arg,dire):
        super(ModoPago,self).__init__(arg)
        self.dir=dire
        with open('%s/css/stylesAsis.css'%self.dir) as f:
            self.setStyleSheet(f.read())
        self.db=conector.Conector(self.dir)
        self.msg=Mensage.Msg(self.dir)
        self.myLabel()
        self.myBitton()
        self.position()
    def myBitton(self):
        self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),'Guardar',self)
        self.guardar.setIconSize(QSize(30,30))
        self.guardar.clicked.connect(self.saveInfo)
        self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),'Limpiar',self)
        self.limpiar.setIconSize(QSize(30,30))
        self.limpiar.clicked.connect(self.limpiarInfo)
        self.borrar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),'Eliminar',self)
        self.borrar.setIconSize(QSize(30,30))
        self.borrar.clicked.connect(self.eliminar)
    def saveInfo(self):
        try:
            self.db.delModalidad()
            fila=0
            while self.tabla.item(fila,0) is not None:
                dato=[self.tabla.item(fila,0).text().title(),int(self.tabla.item(fila,1).text())]
                self.db.setModalidad(dato)
                fila+=1
            self.msg.mensageBueno("<h1>Se Guardo Correctamente la Informacion</h1>")
        except:
            self.msg.mensageMalo("<h1>No se Guardo Correctamente</h1>")
    def limpiarInfo(self):
        self.tabla.clear()
        self.tabla.setHorizontalHeaderLabels(["Tipo Estudiante","Pago [Bs]"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
    def eliminar(self):
        try:
            self.db.delModalidad()
            self.msg.mensageBueno("<h1>Se Guardo Correctamente la Informacion</h1>")
        except:
            self.msg.mensageMalo("<h1>No se pudo Completar </h1>")
    def myLabel(self):
        self.tabla=QTableWidget(self)
        self.tabla.setRowCount(10)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Tipo Estudiante","Pago [Bs]"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
    def position(self):
        self.tabla.setGeometry(50,50,300,300)
        self.guardar.setGeometry(50,510,100,40)
        self.limpiar.setGeometry(200,510,100,40)
        self.borrar.setGeometry(350,510,100,40)
    def actualizar(self):
        dato=self.db.getModalidad()
        fila=0
        for i in dato:
            self.tabla.setItem(fila , 0,QTableWidgetItem(str(i[0])))
            self.tabla.setItem(fila , 1,QTableWidgetItem(str(i[1])))
            fila+=1