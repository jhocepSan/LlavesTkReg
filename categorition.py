#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path as path
import sqlite3
from fpdf import FPDF

class listaCategorias():
	"""docstring for listaCategorias"""
	def __init__(self,txt,dire):
		#super (listaCategorias, self).__init__()
		self.doc=FPDF('P','mm','A4')
		self.doc.add_page()
		self.dir=dire
		formato=open('%s/baseData/%s.txt'%(self.dir,str(txt)),'r')
		self.estudiantes=sqlite3.connect('%s/baseData/listCombate.db'%self.dir)
		self.formato=formato.read().split('\n')
		formato.close()
		for i in range(len(self.formato)):
			if self.formato[i].find('/')>=0:
				cabecera=self.formato[i].split('/')
				self.header(cabecera)
				tabla=cabecera[0][:cabecera[0].find(' ')]+cabecera[1][:cabecera[1].find(' ')]+cabecera[2]+cabecera[3]
				cur=self.estudiantes.cursor()
				cur.execute("SELECT * FROM %s"%str(tabla))
				for i in cur:
					self.lista(i)
				cur.close()
		self.estudiantes.commit()
	def header(self,data):
		self.doc.set_font('Arial','B',10)
		self.doc.ln(2)
		self.doc.cell(120,6,"Categoria: "+data[0]+u" Años",0,0,'L')
		self.doc.cell(100,6,"Genero: "+data[2],0,0,'L')
		self.doc.ln(6)
		self.doc.cell(120,6,"SubCategoria: "+data[1]+" kg",0,0,'L')
		self.doc.cell(100,6,"Cinturon: "+data[3],'L')
		self.doc.ln(6)
	def lista(self,data):
		self.doc.set_font('Times','I',9)
		self.doc.cell(15,6,str(data[0]),1,0,'C')
		self.doc.cell(30,6,unicode(data[1]),1,0,'C')
		self.doc.cell(40,6,unicode(data[2]),1,0,'C')
		self.doc.cell(9,6,str(data[3]),1,0,'C')
		self.doc.cell(9,6,str(data[4]),1,0,'C')
		self.doc.cell(25,6,str(data[5]),1,0,'C')
		self.doc.cell(20,6,str(data[6]),1,0,'C')
		self.doc.cell(20,6,str(data[7]),1,0,'C')
		self.doc.cell(20,6,str(data[8]),1,0,'C')
		self.doc.ln(6)
	def salidaPDF(self,name):
		self.doc.output('%s/Documentos/%s.pdf'%(self.dir,name),'F')

