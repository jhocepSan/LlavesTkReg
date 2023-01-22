from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3,os,formaPDF

class forma():
	def __init__(self,dire=""):
		self.dirr=dire
		self.dir='%s/baseData/listForm.db'%self.dirr
		if os.path.exists(self.dir):
			os.remove(self.dir)
		self.db=sqlite3.connect(self.dir)
		self.crearTabla()
	def clasificarForma(self,cat,gen,part,dbe):
		lParti=sqlite3.connect(dbe)
		lConf=sqlite3.connect('%s/baseData/config.db'%self.dirr)
		cur=lConf.cursor()
		cur2=lConf.cursor()
		cur3=lParti.cursor()
		cur4=self.db.cursor()
		cur5=self.db.cursor()
		cur.execute("SELECT * FROM %s"%str(cat))
		for i in cur:
			cur2.execute("SELECT * FROM Pumse")
			for j in cur2:
				cur3.execute("SELECT * FROM %s WHERE Categoria=:cat"%str(part),
					{"cat":str(i[0])})
				primero=True
				for k in cur3:
					tabla=str(gen)+str(i[0])+str(j[0])
					datos=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8]]
					datosT=[tabla,gen,i[0],i[1],i[2],j[0],j[1]]
					cur4.execute('CREATE TABLE IF NOT EXISTS %s(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso INT,Cinturon TEXT,Categoria TEXT,Forma TEXT,Club TEXT)'%tabla)
					if primero:
						cur4.execute('DELETE FROM %s'%tabla)
						self.db.commit()
						primero=False
					cur4.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?,?,?)"%tabla,datos)
					self.db.commit()
					cur5.execute("SELECT * FROM Formas WHERE Nombre=:nom",{"nom":str(tabla)})
					self.db.commit()
					row=cur5.fetchone()
					try:
						if len(row) is not None:
							aux=[gen,i[0],i[1],i[2],j[0],j[1],tabla]
							cur5.execute("UPDATE Formas SET Genero=?,Categoria=?,EdadIni=?,EdadFin=?,Grado=?,Forma=? WHERE Nombre=?",aux)
					except TypeError:
						cur5.execute("INSERT INTO Formas VALUES(?,?,?,?,?,?,?)",datosT)
					self.db.commit()
		cur5.close()
		cur4.close()
		cur3.close()
		cur2.close()
		cur.close()
		lParti.close()
		lConf.close()
	def separaForma(self,nombre):
		pdf=formaPDF.listaFormas()
		cur=self.db.cursor()
		cur2=self.db.cursor()
		cur.execute("SELECT * FROM Formas")
		for i in cur:
			data=[str(i[2])+" "+str(i[3])+"-"+str(i[4]),str(i[1]),str(i[5])]
			formas=str(i[6]).split(',')
			for k in range(len(formas)):
				pdf.header(data)
				primero=True
				cur2.execute("SELECT * FROM %s"%str(i[0]))
				for j in cur2:
					if j[7].find(str(formas[k]))>-1:
						if primero:
							pdf.subTitulo(formas[k])
							primero=False
						inf=[str(j[0]),unicode(j[1]),unicode(j[2]),str(j[3]),str(j[4]),str(j[5]),
							str(j[6]),str(j[7]),str(j[8])]
						pdf.lista(inf)
		cur.close()
		cur2.close()	
		pdf.salidaPDF(nombre,self.dirr)				
	def crearTabla(self):
		cur=self.db.cursor()
		cur.execute('CREATE TABLE IF NOT EXISTS Formas(Nombre TEXT,Genero TEXT,Categoria TEXT,EdadIni INT,EdadFin INT,Grado TEXT,Forma TEXT)')
		self.db.commit()
		cur.close()
	def cerrarDB(self):
		self.db.close()
