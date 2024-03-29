#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pumse,grade,kyruqui,tk5

class ventanaConfi(QMainWindow):
        def __init__(self,ruta=""):
                super(ventanaConfi,self).__init__()
                self.setObjectName("config")
                self.dir=ruta
                self.setGeometry(100,100,775,460)
                with open('%s/css/styleConf.css'%self.dir) as f:
                        self.setStyleSheet(f.read())
                self.setMinimumHeight(460)
                self.setMinimumWidth(775)
                self.setMaximumHeight(460)      
                self.setMaximumWidth(775)
                self.setWindowTitle("Configuracion")
                self.setWindowIcon(QIcon('%s/Imagenes/Logo.png'%self.dir))
                self.miMenu()
                self.kyrugui()
        def miMenu(self):
                menuConf=self.menuBar().addMenu(str('&Ver'))
                self.newAct = QAction("&Configuracion", self,shortcut="Ctrl+C",
                        statusTip="Mostrar Copnfiguracion", triggered=self.verConf)
                menuConf.addAction(self.newAct)
        def verConf(self):
                print("hOLA")
        def kyrugui(self):
                self.menuCat=QTabWidget(self)
                self.menuCat.setObjectName("tabs")
                self.menuCat.setGeometry(5,30,765,420)
                self.menuCat.addTab(kyruqui.kyruguis(self.dir),"&Combates")
                self.menuCat.addTab(pumse.pumses(self.dir),"&Formas")
                self.menuCat.addTab(grade.grades(self.dir),"&Grados")
                self.menuCat.addTab(tk5.tk(self.dir),"&Tk5")