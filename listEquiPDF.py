#!/usr/bin/python
# -*- coding: utf-8 -*-
import os.path as path
from fpdf import FPDF
import sqlite3

class listEquiPdf(object):
	def __init__(self,db):
		super(listEquiPdf,self).__init__()
		self.pdf=FPDF('L','mm','A4')
		self.pdf.add_page()
		self.pdf.set_font('Arial','B',16)
		self.pdf.cell(260,4,"Lista Equipos TK5",0,0,'C')
		self.pdf.ln(7)
		self.db=sqlite3.connect(db)
	def subtitulo(self,equipo,genero):
		self.pdf.set_font('Arial','BI',16)
		self.pdf.cell(50,6,("Equipo:  "+str(equipo)),1,0,'L')
		self.pdf.cell(50,6,("Genero:  "+str(genero)),1,0,'L')
		self.pdf.ln(6)
		self.pdf.cell(25,8,"ID",1,0,'C')
		self.pdf.cell(47,8,"NOMBRE",1,0,'C')
		self.pdf.cell(47,8,"APELLIDO",1,0,'C')
		self.pdf.cell(16,8,"EDAD",1,0,'C')
		self.pdf.cell(16,8,"PESO",1,0,'C')
		self.pdf.cell(40,8,"CINTURON",1,0,'C')
		self.pdf.cell(35,8,"CATEGORIA",1,0,'C')
		self.pdf.cell(25,8,"EQUIPO",1,0,'C')
		self.pdf.cell(25,8,"CLB",1,0,'C')
		self.pdf.ln(8)
	def enlistarEquipo(self,lista,tabla,genero):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM %s"%str(tabla))
		cur2=self.db.cursor()
		for i in cur:
			if i[1]==5 and i[2]==1:
				self.subtitulo(str(i[0]),genero)
				cur2.execute("SELECT * FROM %s WHERE Equipo=:eq"%str(lista),{"eq":str(i[0])})
				for j in cur2:
					self.pdf.set_font("Times",'I',16)
					self.pdf.cell(25,8,str(j[0]),1,0,'C')
					self.pdf.cell(47,8,str(j[1]),1,0,'C')
					self.pdf.cell(47,8,str(j[2]),1,0,'C')
					self.pdf.cell(16,8,str(j[3]),1,0,'C')
					self.pdf.cell(16,8,str(j[4]),1,0,'C')
					self.pdf.cell(40,8,str(j[5]),1,0,'C')
					self.pdf.cell(35,8,str(j[6]),1,0,'C')
					self.pdf.cell(25,8,str(j[7]),1,0,'C')
					self.pdf.cell(25,8,str(j[8]),1,0,'C')
					self.pdf.ln(8)
			else:
				self.descalificado(str(i[0]),genero)
		self.db.commit()
		cur.close()
		cur2.close()
	def descalificado(self,equipo,genero):
		self.pdf.set_font('Arial','BI',16)
		self.pdf.cell(50,6,("Equipo:  "+str(equipo)),1,0,'L')
		self.pdf.cell(50,6,("Genero:  "+str(genero)),1,0,'L')
		self.pdf.cell(150,6,"DESCALIFICADO POR NO TENER EQUIPO COMPLETO",1,0,'L')
		self.pdf.ln(6)
	def salidaPDF(self,nombre,dire):
		self.pdf.output('%s/Documentos/listaEquipos%s.pdf'%(dire,nombre),'F')
		self.db.close()


		
