from fpdf import FPDF
import sqlite3
import os.path as path

class listaPDF(object):
    def __init__(self,nombre):
        self.snp=FPDF(orientation = 'P', unit = 'mm', format='A4')
        self.snp.set_line_width(0.3)
        self.db=sqlite3.connect(nombre)
        self.snp.add_page()
    def header(self,nom):
        self.snp.set_font('arial','',7)
        self.snp.ln(7)
        self.snp.set_x(70)
        self.snp.cell(60,5,"ESTUDIANTES %s"%nom,0,0,'C')
        self.snp.ln(7)
        self.snp.cell(12,5,"N*",1,0,'C')
        self.snp.cell(12,5,"ID",1,0,'C')
        self.snp.cell(28,5,"NOMBRES",1,0,'C')
        self.snp.cell(40,5,"APELLIDOS",1,0,'C')
        self.snp.cell(8,5,"EDAD",1,0,'C')
        self.snp.cell(8,5,"PESO",1,0,'C')
        self.snp.cell(15,5,"CINTURON",1,0,'C')
        self.snp.cell(15,5,"CLB",1,0,'C')
        self.snp.ln(5)
    def listaEstudiante(self,genero,nombres):
        self.header(nombres)
        cur=self.db.cursor()
        cur.execute("SELECT * FROM %s"%str(genero))
        self.snp.set_font('Times','',7)
        cont=0
        for i in cur:
            self.snp.cell(12,5,str(cont),1,0,'C')
            self.snp.cell(12,5,str(i[0]),1,0,'C')
            self.snp.cell(28,5,unicode(i[1]),1,0,'C')
            self.snp.cell(40,5,unicode(i[2]),1,0,'C')
            self.snp.cell(8,5,str(i[3]),1,0,'C')
            self.snp.cell(8,5,str(i[4]),1,0,'C')
            self.snp.cell(15,5,str(i[5]),1,0,'C')
            self.snp.cell(15,5,str(i[6]),1,0,'C')
            self.snp.ln(5)
            cont+=1
        cur.close()
        self.db.commit()
    def salidaPDF(self,dire,name):
        self.snp.output('%s/Documentos/listaGeneral%s.pdf'%(dire,name),'F')
    def cerrarDB(self):
        self.db.close()
