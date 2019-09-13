#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector,os,Mensage,shutil,buscar
import os.path as path

class RegIns(QWidget):
    """Registrar Instructores del club"""
    def __init__(self, arg,dire):
        super(RegIns, self).__init__(arg)
        self.dir=dire
        self.db=conector.Conector(self.dir)
        self.msg=Mensage.Msg(self.dir)
        self.buscare=buscar.buscarEst(self,self.dir)
        with open('%s/css/stylesAsis.css'%self.dir) as f:
            self.setStyleSheet(f.read())
        self.myLine()
        self.myButton()
        self.loadInstructor()
        self.position()
    def myLine(self):
        self.ide=QLabel('',self)
        self.tabla=QTableWidget(self)
        self.tabla.setRowCount(20)
        self.tabla.setColumnCount(4)
        self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","Genero","Identificador"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.tabla.itemSelectionChanged.connect(self.activado)
    def myButton(self):
        self.agregar=QPushButton(QIcon("%s/Imagenes/agregar.png"%self.dir),"Agregar",self)
        self.agregar.setIconSize(QSize(30,30))
        self.agregar.clicked.connect(self.agregarIns)
        self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Eliminar",self)
        self.eliminar.setIconSize(QSize(30,30))
        self.eliminar.clicked.connect(self.eliminarIns)
        self.guardar=QPushButton(QIcon('%s/Imagenes/save.png'%self.dir),'Guargar',self)
        self.guardar.setIconSize(QSize(30,30))
        self.guardar.clicked.connect(self.guardarInfo)
        self.limpiar=QPushButton(QIcon('%s/Imagenes/limpiar.png'%self.dir),'Limpiar',self)
        self.limpiar.setIconSize(QSize(30,30))
        self.limpiar.clicked.connect(self.limpiarInfo)
    def activado(self):
        fila=self.tabla.currentRow()
        self.ide.setText(self.tabla.item(fila,3).text())
    def limpiarInfo(self):
        self.buscare.buscar.clear()
        self.tabla.clear()
        self.tabla.setHorizontalHeaderLabels(["Nombre","Apellido","Genero","Identificador"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.ide.setText('')
    def eliminarIns(self):
        if self.ide.text()!='':
            self.db.delInstructorIde(self.ide.text())
            self.msg.mensageBueno("<h1>Se elimino el Istructor</h1>")
            self.limpiarInfo()
            self.loadInstructor()
        else:
            self.msg.mensageMalo("<h1>Error al Eliminar\nSeleccione un Instructor</h1>")
    def guardarInfo(self):
        self.db.delInstructor()
        fila=0
        while self.tabla.item(fila,0)is not None:
            dato=[self.tabla.item(fila,3).text(),self.tabla.item(fila,0).text(),
            self.tabla.item(fila,1).text(),self.tabla.item(fila,2).text()]
            self.db.setInstructor(dato)
            fila+=1
        self.msg.mensageBueno("<h1>Instructores Guardados</h1>")
    def agregarIns(self):
        self.buscare.delSelec()
        dato=self.buscare.getPersona()
        fila=0
        while self.tabla.item(fila,0)is not None:
            fila+=1
        if len(dato)>=2:
            self.tabla.setItem(fila, 0,QTableWidgetItem(dato[0][1]))
            self.tabla.setItem(fila, 1,QTableWidgetItem(dato[0][2]))
            self.tabla.setItem(fila, 2,QTableWidgetItem(dato[1]))
            self.tabla.setItem(fila, 3,QTableWidgetItem(dato[0][0]))
            self.ide.setText(dato[0][0])
        self.buscare.cleanPersona()
    def loadInstructor(self):
        lista=self.db.getInstructor()
        fila=0
        for i in lista:
            self.tabla.setItem(fila,3,QTableWidgetItem(i[0]))
            self.tabla.setItem(fila,0,QTableWidgetItem(i[1]))
            self.tabla.setItem(fila,1,QTableWidgetItem(i[2]))
            self.tabla.setItem(fila,2,QTableWidgetItem(i[3]))
            fila+=1
    def position(self):
        self.tabla.setGeometry(30,30,500,400)
        self.buscare.setGeometry(560,30,250,180)
        self.agregar.setGeometry(560,230,100,40)
        self.eliminar.setGeometry(680,230,100,40)
        self.ide.setGeometry(560,290,250,40)
        self.guardar.setGeometry(200,500,100,40)
        self.limpiar.setGeometry(400,500,100,40)
