#!/usr/bin/python
# -*- coding: utf-8 -*-
from fpdf import FPDF

class listaFormas(object):
	def __init__(self):
		super (listaFormas, self).__init__()
		self.doc=FPDF('L','mm','A4')
		self.doc.add_page()
		self.doc.set_font('Arial','BI',16)
		self.doc.cell(260,8,"Lista de Formas",0,0,'C')
		self.doc.ln(8)
	def header(self,data):
		self.doc.set_font('Arial','B',16)
		self.doc.ln(2)
		self.doc.cell(120,8,"Categoria: "+data[0]+" years",0,0,'L')
		self.doc.cell(100,8,"Genero: "+data[1],0,0,'L')
		self.doc.ln(8)
		self.doc.cell(120,8,"Grado: "+data[2],0,0,'L')
		self.doc.ln(8)
	def subTitulo(self,data):
		self.doc.set_font('Times','I',14)
		self.doc.cell(300,8,"Forma: "+data,0,0,'C')
		self.doc.ln(10)
		self.doc.cell(25,8,"ID",1,0,'C')
		self.doc.cell(47,8,"NOMBRE",1,0,'C')
		self.doc.cell(47,8,"APELLIDO",1,0,'C')
		self.doc.cell(16,8,"EDAD",1,0,'C')
		self.doc.cell(16,8,"PESO",1,0,'C')
		self.doc.cell(35,8,"CINTURON",1,0,'C')
		self.doc.cell(30,8,"CATEGORIA",1,0,'C')
		self.doc.cell(30,8,"FORMA",1,0,'C')
		self.doc.cell(25,8,"CLB",1,0,'C')
		self.doc.ln(8)
	def lista(self,data):
		self.doc.set_font('Times','I',14)
		self.doc.cell(25,8,data[0],1,0,'C')
		self.doc.cell(47,8,data[1],1,0,'C')
		self.doc.cell(47,8,data[2],1,0,'C')
		self.doc.cell(16,8,data[3],1,0,'C')
		self.doc.cell(16,8,data[4],1,0,'C')
		self.doc.cell(35,8,data[5],1,0,'C')
		self.doc.cell(30,8,data[6],1,0,'C')
		self.doc.cell(30,8,data[7],1,0,'C')
		self.doc.cell(25,8,data[8],1,0,'C')
		self.doc.ln(8)
	def salidaPDF(self,nombre):
		self.doc.output('C:/Registro/Documentos/formas%s.pdf'%str(nombre),'F')
