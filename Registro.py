#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3,sys,os,shutil
import os.path as path
from fpdf import FPDF
import time,genLlave,listEquiPDF,llavesTK5,genLista
import formas,listEstudent,Mensage,Configure,cameraP
#colocar visualizacion de la configuracion del campeonato en pdf
class ventanaR(QMainWindow):
        def __init__(self,name="",dire=""):
                super(ventanaR,self).__init__()
                self.namE=name
                self.dir=dire
                self.dirrFotoE=''
                self.dirrForoC=''
                self.yearActual=time.strftime("%Y")
                self.setObjectName("ventanaR")  
                self.msges=Mensage.Msg(self.dir)
                self.setWindowIcon(QIcon('%s/Imagenes/Logo.png'%self.dir))
                self.datosC=sqlite3.connect('%s/baseData/config.db'%self.dir)
                with open('%s/css/stylesReg.css'%self.dir) as f:
                        self.setStyleSheet(f.read())
                self.setWindowTitle("Registro de participantes")
                self.resize(1100,700)
                self.setMinimumHeight(700)
                self.setMinimumWidth(1100)
                self.setMaximumHeight(700)
                self.setMaximumWidth(1100)
                self.statusBar().showMessage("Mucho Gusto")
                self.statusBar().setObjectName("infB")
                self.textos()
                self.initLine()
                self.botones()
                self.posicion()
                self.createMenu()
                self.genForm=formas.forma(self.dir)
                namer='%s/baseData/estudiantes.db'%self.dir
                if path.exists(namer):
                        self.listaGeneral=sqlite3.connect(namer)
                else:
                        self.listaGeneral=sqlite3.connect(namer)
                        cur=self.listaGeneral.cursor()
                        cur.execute('CREATE TABLE Hombre(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Club TEXT,FotoP TEXT,FotoC TEXT)')
                        cur.execute('CREATE TABLE Mujer(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Club TEXT,FotoP TEXT,FotoC TEXT)')
                        cur.close()
                        self.listaGeneral.commit()
                if path.exists("%s/baseData/sinDoc.db"%self.dir):
                        self.sndto=sqlite3.connect('%s/baseData/sinDoc.db'%self.dir)
                else:
                        self.sndto=sqlite3.connect('%s/baseData/sinDoc.db'%self.dir)
                        cur=self.sndto.cursor()
                        cur.execute('CREATE TABLE HombreSND(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Equipo TEXT,Club TEXT,Modo TEXT)')
                        cur.execute('CREATE TABLE MujerSND(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Equipo TEXT,Club TEXT,Modo TEXT)')
                        cur.close()
                        self.sndto.commit()
                self.name='%s/baseData/Evento/%s.db'%(self.dir,str(name))
                if path.exists(self.name):
                        self.datos=sqlite3.connect(self.name)
                else:
                        self.datos=sqlite3.connect(self.name)
                        cur=self.sndto.cursor()
                        cur.execute("DELETE from HombreSND WHERE Edad<2000")
                        cur.execute("DELETE FROM MujerSND WHERE Edad<2000")
                        cur.close()
                        self.sndto.commit()
                        self.createTablas()
        def textos(self):
                self.nombr=QLabel("<h1>Nombres</h1>",self)
                self.yearl=QLabel(u"<h1>Año de Nac.</h1>",self)
                self.apllds=QLabel("<h1>Apellidos</h1>",self)
                self.carnet=QLabel("<h1>ID</h1>",self)
                self.cturon=QLabel("<h1>Cinturon</h1>",self)
                self.category=QLabel("<h1>Categoria</h1>",self)
                self.genery=QLabel("<h1>Genero</h1>",self)
                self.club=QLabel("<h1>Club</h1>",self)
                self.years=QLabel("<h1>Edad</h1>",self)
                self.bunder=QLabel("<h1>Peso</h1>",self)
                self.subCategory=QLabel("<h1>SubCategoria</h1>",self)
                self.tipoPartL=QLabel("<h1>Participa</h1>",self)
                self.alturaL=QLabel("<h1>Altura</h1>",self)
                self.ci=QCheckBox("Carnet Identidad",self)
                self.doc=QCheckBox("Documento Grado",self)
                self.cintaN=QCheckBox("Activar CintaNegra",self)
                self.tkTipo=QComboBox(self)
                self.tkTipo.addItem("")
                self.tkTipo.addItem("Principal")
                self.tkTipo.addItem("Suplente")
                self.tkTipo.setObjectName("tkTipo")
                self.tkTipo.setStatusTip("Seleccionar si es Principal o Suplente en TK5 ") 
                self.genero=QComboBox(self)
                self.genero.addItem(QIcon('%s/Imagenes/hombre.png'%self.dir),"Hombre")
                self.genero.addItem(QIcon('%s/Imagenes/mujer.png'%self.dir),"Mujer")
                self.genero.setIconSize(QSize(25,25))
                self.genero.setStatusTip("Seleccionar el genero del Participante")
                self.dataCm=QCheckBox("Mostrar Datos Completos",self)
                self.dataCm.setChecked(True)
                self.imgPar=QLabel(self)
                self.imgPar.setObjectName("imgPar")
                img=QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
                self.imgPar.setPixmap(img)
                self.imgPar.setAlignment(Qt.AlignCenter)
                self.imgClb=QLabel(self)
                self.imgClb.setObjectName("imgPar")
                img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
                self.imgClb.setPixmap(img)
                self.imgClb.setAlignment(Qt.AlignCenter)
                self.tipoPart=QComboBox(self)
                self.tipoPart.addItem(QIcon('%s/Imagenes/cmbat.png'%self.dir),"Combate")
                self.tipoPart.addItem(QIcon('%s/Imagenes/forma.png'%self.dir),"Forma")
                self.tipoPart.addItem(QIcon('%s/Imagenes/romper.png'%self.dir),"Rompimiento")
                self.tipoPart.addItem(QIcon('%s/Imagenes/tk5.png'%self.dir),"TK5")
                self.tipoPart.setStatusTip("Seleccionar el tipo de Participacion del Estudiante") 
                self.tipoPart.setIconSize(QSize(30,30))
                self.tipoPart.currentIndexChanged.connect(self.modoParti)
        def modoParti(self):
                if self.tipoPart.currentText()=='Forma':
                        self.subCategory.setText("<h1>Formas</h1>")
                        self.repaint()
                if self.tipoPart.currentText()=='Combate':
                        self.subCategory.setText("<h1>SubCategoria</h1>")
                        self.repaint()
                if self.tipoPart.currentText()=='TK5':
                        cur=self.datosC.cursor()
                        cur.execute("SELECT * FROM Tk5 WHERE ID=0")
                        for i in cur:
                                self.datoPr=int(i[1])
                                self.datoSp=int(i[2])
                        cur.close()
                        self.datosC.commit()
                        self.subCategory.setText("<h1>Equipo</h1>")
                        self.repaint()
                if self.tipoPart.currentText()=='Rompimiento':
                        self.subCategory.setText("<h1>SubCategoria</h1>")
                        self.repaint()
                self.cinturon.clear()
                self.subCategoria.clear()
        def formalizar(self,elemento):
                texto=unicode(elemento.text())
                elemento.setText(texto.title())
        def initLine(self):
                self.carnetId=QLineEdit(self)
                self.carnetId.editingFinished.connect(self.changeEstu)
                self.carnetId.setStatusTip("Carnet de Identidad o Codigo Aleatorio")
                self.year=QSpinBox(self)
                self.year.setMinimum(0)
                self.year.setMaximum(int(self.yearActual))
                self.year.valueChanged.connect(self.completarYear)
                self.year.setStatusTip(u"Ingresar los años de nacimiento del Participante")
                self.nombres=QLineEdit(self)
                self.nombres.editingFinished.connect(lambda:self.formalizar(self.nombres))
                self.nombres.setStatusTip("Ingrese el nombre del Participante")
                self.apellidos=QLineEdit(self)
                self.apellidos.editingFinished.connect(lambda:self.formalizar(self.apellidos))
                self.apellidos.setStatusTip("Ingresar el apellido del Participante")
                self.edad=QSpinBox(self)
                self.edad.setMinimum(0)
                self.edad.setMaximum(100)
                self.edad.valueChanged.connect(self.completar)
                self.edad.setStatusTip("Ingresar Edad del Participante")
                self.peso=QDoubleSpinBox(self)
                self.peso.setMinimum(0)
                self.peso.setMaximum(300)
                self.peso.setSingleStep(0.1)
                self.peso.valueChanged.connect(self.completarSC)
                self.peso.setStatusTip("Ingresar Peso del Participante")
                self.cinturon=QLineEdit(self)
                self.cinturon.editingFinished.connect(self.autoCarga)
                self.cinturon.setStatusTip("Ingresar el Grado del Participante")
                self.clubs=QLineEdit(self)
                self.clubs.editingFinished.connect(self.formalClub)
                self.clubs.setStatusTip("Ingresar el Club del Participante")
                self.categoria=QLineEdit(self) 
                self.categoria.setStatusTip("Categoria del Participante") 
                self.subCategoria=QLineEdit(self)
                self.subCategoria.textChanged.connect(self.autoForma)
                self.subCategoria.setStatusTip("Sub-Categoria del Participante")
                self.altura=QDoubleSpinBox(self)
                self.altura.setMinimum(0)
                self.altura.setMaximum(2)
                self.altura.setSingleStep(0.01)
                self.altura.setStatusTip("Ingresar la altura del Participante") 
        def formalClub(self):
                self.clubs.setText(str(self.clubs.text()).upper())
        def posicion(self):
                self.carnet.setGeometry(20,30,30,40)
                self.carnetId.setGeometry(60,30,140,40)
                self.ci.setGeometry(220,25,180,20)
                self.doc.setGeometry(220,50,190,20)
                self.yearl.setGeometry(420,30,140,40)
                self.year.setGeometry(570,30,80,40)
                self.tabla.setGeometry(680,30,400,630)
                self.nombr.setGeometry(20,80,110,40)
                self.nombres.setGeometry(140,80,140,40)
                self.apllds.setGeometry(300,80,110,40)
                self.apellidos.setGeometry(420,80,150,40)
                self.bsc.setGeometry(600,85,35,35)
                self.genery.setGeometry(20,130,100,40)
                self.genero.setGeometry(130,135,110,40)
                self.years.setGeometry(250,130,80,40)
                self.edad.setGeometry(340,135,80,30)
                self.bunder.setGeometry(480,130,80,40)
                self.peso.setGeometry(570,135,80,30)
                self.cturon.setGeometry(20,190,130,40)
                self.cinturon.setGeometry(160,190,140,40)
                self.category.setGeometry(320,190,130,40)
                self.categoria.setGeometry(460,190,140,40)
                self.club.setGeometry(20,240,130,40)
                self.clubs.setGeometry(160,240,140,40)
                self.subCategory.setGeometry(320,240,185,40)
                self.subCategoria.setGeometry(510,240,90,40)
                self.tipoPartL.setGeometry(20,290,140,40)
                self.tipoPart.setGeometry(170,290,150,40)
                self.alturaL.setGeometry(340,290,80,40)
                self.altura.setGeometry(430,290,100,40)
                self.dataCm.setGeometry(230,360,210,30)
                self.cintaN.setGeometry(230,400,200,40)
                self.tkTipo.setGeometry(230,440,110,40)
                self.imgPar.setGeometry(20,350,200,200)
                self.fotoP.setGeometry(80,560,80,30)
                self.imgClb.setGeometry(450,350,200,200)
                self.fotoCl.setGeometry(510,560,80,30)
                self.foto.setGeometry(285,500,100,100)
                self.botonG.setGeometry(80,610,140,50)
                self.botonC.setGeometry(240,610,120,50)
                self.limpiar.setGeometry(380,610,100,50)
                self.botonS.setGeometry(500,610,100,50)
        def botones(self):
                self.bsc=QPushButton(QIcon('%s/Imagenes/buscar.png'%self.dir),'',self)
                self.bsc.setIconSize(QSize(40,40))
                self.bsc.setStatusTip("Realizar la Busqueda por Nombre Completo")
                self.bsc.clicked.connect(self.buscarNombre)
                self.botonG=QPushButton("Guardar\nParticipante",self)
                self.botonG.setIcon(QIcon('%s/Imagenes/save.png'%self.dir))
                self.botonG.setIconSize(QSize(30,30))
                self.botonG.clicked.connect(self.guardar)
                self.botonG.setStatusTip("Guadar Informacion")
                self.botonC=QPushButton("Generar\nLlaves",self)
                self.botonC.setIcon(QIcon('%s/Imagenes/generar.png'%self.dir))
                self.botonC.setIconSize(QSize(30,30))
                self.botonC.clicked.connect(self.generar)
                self.botonC.setStatusTip("Generar las llaves del Campeonato")
                self.limpiar=QPushButton("Limpiar\nDatos",self)
                self.limpiar.setIcon(QIcon('%s/Imagenes/limpiar.png'%self.dir))
                self.limpiar.clicked.connect(self.clearAll)
                self.limpiar.setIconSize(QSize(30,30))
                self.limpiar.setStatusTip("Limpiar los campos que llenaste")
                self.botonS=QPushButton("Salir",self)
                self.botonS.setIcon(QIcon('%s/Imagenes/salir.png'%self.dir))
                self.botonS.setIconSize(QSize(30,30))
                self.botonS.setStatusTip("Salir de la Aplicacion")
                self.botonS.clicked.connect(self.salir)
                self.iconP=QIcon('%s/Imagenes/load.png'%self.dir)
                self.iconCl=QIcon('%s/Imagenes/load.png'%self.dir)
                self.fotoP=QPushButton("PSN",self)
                self.fotoP.setIcon(self.iconP)
                self.fotoP.setIconSize(QSize(30,30))
                self.fotoP.clicked.connect(lambda: self.openImg(self.imgPar,"P"))
                self.fotoP.setStatusTip("Cargar Imagen de la Persona")
                self.fotoCl=QPushButton("CLB",self)
                self.fotoCl.setIcon(self.iconCl)
                self.fotoCl.setIconSize(QSize(30,30))
                self.fotoCl.clicked.connect(lambda: self.openImg(self.imgClb,"C"))
                self.fotoCl.setStatusTip("Cargar Imagen del Club")
                self.foto=QPushButton(QIcon("%s/Imagenes/foto.png"%self.dir),"",self)
                self.foto.setIconSize(QSize(60,60))
                self.foto.setObjectName("redondo")
                self.foto.setStatusTip("Sacar Foto con la Computadora")
                self.foto.clicked.connect(self.capturaCamara)
                self.tabla=QTableWidget(self)
                self.tabla.setRowCount(100)
                self.tabla.setColumnCount(3)
                self.tabla.setHorizontalHeaderLabels(['Id',"Nombre","Apellido"])
                self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
                self.tabla.cellClicked.connect(self.accionTabla)
        def capturaCamara(self):
                self.camr=cameraP.camaraCap(self.dir)
                self.camr.show()
        def accionTabla(self):
                iden=self.tabla.item(self.tabla.currentRow(),0).text()
                self.carnetId.setText(str(iden))
                self.changeEstu()
        def completarYear(self):
                self.peso.clear()
                self.edad.setValue(int(int(self.yearActual)-int(self.year.value())))
                self.subCategoria.clear()
        def clearAll(self):
                self.carnetId.clear()
                self.nombres.clear()
                self.apellidos.clear()
                self.categoria.clear()
                self.cinturon.clear()
                self.clubs.clear()
                self.subCategoria.clear()
                self.edad.clear()
                self.peso.clear()
                self.year.clear()
                img=QPixmap.fromImage(QImage('%s/Imagenes/psn.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
                self.imgPar.setPixmap(img)
                self.imgPar.setAlignment(Qt.AlignCenter)
                img=QPixmap.fromImage(QImage('%s/Imagenes/clb.png'%self.dir)).scaled(180,180,Qt.KeepAspectRatio)
                self.imgClb.setPixmap(img)
                self.imgClb.setAlignment(Qt.AlignCenter)
                self.tabla.clear()
                self.tabla.setHorizontalHeaderLabels(['Id',"Nombre","Apellido"])
                self.dirrForoC=''
                self.dirrFotoE=''
        def buscarNombre(self):
                cur=self.listaGeneral.cursor()
                rown=0
                gen=["Hombre","Mujer"]
                for j in range(2):
                        if self.nombres.text()!='' and self.apellidos.text()!='':
                                cur.execute("SELECT * FROM %s WHERE Nombre=:nom AND Apellido=:apll"%str(gen[j]),
                                        {"nom":str(self.nombres.text()),"apll":str(self.apellidos.text())})
                                for i in cur:
                                        self.carnetId.setText(str(i[0]))
                                        self.genero.setCurrentIndex(j)
                                        self.edad.setValue(int(i[3]))
                                        self.cinturon.setText(i[5])
                                        self.peso.setValue(float(i[4]))
                                        self.clubs.setText(i[6])
                                        self.dirrFotoE=str(i[7])
                                        self.dirrForoC=str(i[8])
                                        self.loaderImg(self.imgPar,str(i[7]))
                                        self.loaderImg(self.imgClb,str(i[8]))
                        elif self.nombres.text()!='' and self.apellidos.text()=='':
                                cur.execute("SELECT * FROM %s WHERE Nombre=:nom"%str(gen[j]),
                                        {"nom":str(self.nombres.text())})
                                for i in cur:
                                        self.tabla.setItem(rown,0,QTableWidgetItem(str(i[0])))
                                        self.tabla.setItem(rown,1,QTableWidgetItem(str(i[1])))
                                        self.tabla.setItem(rown,2,QTableWidgetItem(str(i[2])))
                                        rown+=1
                        elif self.nombres.text()=='' and self.apellidos.text()!='':
                                cur.execute("SELECT * FROM %s WHERE Apellido=:apll"%str(gen[j]),
                                        {"apll":str(self.apellidos.text())})
                                for i in cur:
                                        self.tabla.setItem(rown,0,QTableWidgetItem(str(i[0])))
                                        self.tabla.setItem(rown,1,QTableWidgetItem(str(i[1])))
                                        self.tabla.setItem(rown,2,QTableWidgetItem(str(i[2])))
                                        rown+=1
                cur.close()
                self.listaGeneral.commit()
        def changeEstu(self):
                cur=self.listaGeneral.cursor()
                gen=["Hombre","Mujer"]
                for j in range(2):
                        cur.execute("SELECT * FROM %s WHERE ID=:id"%str(gen[j]),
                                {"id":str(self.carnetId.text()).replace(' ','')})
                        for i in cur:
                                self.genero.setCurrentIndex(j)
                                self.nombres.setText(i[1])
                                self.apellidos.setText(i[2])
                                self.edad.setValue(int(i[3]))
                                self.cinturon.setText(i[5])
                                self.peso.setValue(float(i[4]))
                                self.clubs.setText(i[6])
                                self.dirrFotoE=str(i[7])
                                self.dirrForoC=str(i[8])
                                self.loaderImg(self.imgPar,str(i[7]))
                                self.loaderImg(self.imgClb,str(i[8]))
                if self.dataCm.isChecked()==True:
                        cur1=self.datos.cursor()
                        tabla=str(self.genero.currentText()+self.tipoPart.currentText())
                        cur1.execute("SELECT * FROM %s WHERE ID=:ide"%tabla,{"ide":str(self.carnetId.text())})
                        for i in cur1:
                                tipo=str(self.tipoPart.currentText())
                                if tipo=='TK5' or tipo=='Forma':
                                        self.cinturon.setText(str(i[5]))
                                        self.subCategoria.setText(str(i[7]))
                                        if self.tipoPart.currentText()=='TK5':
                                                if str(i[9])=='Principal':
                                                        self.tkTipo.setCurrentIndex(1)
                                                elif str(i[9])=='Suplente':
                                                        self.tkTipo.setCurrentIndex(2)
                        cur1.close()
                cur.close()
                self.listaGeneral.commit()
                self.datos.commit()
        def completar(self):
                self.year.setValue(int(self.yearActual)-int(self.edad.value()))
                if self.genero.currentText()=="Hombre":
                        if self.cintaN.isChecked():
                                self.completarCatSN("CategoriaH",int(self.edad.value()))
                        else:
                                self.completarCat("CategoriaH",int(self.edad.value()))
                else:
                        if self.cintaN.isChecked():
                                self.completarCatSN("CategoriaM",int(self.edad.value()))
                        else:
                                self.completarCat("CategoriaM",int(self.edad.value()))
        def completarCat(self,categoria,edad):
                cur=self.datosC.cursor()
                cur.execute("SELECT Categoria,EdadIni,EdadFin FROM %s"%str(categoria))
                for i in cur:
                        if edad<=i[2] and edad>=i[1]:
                                self.categoria.setText(str(i[0]))
                                break
                        else:
                                self.categoria.clear()
                cur.close()
                self.datosC.commit()
        def completarCatSN(self,categoria,edad):
                cur=self.datosC.cursor()
                cur.execute("SELECT * FROM %s"%categoria)
                for i in cur:
                        if i[0].find("CintasNegra")>-1:
                                if edad<=i[2] and edad>=i[1]:
                                        self.categoria.setText(str(i[0]))
                                        break
                                else:
                                        self.categoria.clear()
                cur.close()
                self.datosC.commit()
        def completarSC(self):
                if self.genero.currentText()=="Hombre":
                        categoria=str(self.categoria.text())+"Hombre"
                        self.buscarSub(categoria,(self.peso.value()))
                else:
                        categoria=str(self.categoria.text())+"Mujer"
                        self.buscarSub(categoria,(self.peso.value()))
        def buscarSub(self,nombreC,peso):
                tipo=self.tipoPart.currentText()
                if self.categoria.text()!='' and (tipo=='Combate' or tipo=='Rompimiento'):
                        cur=self.datosC.cursor()
                        cur.execute("SELECT SubCat,PesoIni,PesoFin FROM %s"%nombreC)
                        for i in cur:
                                if peso>=i[1] and peso<=i[2]:
                                        self.subCategoria.setText(str(i[0]))
                                        break
                                else:
                                        self.subCategoria.clear()
                        cur.close()
                        self.datosC.commit()
        def createMenu(self):
                self.menuBar().setObjectName("Informar")
                menuConf=self.menuBar().addMenu(str('&Config'))
                self.newAct = QAction("&Configurar", self,shortcut="Ctrl+C",
                        statusTip="Configurar Registro", triggered=self.newConf)
                menuSendI=QAction(u"Copiar la &Configuración",self,shortcut="Ctrl+A",
                        statusTip=u"Copiar la Configuracion de la Asociacón",triggered=self.copyConf)
                menuConf.addAction(self.newAct)
                menuConf.addAction(menuSendI)
                menuPdf=self.menuBar().addMenu(str('&Combates'))
                self.openP=QAction("&Participantes",self,shortcut="Ctrl+P",
                        statusTip="Lista de Participantes clasificados segun categoria",
                        triggered=lambda:self.mostrar("participantes%s"%str(self.namE)))
                menuPdf.addAction(self.openP)
                self.openLl=QAction("&Llaves",self,shortcut="Ctrl+L",
                        statusTip="Llaves de los Combate generados para el Evento: %s"%str(self.namE),
                        triggered=lambda:self.mostrar("llavesCombate%s"%str(self.namE)))
                menuPdf.addAction(self.openLl)
                self.openLsp=QAction("&Sin Pelea",self,shortcut="Ctrl+S",
                        statusTip="Participantes sin Pelea",
                        triggered=lambda:self.mostrar("listaSinPeleallavesCombate%s"%self.namE))
                menuPdf.addAction(self.openLsp)         
                menuPdfF=self.menuBar().addMenu(str('&Formas'))
                openListF=QAction("&Lista &Formas",self,shortcut="Ctrl+F",
                        statusTip="Lista de participantes en Formas",
                        triggered=lambda:self.mostrar("formas%s"%str(self.namE)))
                menuPdfF.addAction(openListF)
                menuPdfR=self.menuBar().addMenu(str('&Rompimiento'))
                self.openPR=QAction("&Participantes",self,shortcut="Ctrl+Q",
                        statusTip="Participantes Rompimiento",
                        triggered=lambda:self.mostrar("participantesRompimiento%s"%str(self.namE)))
                menuPdfR.addAction(self.openPR)
                self.openLlR=QAction("&Llaves",self,shortcut="Ctrl+W",
                        statusTip="Llaves de Rompimiento",
                        triggered=lambda:self.mostrar("llavesRompimiento%s"%str(self.namE)))
                menuPdfR.addAction(self.openLlR)
                self.openSPR=QAction("&Sin Pelea",self,shortcut="Ctrl+E",
                        statusTip="Lista de Rompimiento sinPelea",
                        triggered=lambda:self.mostrar("listaSinPeleallavesR"))
                menuPdfR.addAction(self.openSPR)
                menuTk5=self.menuBar().addMenu(str("&tk5"))
                openLisEq=QAction("Lista &Equipos",self,shortcut="Ctrl+R",
                        statusTip="Lista de Equipos TK5",triggered=lambda:self.mostrar("listaEquipos%s"%self.namE))
                openLlavestk=QAction("Llaves TK5",self,shortcut="Ctrl+T",
                        statusTip="Llaves de TK5",triggered=lambda:self.mostrar("llavestk5%s"%self.namE))
                menuTk5.addAction(openLisEq)
                menuTk5.addAction(openLlavestk)
                menuElim=self.menuBar().addMenu(str('&Eliminar'))
                clearAll=QAction("Eliminar de &Listas",self,shortcut="Ctrl+Z",
                        statusTip="Eliminar participante de la lista general",triggered=lambda:self.eliPar("todo"))
                clearEvent=QAction("Eliminar de &Combate",self,shortcut="Ctrl+X",
                        statusTip="Eliminar participante de la lista de Combate",triggered=lambda:self.eliPar("Combate"))
                clearForm=QAction("Eliminar de &Forma",self,shortcut="Ctrl+V",
                        statusTip="Eliminar participante de la lista de Formas",triggered=lambda:self.eliPar("Forma"))
                clearRomp=QAction("Eliminar de &Rompimiento",self,shortcut="Ctrl+B",
                        statusTip="Eliminar participante de la lista de Rompimiento",triggered=lambda:self.eliPar("Rompimiento"))
                clearTk5=QAction("Eliminar de &TK5",self,shortcut="Ctrl+G",
                        statusTip="Eliminar participante de la lista de TK5",triggered=lambda:self.eliPar("TK5"))
                menuElim.addAction(clearAll)
                menuElim.addAction(clearEvent)  
                menuElim.addAction(clearForm)
                menuElim.addAction(clearRomp)
                menuElim.addAction(clearTk5)
                menuDat=self.menuBar().addMenu(str("&Info"))
                openLsd=QAction("Sin &Documento",self,shortcut="Ctrl+H",
                        statusTip="Participantes Sin Documento",triggered=lambda:self.mostrarSD("sinDocument"))
                loadEst=QAction("Cargar &Lista",self,shortcut="Ctrl+K",
                        statusTip="Cargar lista de Participates",triggered=self.introducirLista)
                loadFot=QAction("Cargar Foto de Estudiantes",self,shortcut="Ctrl+N",
                        statusTip="Cargar foto de Estudiantes del club",triggered=self.loadImgEs)
                loadFotC=QAction("Cargar Foto de Club",self,shortcut="Ctrl+M",
                        statusTip="Cargar foto de Club",triggered=self.loadImgClb)
                menuDat.addAction(loadEst)
                menuDat.addAction(loadFot)
                menuDat.addAction(loadFotC)
                menuLista=self.menuBar().addMenu(str("&Listas"))
                listEe=QAction("Configuraciones",self,shortcut="Ctrl+J",
                        statusTip="Abrir la Configuracion del Programa",
                        triggered=lambda:self.mostrarConf())
                listEr=QAction("General",self,shortcut="Ctrl+Y",
                        statusTip="Abrir lista de Estudiantes Registrados",
                        triggered=lambda:self.mostrarLista("estudiantes"))
                menuLista.addAction(openLsd)
                menuLista.addAction(listEr)
                menuLista.addAction(listEe)
        def eliPar(self,obj):
                ide=str(self.carnetId.text()).replace(' ','')
                gen=str(self.genero.currentText())
                try:
                        if obj=="todo":
                                self.elimination(self.datos,"%sCombate"%gen,ide)
                                self.elimination(self.listaGeneral,"%s"%gen,ide)
                                self.elimination(self.datos,"%sForma"%gen,ide)
                                self.elimination(self.datos,"%sRompimiento"%gen,ide)
                                self.elimination(self.datos,"%sTK5"%gen,ide)
                                self.elimination(self.sndto,"%sSND"%gen,ide)
                        else:
                                if obj=='TK5':
                                        datos=self.obtenerDato()
                                        self.downEquipo("Equipos%s"%str(gen),datos[7],datos[9])
                                self.elimination(self.datos,"%s"%str(gen+obj),ide)
                                self.eliminationSD("%sSND"%gen,ide,obj)
                        self.msges.mensageBueno("<h1>Participante Eliminado</h1>")
                except:
                       self.msges.mensageMalo("<h1>No es posible ELIMINAR participante</h1>")
        def elimination(self,db,tabla,id):
                cur=db.cursor()
                cur.execute("DELETE FROM %s WHERE ID=:ide"%tabla,{"ide":str(id)})
                db.commit()
                cur.close()
        def eliminationSD(self,tabla,ide,modo):
                cur=self.sndto.cursor()
                cur.execute("DELETE FROM %s WHERE ID=:ide AND Modo=:md"%str(tabla),{"ide":str(ide),"md":str(modo)})
                self.sndto.commit()
                cur.close()
        def mostrar(self,name):
                os.system('%s/Documentos/%s.pdf &'%(str(self.dir),str(name)))
        def mostrarLista(self,nombre):
                name="%s/baseData/%s.db"%(self.dir,nombre)
                lista=genLista.listaPDF(name)
                lista.listaEstudiante("Hombre",nombre)
                lista.listaEstudiante("Mujer",nombre)
                lista.salidaPDF(self.dir,nombre)
                lista.cerrarDB()
                self.mostrar("listaGeneral%s"%nombre)
        def mostrarConf(self):
                pass
        def mostrarSD(self,name):
                listaESD=listEstudent.listaPartPDF(self.dir)
                listaESD.generaPDF()
                listaESD.salidaPDF(str(name))
                os.system('%s/Documentos/%s.pdf'%(self.dir,str(name)))
        def guardar(self):
                tipo=self.tipoPart.currentText()
                self.saveInfo()
                if tipo=='Combate'or tipo=='Rompimiento':
                        self.guardarCbt()
                elif tipo=='Forma':
                        self.guardarForm()
                elif tipo=='TK5':
                        self.guardarTk5()
                if self.ci.isChecked()==False and self.doc.isChecked()==False:
                        self.saveInfoSD()
                self.dirrForoC=''
                self.dirrFotoE=''
        def guardarForm(self):
                if self.categoria.text()!='' and self.subCategoria.text()!='':
                        nombre=str(self.genero.currentText()+self.tipoPart.currentText())
                        self.saveCompetitorF(nombre)
                        self.msges.mensageBueno("Participante Guardado")
                else:
                        self.msges.mensageMalo("<h1>Error al GUARDAR</h1>\n<h1>Complete Informacion</h1>")
        def guardarCbt(self):
                if self.categoria.text()!='' and self.subCategoria.text()!='':
                        self.saveCompetitor(str(self.genero.currentText()+self.tipoPart.currentText()))
                        self.msges.mensageBueno("Participante Guardado")
                else:
                        self.msges.mensageMalo("<h1>Error al GUARDAR</h1>\n<h1>Complete Informacion</h1>")
        def guardarTk5(self):
                gen=self.genero.currentText()
                nombre=str(self.genero.currentText()+self.tipoPart.currentText())
                equipo=str(self.subCategoria.text()).replace(' ','')
                if self.tkTipo.currentText()!='':
                        if self.existe()==False and equipo!='':
                                if self.saveEquipo("Equipos%s"%str(gen),equipo,str(self.tkTipo.currentText())):
                                        self.saveCompetitorTK(nombre,str(self.tkTipo.currentText()))
                                        self.msges.mensageBueno("<h2>Participante Guardado en TK5</h2>")
                        elif self.existe()==True and equipo!='':
                                datos=self.obtenerDato()
                                if datos[7]==equipo:
                                        if self.updateEquipo("Equipos%s"%str(gen),equipo,str(self.tkTipo.currentText()),str(datos[9])):
                                                self.updateTk(nombre,str(self.tkTipo.currentText()))
                                                self.msges.mensageBueno("<h2>Infomacion Actualizada</h2>")
                                        else:
                                                self.updateTk(nombre,str(self.tkTipo.currentText()))
                                                self.msges.mensageBueno("<h2>Infomacion Actualizada</h2>")
                                else:
                                        self.downEquipo("Equipos%s"%str(gen),datos[7],str(datos[9]))
                                        if self.saveEquipo("Equipos%s"%str(gen),equipo,str(self.tkTipo.currentText())):
                                                self.updateTk(nombre,str(self.tkTipo.currentText()))
                                                self.msges.mensageBueno("<h2>Actualizacion Correcta</h2>")
                        else:
                                self.msges.mensageMalo("<h1>Colocar El nombre del Equipo !!!<h1>")
                else:
                        self.msges.mensageMalo("<h2>Seleccione si el Participante es:\n Principal o Suplente</h2>")
        def saveEquipo(self,lista,equipo,modotk):
                estado=False
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE Equipo=:n"%str(lista),{"n":str(equipo)})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                if modotk=='Principal':
                                        if int(row[1])<self.datoPr:
                                                datos=[(row[1]+1),row[2],equipo]
                                                cur.execute("UPDATE %s SET Principal=?,Suplente=? WHERE Equipo=?"%str(lista),datos)
                                                self.datos.commit()
                                                estado=True
                                        else:
                                                datos=[row[1],row[2],equipo]
                                                self.msges.mensageMalo("<h2>Equipo %s esta lleno de Principales\nReintente el Guardado</h2>"%str(datos[2]))
                                                estado=False
                                elif modotk=='Suplente':
                                        if row[2]<self.datoSp:
                                                datos=[row[1],(row[2]+1),equipo]
                                                cur.execute("UPDATE %s SET Principal=?,Suplente=? WHERE Equipo=?"%str(lista),datos)
                                                self.datos.commit()
                                                estado=True
                                        else:
                                                datos=[row[1],row[2],equipo]
                                                self.msges.mensageMalo("<h2>Equipo %s esta lleno de Principales\nReintente el Guardado</h2>"%str(datos[2]))
                                                estado=False
                                cur.close()
                                return estado
                except TypeError:
                        dato=[equipo,0,0]
                        cur.execute("INSERT INTO %s VALUES(?,?,?)"%str(lista),dato)
                        self.datos.commit()
                        cur.close()
                        return self.saveEquipo(lista,equipo,modotk)
        def updateEquipo(self,lista,equipo,modotk,modotka):
                estado=False
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE Equipo=:n"%str(lista),{"n":str(equipo)})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                if modotk=='Principal'and modotka!=modotk:
                                        if int(row[1])<self.datoPr:
                                                datos=[(row[1]+1),(row[2]-1),equipo]
                                                cur.execute("UPDATE %s SET Principal=?,Suplente=? WHERE Equipo=?"%str(lista),datos)
                                                self.datos.commit()
                                                estado=True
                                        else:
                                                self.msges.mensageMalo("<h2>Equipo %s esta lleno de Principales\nReintente el Guardado</h2>"%str(datos[2]))
                                                estado=False
                                elif modotk=='Suplente' and modotk!=modotka:
                                        if row[2]<self.datoSp:
                                                datos=[(row[1]-1),(row[2]+1),equipo]
                                                cur.execute("UPDATE %s SET Principal=?,Suplente=? WHERE Equipo=?"%str(lista),datos)
                                                self.datos.commit()
                                                estado=True
                                        else:
                                                self.msges.mensageMalo("<h2>Equipo %s esta lleno de Principales\nReintente el Guardado</h2>"%str(datos[2]))
                                                estado=False
                                cur.close()
                                return estado
                except TypeError:
                        cur.close()
                        return False
        def downEquipo(self,lista,equipo,modotk):
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE Equipo=:n"%str(lista),{"n":str(equipo)})
                self.datos.commit()
                row=cur.fetchone()
                if len(row) is not None:
                        if modotk=='Principal':
                                datos=[(row[1]-1),row[2],equipo]
                                cur.execute("UPDATE %s SET Principal=?,Suplente=? WHERE Equipo=?"%str(lista),datos)
                                self.datos.commit()
                        elif modotk=='Suplente':
                                datos=[(row[1]),(row[2]-1),equipo]
                                cur.execute("UPDATE %s SET Principal=?,Suplente=? WHERE Equipo=?"%str(lista),datos)
                                self.datos.commit()
                        cur.close()
        def existe(self):
                lista=str(self.genero.currentText()+self.tipoPart.currentText())
                cure=self.datos.cursor()
                cure.execute("SELECT * FROM %s WHERE ID=:c "%str(lista),{"c":str(self.carnetId.text())})
                row=cure.fetchone()
                try:
                        if len(row) is not None:
                                cure.close()
                                return True
                except TypeError:
                        cure.close()
                        return False
        def obtenerDato(self):
                lista=str(self.genero.currentText()+self.tipoPart.currentText())
                cure=self.datos.cursor()
                cure.execute("SELECT * FROM %s WHERE ID=:c "%str(lista),{"c":str(self.carnetId.text())})
                row=cure.fetchone()
                cure.close()
                return row
        def updateTk(self,lista,orden):
                cur=self.datos.cursor()
                datoAu=[self.nombres.text(),self.apellidos.text(),self.edad.value(),
                self.peso.value(),self.cinturon.text(),self.categoria.text(),
                self.subCategoria.text(),self.clubs.text().upper(),str(orden),self.carnetId.text()]
                cur.execute("UPDATE %s SET Nombre=?,Apellido=?,Edad=?,Peso=?,Cinturon=?,Categoria=?,Equipo=?,Club=?,Orden=? WHERE ID=?"%str(lista),datoAu)
                self.datos.commit()
                cur.close()
        def saveCompetitorTK(self,lista,orden):
                cur=self.datos.cursor()
                datoAu=[self.carnetId.text(),self.nombres.text(),self.apellidos.text(),
                self.edad.value(),self.peso.value(),self.cinturon.text(),self.categoria.text(),
                self.subCategoria.text(),self.clubs.text().upper(),str(orden)]
                cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?)"%str(lista), datoAu)
                self.datos.commit()
                cur.close()     
        def saveInfo(self):
                cur=self.listaGeneral.cursor()
                identidad=str(self.carnetId.text()).replace(' ','')
                tabla=str(self.genero.currentText())
                cur.execute("SELECT * FROM %s WHERE ID=:id"%tabla,{"id":identidad})
                self.listaGeneral.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                datoAu=[self.nombres.text(),self.apellidos.text(),
                                self.edad.value(),self.peso.value(),self.cinturon.text(),
                                self.clubs.text().upper(),self.dirrFotoE,self.dirrForoC,identidad]
                                cur.execute("UPDATE %s SET Nombre=?,Apellido=?,Edad=?,Peso=?,Cinturon=?,Club=?,FotoP=?,FotoC=? WHERE ID=?"%tabla,
                                datoAu)
                                self.listaGeneral.commit()
                except TypeError:
                        datoAu=[identidad,self.nombres.text(),self.apellidos.text(),
                        self.edad.value(),self.peso.value(),self.cinturon.text(),
                        self.clubs.text().upper(),self.dirrFotoE,self.dirrForoC]
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)"%tabla, datoAu)
                        self.listaGeneral.commit()
                        cur.close()
        def saveInfoSD(self):
                cur=self.sndto.cursor()
                identidad=str(self.carnetId.text()).replace(' ','')
                tabla=str(self.genero.currentText()+"SND")
                cur.execute("SELECT * FROM %s WHERE ID=:id AND Modo=:md"%tabla,{"id":str(identidad),"md":str(self.tipoPart.currentText())})
                self.sndto.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                datoAu=[self.nombres.text(),self.apellidos.text(),
                                        self.edad.value(),self.peso.value(),self.cinturon.text(),
                                        self.categoria.text(),self.subCategoria.text(),
                                        self.clubs.text().upper(),identidad,self.tipoPart.currentText()]
                                cur.execute("UPDATE %s SET Nombre=?,Apellido=?,Edad=?,Peso=?,Cinturon=?,Categoria=?,Equipo=?,Club=? WHERE ID=? AND Modo=?"%tabla,
                                datoAu)
                                self.sndto.commit()
                except TypeError:
                        datoAu=[identidad,self.nombres.text(),self.apellidos.text(),
                                self.edad.value(),self.peso.value(),self.cinturon.text(),
                                self.categoria.text(),self.subCategoria.text(),
                                self.clubs.text().upper(),self.tipoPart.currentText()]
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?)"%tabla, datoAu)
                        self.sndto.commit()
                        cur.close()
        def saveCompetitor(self,lista):
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE ID=:c "%str(lista),
                        {"c": str(self.carnetId.text())})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                datoAu=[self.nombres.text(),self.apellidos.text(),
                                        self.edad.value(),self.peso.value(),self.cinturon.text(),
                                        self.categoria.text(),self.subCategoria.text(),self.clubs.text().upper(),self.carnetId.text()]
                                cur.execute("UPDATE %s SET Nombre=?,Apellido=?,Edad=?,Peso=?,Cinturon=?,Categoria=?,SubCat=?,Club=? WHERE ID=?"%str(lista),
                                datoAu)
                                self.datos.commit()
                except TypeError:
                        datoAu=[self.carnetId.text(),self.nombres.text(),self.apellidos.text(),
                                self.edad.value(),self.peso.value(),self.cinturon.text(),
                                self.categoria.text(),self.subCategoria.text(),self.clubs.text().upper()]
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)"%str(lista), datoAu)
                        self.datos.commit()
                        cur.close()
        def saveCompetitorF(self,lista):
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE ID=:c "%str(lista),
                        {"c": str(self.carnetId.text())})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                datoAu=[self.nombres.text(),self.apellidos.text(),
                                        self.edad.value(),self.peso.value(),self.cinturon.text(),
                                        self.categoria.text(),self.subCategoria.text(),self.clubs.text().upper(),self.carnetId.text()]
                                cur.execute("UPDATE %s SET Nombre=?,Apellido=?,Edad=?,Peso=?,Cinturon=?,Categoria=?,Forma=?,Club=? WHERE ID=?"%str(lista),
                                        datoAu)
                                self.datos.commit()
                except TypeError:
                        datoAu=[self.carnetId.text(),self.nombres.text(),self.apellidos.text(),
                                self.edad.value(),self.peso.value(),self.cinturon.text(),
                                self.categoria.text(),self.subCategoria.text(),self.clubs.text().upper()]
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)"%str(lista), datoAu)
                        self.datos.commit()
                        cur.close()
        def salir(self):
                self.listaGeneral.close()
                self.datos.close()
                self.datosC.close()
                self.genForm.cerrarDB()
                self.close()
        def newConf(self):
                self.config=Configure.ventanaConfi(self.dir)
                self.config.show()
        def loadClub(self):
                self.loadClb=cargarClub()               
                self.loadClb.show()
        def autoCarga(self):
                texto=self.cinturon.text()
                tipo=self.tipoPart.currentText()
                cur=self.datosC.cursor()
                if texto!='' and (tipo=='Combate' or tipo=='Rompimiento' or tipo=='TK5'):
                        cur.execute("SELECT * FROM Grados")
                        for i in cur:
                                sm=self.buscarSimb(str(i[1]))
                                if i[1].find(str(texto+sm))>=0:
                                        self.cinturon.setText(str(i[0]))
                                        break
                                elif i[1].find(str(sm+texto))>=0:
                                        self.cinturon.setText(str(i[0]))
                                        break
                                else:
                                        if i[1].find(texto)>=0 and sm!=',':
                                                self.cinturon.setText(str(i[0]))
                                                break
                                        self.cinturon.clear()
                elif tipo!='Forma':
                        self.cinturon.clear()
                cur.close()
        def buscarSimb(self,dato):
                smb=''
                for i in range(len(dato)):
                        if not dato[i].isdigit():
                                smb=dato[i]
                                break
                return smb
        def autoForma(self):
                if self.tipoPart.currentText()=='Forma':
                        formas=self.subCategoria.text()
                        num=formas[len(formas)-1:]
                        if not num.isdigit():
                                gra=self.cinturon.text().replace(' ','')
                                cur=self.datosC.cursor()
                                cur.execute("SELECT * FROM Pumse WHERE Grado=:gr",{"gr":gra})
                                self.datosC.commit()
                                row=cur.fetchone()
                                nn=formas.split(num)
                                nnn=nn[len(nn)-2]
                                try:
                                        if len(row) is not None:
                                                cur.execute("SELECT * FROM Pumse WHERE Grado=:gr",{"gr":gra})
                                                nf=cur.fetchone()[1].split(',')
                                                for i in range(len(nf)):
                                                        if nf[i]==nnn:
                                                                break
                                                        elif i==len(nf)-1:
                                                                self.msges.mensageMalo("<h2>La FORMA Ingresada\nNo es permitido</h2>")
                                except TypeError:
                                        self.cinturon.clear()
                                        self.subCategoria.clear()
                                        self.msges.mensageMalo("<h1>El Cinturon ingresado No EXISTE</h1>")
                                self.datosC.commit()
                                cur.close()
        def createTablas(self):
                cur=self.datos.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS HombreCombate(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,SubCat TEXT,Club TEXT)')
                cur.execute('CREATE TABLE IF NOT EXISTS MujerCombate(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,SubCat TEXT,Club TEXT)')
                cur.execute('CREATE TABLE IF NOT EXISTS HombreForma(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Forma TEXT,Club TEXT)')
                cur.execute('CREATE TABLE IF NOT EXISTS MujerForma(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Forma TEXT,Club TEXT)')
                cur.execute('CREATE TABLE IF NOT EXISTS HombreRompimiento(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,SubCat TEXT,Club TEXT)')
                cur.execute('CREATE TABLE IF NOT EXISTS MujerRompimiento(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,SubCat TEXT,Club TEXT)')
                cur.execute('CREATE TABLE IF NOT EXISTS HombreTK5(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Equipo TEXT,Club TEXT,Orden INT)')
                cur.execute('CREATE TABLE IF NOT EXISTS MujerTK5(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Equipo TEXT,Club TEXT,Orden INT)')
                cur.execute('CREATE TABLE IF NOT EXISTS EquiposMujer(Equipo TEXT,Principal INT, Suplente INT)')
                cur.execute('CREATE TABLE IF NOT EXISTS EquiposHombre(Equipo TEXT,Principal INT,Suplente INT)')
                cur.close()
                self.datos.commit()
        def generar(self):
                self.genLl=genLlave.generaLlave(self.dir)
                evento=self.tipoPart.currentText()
                QApplication.setOverrideCursor(Qt.WaitCursor)
                #try:
                if evento=='Combate':
                        self.genLl.limpiar("formato")
                        self.genLl.categorizar("CategoriaH","Hombre","HombreCombate",str(self.name),"formato")
                        self.genLl.categorizar("CategoriaM","Mujer","MujerCombate",str(self.name),"formato")
                        self.genLl.generaPdf("participantes%s"%self.namE,"formato")
                        self.genLl.generarLlaves("llavesCombate%s"%self.namE,"Combates")
                        self.msges.mensageBueno("<h1>Generado las llaves</h1>")
                elif evento=='Forma':
                        self.genForm.clasificarForma("CategoriaH","Hombre","HombreForma",str(self.name))
                        self.genForm.clasificarForma("CategoriaM","Mujer","MujerForma",str(self.name))
                        self.genForm.separaForma(self.namE)
                        self.msges.mensageBueno("<h1>Generado las Forma</h1>")                        
                elif evento=='Rompimiento':
                        self.genLl.limpiar("formatoR")
                        self.genLl.categorizar("CategoriaH","Hombre","HombreRompimiento",str(self.name),"formatoR")
                        self.genLl.categorizar("CategoriaM","Mujer","MujerRompimiento",str(self.name),"formatoR")       
                        self.genLl.generaPdf("participantesRompimiento%s"%self.namE,"formatoR")
                        self.genLl.generarLlaves("llavesRompimiento%s"%self.namE,"Rompimiento")
                        self.msges.mensageBueno("<h1>Generado llaves de rompimiento</h1>")
                elif evento=='TK5':
                        llavetk=listEquiPDF.listEquiPdf(self.name)
                        llavetk.enlistarEquipo("HombreRompimiento","EquiposHombre","Hombre")
                        llavetk.enlistarEquipo("MujerRompimiento","EquiposMujer","Mujer")
                        llavetk.salidaPDF(self.namE,self.dir)
                        llaveTkl=llavesTK5.llaveTk5(self.name)
                        llaveTkl.generarTk()
                        llaveTkl.salidaPDF(self.namE,self.dir)
                        self.msges.mensageBueno("<h1>Generado de listas TK5 </h1>")
                #except Exception as e:
                #        self.msges.mensageMalo("Error {}".format(e.args[0]))
                #finally:
                #        QApplication.restoreOverrideCursor()
        def openImg(self,elemento,tipo):
                fileName,_ = QFileDialog.getOpenFileName(self, "Open File",QDir.currentPath())
                if fileName:
                        image = QImage(fileName)
                        if image.isNull():
                                QMessageBox.information(self, "Seleccione Una Imagen","error %s." % fileName)
                                return
                        img=QPixmap.fromImage(image).scaled(180, 180,Qt.KeepAspectRatio)
                        elemento.setPixmap(img)
                        elemento.setAlignment(Qt.AlignCenter)
                        extencion=fileName[fileName.find('.'):]
                        if tipo=='C':
                                direccion="%s/Imagenes/imgEstudiante/%s"%(str(os.getcwd()),str(self.carnetId.text()+extencion))
                                print(direccion)
                                shutil.copyfile(fileName,direccion)
                                self.dirrForoC=str(direccion)
                        else:
                                direccion="%s/Imagenes/imgClub/%s"%(str(os.getcwd()),str(self.clubs.text().upper()+extencion))
                                shutil.copyfile(fileName,direccion)
                                self.dirrFotoE=str(direccion)
        def loaderImg(self,ms,dirr):
                img=QPixmap.fromImage(QImage(dirr)).scaled(180,180,Qt.KeepAspectRatio)
                ms.setPixmap(img)
                ms.setAlignment(Qt.AlignCenter)
        def loadImgEs(self):
                fileName,_=QFileDialog.getOpenFileNames(self,u"Imagenes de los Estudiantes",QDir.currentPath())
                if fileName:
                        for i in range(len(fileName)):
                                try:
                                        shutil.move(str(fileName[i]),'%s/Imagenes/imgEstudiante/'%str(os.getcwd()))
                                except shutil.Error as e:
                                        cadena=str(e)[str(e).find('\'')+1:]
                                        os.remove(str(cadena[:cadena.find('\'')]))
                                        shutil.move(str(fileName[i]),'%s/Imagenes/imgEstudiante/'%str(os.getcwd()))
                        self.msges.mensageBueno('<h1>Imagenes de los Estudiantes Cargado</h1>')
        def loadImgClb(self):
                fileName,_=QFileDialog.getOpenFileNames(self,u"Imagen del club",QDir.currentPath())
                if fileName:
                        for i in range(len(fileName)):
                                try:
                                        shutil.move(str(fileName[i]),"%s/Imagenes/imgClub/"%str(os.getcwd()))
                                except shutil.Error as e:
                                        cadena=str(e)[str(e).find('\'')+1:]
                                        os.remove(str(cadena[:cadena.find('\'')]))
                                        shutil.move(str(fileName[i]),"%s/Imagenes/imgClub/"%str(os.getcwd()))
                        self.msges.mensageBueno('<h1>Imagen del Club Cargado</h1>')
        def introducirLista(self):
                tablas=["HombreCombate","MujerCombate","HombreForma","MujerForma",
                        "HombreRompimiento","MujerRompimiento"]
                tablas1=["EquiposHombre","EquiposMujer"]
                tablas2=["HombreRompimiento","MujerRompimiento"]
                tablas3=["HombreSND","MujerSND"]
                tablas4=["Hombre","Mujer"]
                fileName,_ = QFileDialog.getOpenFileName(self, "Open File",QDir.currentPath())
                if fileName.find(".db")>0:
                        cargo=sqlite3.connect(fileName)
                        cur1=cargo.cursor()
                        cur1.execute("SELECT * FROM Seguridad WHERE ID=0")
                        for l in cur1:
                                cur=cargo.cursor()
                                print("entro"+str(l[1]))
                                if int(l[1])==int(self.yearActual):             
                                        for i in range(len(tablas)):
                                                cur.execute("SELECT * FROM %s"%str(tablas[i]))
                                                for j in cur:
                                                        print(j[1])
                                                        self.cargaDato(j,str(tablas[i]))
                                        for i in range(len(tablas1)):
                                                cur.execute("SELECT * FROM %s"%str(tablas1[i]))
                                                for j in cur:
                                                        self.cargaDatoEq(j,str(tablas1[i]))
                                        for i in range(len(tablas2)):
                                                cur.execute("SELECT * FROM %s"%str(tablas2[i]))
                                                for j in cur:
                                                        self.cargaDatoTk(j,str(tablas2[i]))
                                        for i in range(len(tablas3)):
                                                cur.execute("SELECT * FROM %s"%str(tablas3[i]))
                                                for j in cur:
                                                        self.cargaDatoSND(j,str(tablas3[i]))
                                        for i in range(len(tablas4)):
                                                cur.execute("SELECT * FROM %s"%str(tablas4[i]))
                                                for j in cur:
                                                        self.cargaDatoG(j,str(tablas4[i]))
                                cur.close()
                        cargo.commit()
                        cur1.close()
                        self.msges.mensageBueno("<h1>Datos Cargados</h1>")
                else:
                        self.msges.mensageMalo("<h1>La seguridad de los\nDATOS no son fiables!</h1>")
        def cargaDatoG(self,data,tabla):
                cur=self.listaGeneral.cursor()
                cur.execute("SELECT * FROM %s WHERE ID=:c "%str(tabla),
                        {"c": str(data[0])})
                self.listaGeneral.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                cur.execute("DELETE FROM %s WHERE ID=:i"%tabla,{"i":str(data[0])})
                                cur.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?)"%tabla,data)
                                self.listaGeneral.commit()
                except TypeError:
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)"%tabla,data)
                        self.listaGeneral.commit()
                cur.close()
        def cargaDatoSND(self,data,tabla):
                cur=self.sndto.cursor()
                cur.execute("SELECT * FROM %s WHERE ID=:c AND Modo=:m"%str(tabla),
                        {"c": str(data[0]),"m":str(data[9])})
                self.sndto.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                cur.execute("DELETE FROM %s WHERE ID=:i AND Modo=:m"%tabla,{"i":str(data[0]),"m":str(data[9])})
                                cur.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?)"%tabla,data)
                                self.sndto.commit()
                except TypeError:
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?)"%tabla,data)
                        self.sndto.commit()
                cur.close()
        def cargaDatoEq(self,data,tabla):
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE Equipo=:c "%str(tabla),
                        {"c": str(data[0])})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                cur.execute("DELETE FROM %s WHERE Equipo=:i"%tabla,{"i":str(data[0])})
                                cur.execute("INSERT INTO %s VALUES (?,?,?)"%tabla,data)
                                self.datos.commit()
                except TypeError:
                        cur.execute("INSERT INTO %s VALUES(?,?,?)"%tabla,data)
                        self.datos.commit()
                cur.close()
        def cargaDatoTk(self,data,tabla):
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE ID=:c "%str(tabla),
                        {"c": str(data[0])})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                cur.execute("DELETE FROM %s WHERE ID=:i"%tabla,{"i":str(data[0])})
                                cur.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?)"%tabla,data)
                                self.datos.commit()
                except TypeError:
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?,?)"%tabla,data)
                        self.datos.commit()
                cur.close()
        def cargaDato(self,data,tabla):
                cur=self.datos.cursor()
                cur.execute("SELECT * FROM %s WHERE ID=:c "%str(tabla),
                        {"c": str(data[0])})
                self.datos.commit()
                row=cur.fetchone()
                try:
                        if len(row) is not None:
                                cur.execute("DELETE FROM %s WHERE ID=:i"%tabla,{"i":str(data[0])})
                                cur.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?)"%tabla,data)
                                self.datos.commit()
                except TypeError:
                        cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)"%tabla,data)
                        self.datos.commit()
                cur.close()
        def copyConf(self):
                fileName,_=QFileDialog.getSaveFileName(self,u"Guardar la Configuración",QDir.currentPath())
                if fileName:
                        direccion="%s/baseData/config.db"%self.dir
                        shutil.copyfile(direccion,str(fileName+'.db'))
                self.msges.mensageBueno("<h1>La Configuración fue Guardado..!!</h1>")