from fpdf import *
import sqlite3
import os.path as path
'''
	clase para generar pdf de estudiantes sin documento
'''
class listaPartPDF(object):
	def __init__(self,dire):
		self.doc=FPDF(orientation = 'L', unit = 'mm', format='A4')
		self.dir=dire
		name='%s/baseData/sinDoc.db'%self.dir
		self.db=sqlite3.connect(name)
		self.doc.set_font('arial','',19.0)
		self.doc.set_line_width(0.5)
		self.header()
	def header(self):
		self.doc.add_page()
		self.doc.set_xy(50,10)
		self.doc.cell(120,6,"SIN DOCUMENTOS",1,0,'C')
		self.doc.ln(10)
	def subTitle(self,genero):
		self.doc.set_font('times','',10.0)
		self.doc.cell(50,5,"Genero: %s"%str(genero[:genero.find('S')]),0,0,'C')
		self.doc.ln(6)
		self.doc.cell(20,5,"ID",1,0,'C')
		self.doc.cell(42,5,"NOMBRE",1,0,'C')
		self.doc.cell(42,5,"APELLIDO",1,0,'C')
		self.doc.cell(13,5,"EDAD",1,0,'C')
		self.doc.cell(13,5,"PESO",1,0,'C')
		self.doc.cell(25,5,"CINTURON",1,0,'C')
		self.doc.cell(30,5,"CATEGORIA",1,0,'C')
		self.doc.cell(30,5,"EQ/FRM/SUBc",1,0,'C')
		self.doc.cell(25,5,"CLB",1,0,'C')
		self.doc.cell(25,5,"MODO",1,0,'C')
		self.doc.ln(5)
	def generaPDF(self):
		tabla=["HombreSND","MujerSND"]
		cur=self.db.cursor()
		cabezera=False
		for j in range(2):
			cur.execute("SELECT * FROM %s"%str(tabla[j]))
			cabezera=True
			for i in cur:
				if cabezera==True:
					self.subTitle(tabla[j])
					cabezera=False
				self.doc.cell(20,5,str(i[0]),1,0,'C')
				self.doc.cell(42,5,unicode(i[1]),1,0,'C')
				self.doc.cell(42,5,unicode(i[2]),1,0,'C')
				self.doc.cell(13,5,str(i[3]),1,0,'C')
				self.doc.cell(13,5,str(i[4]),1,0,'C')
				self.doc.cell(25,5,str(i[5]),1,0,'C')
				self.doc.cell(30,5,str(i[6]),1,0,'C')
				self.doc.cell(30,5,str(i[7]),1,0,'C')
				self.doc.cell(25,5,str(i[8]),1,0,'C')
				self.doc.cell(25,5,str(i[9]),1,0,'C')
				self.doc.ln(5)
		cur.close()
		self.db.commit()
	def salidaPDF(self,name):
		self.doc.output('%s/Documentos/sinDocument%s.pdf'%(self.dir,name),'F')
		self.db.close()
