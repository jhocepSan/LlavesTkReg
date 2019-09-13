#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import Mensage,conector

class Club(QWidget):
    def __init__(self,parent,dir):
        super(Club, self).__init__(parent)
        self.dir=dir
        with open('%s/css/stylesAsis.css'%self.dir) as f:
			self.setStyleSheet(f.read())
        self.db=conector.Conector(self.dir)
        self.setWindowTitle("Agregar Club")
        self.msg=Mensage.Msg(self.dir)
        self.myText()
        self.myLine()
        self.myButton()
        self.position()
        self.llenarClub()
    def myText(self):
        self.nomClubl=QLabel("Nombre Club",self)
        self.siglaClubl=QLabel("Sigla Club",self)
        self.phoneClubl=QLabel("Telefono",self)
        self.dirClubl=QLabel("Direccion",self)
        self.fechaClubl=QLabel("Fecha Inicio",self)
        self.imgClb=QLabel(self)
        self.imgClb.setObjectName("img")
        img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
        self.imgClb.setPixmap(img)
        self.imgClb.setAlignment(Qt.AlignCenter)
        self.direClub=''
        self.tabla=QTableWidget(self)
        self.tabla.setRowCount(20)
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["Nombre","Sigla"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
        self.tabla.itemSelectionChanged.connect(self.activado)
    def myLine(self):
        self.nomClub=QLineEdit(self)
        self.nomClub.editingFinished.connect(lambda:self.formalizar(self.nomClub))
        self.siglaClub=QLineEdit(self)
        self.siglaClub.editingFinished.connect(self.mayusculas)
        self.phoneClub=QLineEdit(self)
        self.dirClub=QLineEdit(self)
        self.dirClub.editingFinished.connect(lambda:self.formalizar(self.dirClub))
        self.fechaClub=QDateEdit(self)
    def position(self):
        self.nomClubl.setGeometry(30,100,150,40)
        self.siglaClubl.setGeometry(30,160,150,40)
        self.phoneClubl.setGeometry(30,220,150,40)
        self.dirClubl.setGeometry(30,280,150,40)
        self.fechaClubl.setGeometry(30,340,150,40)
        self.nomClub.setGeometry(200,100,150,40)
        self.siglaClub.setGeometry(200,160,150,40)
        self.phoneClub.setGeometry(200,220,150,40)
        self.dirClub.setGeometry(200,280,150,40)
        self.fechaClub.setGeometry(200,340,150,40)
        self.imgClb.setGeometry(400,100,200,200)
        self.tabla.setGeometry(650,100,220,300)
        self.loadImg.setGeometry(450,320,100,100)
        self.guardar.setGeometry(30,500,100,40)
        self.limpiar.setGeometry(300,500,100,40)
        self.eliminar.setGeometry(600,500,100,40)
    def myButton(self):
        self.guardar=QPushButton(QIcon("%s/Imagenes/save.png"%self.dir),"Guardar",self)
        self.guardar.setIconSize(QSize(30,30))
        self.guardar.clicked.connect(self.save)
        self.limpiar=QPushButton(QIcon("%s/Imagenes/limpiar.png"%self.dir),"Limpiar",self)
        self.limpiar.setIconSize(QSize(30,30))
        self.limpiar.clicked.connect(self.limpiarI)
        self.eliminar=QPushButton(QIcon('%s/Imagenes/borrar.png'%self.dir),"Eliminar",self)
        self.eliminar.setIconSize(QSize(30,30))
        self.eliminar.clicked.connect(self.borrarBd)
        self.loadImg=QPushButton(QIcon('%s/Imagenes/foto.png'%self.dir),"",self)
        self.loadImg.setIconSize(QSize(70,70))
        self.loadImg.setObjectName("redondo")
        #self.loadImg.clicked.connect(self.cargarImg)
    def limpiarI(self):
        self.nomClub.clear()
        self.siglaClub.clear()
        self.phoneClub.clear()
        self.dirClub.clear()
    def borrarBd(self):
        nombre=self.nomClub.text()
        sigla=self.siglaClub.text()
        if nombre!='' and sigla!='':
            self.db.delClubId([nombre,sigla])
            self.clearTabla()
            self.llenarClub()
            self.msg.mensageBueno("<h1>Se elimino el club %s</h1>"%nombre)
        else:
            self.msg.mensageMalo("<h1>Seleccione el Club que Quiere Eliminar</h1>")
    def clearTabla(self):
        self.tabla.clear()
        self.tabla.setHorizontalHeaderLabels(["Nombre","Sigla"])
        self.tabla.horizontalHeader().setResizeMode(QHeaderView.ResizeToContents)
    def save(self):
        try:
            dato=[unicode(self.nomClub.text()),unicode(self.siglaClub.text()),
            int(self.phoneClub.text()),unicode(self.dirClub.text()),
            self.fechaClub.date().toString("d/M/yyyy"),self.direClub]
            self.db.setClub(dato)
            self.clearTabla()
            self.llenarClub()
            self.msg.mensageBueno("<h1>Se Guardo Correctamente\nEl Club %s</h1>"%self.nomClub.text())
        except:
            self.msg.mensageMalo("<h1>Se Produjo un Error</h1>")
    def formalizar(self,line):
        line.setText(line.text().title())
    def mayusculas(self):
        self.siglaClub.setText(self.siglaClub.text().upper())
    def llenarClub(self):
        club=self.db.getClub()
        cont=0
        for i in club:
            self.tabla.setItem(cont , 0,QTableWidgetItem(str(i[0])))
            self.tabla.setItem(cont , 1,QTableWidgetItem(str(i[1])))
            cont+=1
    def activado(self):
        info=self.db.getClubId(self.tabla.item(self.tabla.currentRow(),0).text())
        if len(info)!=0:
            info=info[0]
            self.nomClub.setText(unicode(info[0]))
            self.siglaClub.setText(unicode(info[1]))
            self.phoneClub.setText(unicode(info[2]))
            self.dirClub.setText(unicode(info[3]))
            fecha=info[4].split('/')
            self.fechaClub.setDate(QDate(int(fecha[2]),int(fecha[1]),int(fecha[0])))
            img=QPixmap.fromImage(QImage(info[5])).scaled(180,180,Qt.KeepAspectRatio)
            self.imgClb.setPixmap(img)
            self.imgClb.setAlignment(Qt.AlignCenter)