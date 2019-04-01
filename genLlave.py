#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3,llaver,snpelea,categorition

class generaLlave():
	def __init__(self,dire):
		self.dir=dire
		self.db=sqlite3.connect('%s/baseData/listCombate.db'%self.dir)
		self.formato=open('%s/baseData/formato.txt'%self.dir,'w')
		self.formato.close()
		self.formato=open('%s/baseData/formatoR.txt'%self.dir,'w')
		self.formato.close()
		self.formatoll=open('%s/baseData/llaves.txt'%self.dir,'w')
		self.formatoll.close()
		self.documentaPDF=llaver.crearLlavePdf()
		self.cnpeleas=snpelea.sinpeleaPDF(self.dir)
	def categorizar(self,cat,gen,lista,nombre,txt):
		self.formato=open('%s/baseData/%s.txt'%(self.dir,str(txt)),'a')
		self.formatoll=open('%s/baseData/llaves.txt'%self.dir,'a')
		point=self.db.cursor()
		datos=sqlite3.connect('%s'%nombre)
		grado=sqlite3.connect('%s/baseData/config.db'%self.dir)
		cur=grado.cursor()
		cur2=grado.cursor()
		cur3=datos.cursor()
		cur4=grado.cursor()
		cur.execute("SELECT Categoria,EdadIni,EdadFin FROM %s"%str(cat))
		for i in cur:
			cur2.execute("SELECT SubCat,PesoIni,PesoFin FROM %s"%str(str(i[0])+gen))
			for j in cur2:
				cur4.execute("SELECT nombre FROM grados")
				for g in cur4:
					cur3.execute("SELECT * FROM %s WHERE Categoria=:cat AND SubCat=:sct AND Cinturon=:grad"%str(lista),
						{"cat":str(i[0]),"sct":str(j[0]),"grad":str(g[0])})	
					uno=True
					for k in cur3:
						if uno:
							self.formato.write((str(i[0])+" "+str(i[1])+"-"+str(i[2]))+'/'+str(j[0])
								+" "+str(j[1])+"-"+str(j[2])+'/'+str(gen)+'/'+str(g[0])+'\n')
							llave=str(i[0])+str(j[0])+str(gen)+str(g[0])
							self.formatoll.write(llave+"-"+str(gen)+'\n')
							uno=False
							try:
								point.execute("DELETE FROM %s "%str(llave))
								self.db.commit()
							except:
								pass
						try:
							llave=str(i[0])+str(j[0])+str(gen)+str(g[0])
							infor=(k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8])
							'''self.formato.write(str(k[0])+','+unicode(k[1])+','+unicode(k[2])+','+
								str(k[3])+','+str(k[4])+','+str(k[5])+','+str(k[6])+','+str(k[7])+','+str(k[8]))
							self.formato.write('\n')'''
							point.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?)"%str(llave),infor)
							self.db.commit()
						except sqlite3.OperationalError:
							llave=str(i[0])+str(j[0])+str(gen)+str(g[0])
							point.execute('CREATE TABLE %s(ID TEXT,Nombre TEXT,Apellido TEXT,Edad INT,Peso REAL,Cinturon TEXT,Categoria TEXT,SubCat TEXT,Club TEXT)'%llave)
							infor=[k[0],k[1],k[2],k[3],k[4],k[5],k[6],k[7],k[8]]
							point.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?)"%str(llave),infor)
							self.db.commit()
		cur3.close()
		cur2.close()
		cur.close()
		point.close()
		datos.commit()
		datos.close()
		self.formato.close()
		self.formatoll.close()
	def limpiar(self,name):
		self.formato=open('%s/baseData/%s.txt'%(self.dir,name),'w')
		self.formato.close()	
	def generaPdf(self,name,txt):
		dato=categorition.listaCategorias(txt,self.dir)
		dato.salidaPDF(name)
	def generarLlaves(self,name,titulo):
		self.formatoll=open('%s/baseData/llaves.txt'%self.dir,'r')
		datos=self.formatoll.read()
		nombrell=[]
		genero=[]
		self.formatoll.close()
		while len(datos)!=0:
			nombrell.append(datos[0:datos.find('-')])
			genero.append(datos[datos.find('-')+1:datos.find('\n')])
			datos=datos[datos.find('\n')+1:]
		cur=self.db.cursor()
		for i in range(len(nombrell)):
			cur.execute("SELECT * FROM %s"%str(nombrell[i]))
			filas=cur.fetchall()
			caso=len(filas)
			if caso == 1:
				self.cnpeleas.sinPeleas(str(nombrell[i]),genero[i])
			elif caso>=2 and caso<=4:
				self.documentaPDF.llaveFord(filas,caso,genero[i],titulo)
			elif caso>=5 and caso<=8:
				self.documentaPDF.llaveEight(filas,caso,genero[i],titulo)
			elif caso>=9 and caso<=16:
				self.documentaPDF.llaveSixteen(filas,caso,genero[i],titulo)
			elif caso>=17 and caso<=32:
				pass
		cur.close()
		self.documentaPDF.salidaPDF(name,self.dir)
		self.cnpeleas.salidaPDF(name)
	def salirDb(self):
		self.db.close()
		self.cnpeleas.cerrarDB()
