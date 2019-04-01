from fpdf import FPDF
import sqlite3
import os.path as path

class genPDF(object):
    def __init__(self,dire):
        self.snp=FPDF(orientation = 'P', unit = 'mm', format='A4')
        self.snp.set_line_width(0.3)
        self.header()
        self.dir=dire
    def header(self,titulo):
        self.snp.set_font('arial','',7)
        self.snp.add_page()
        self.snp.set_xy(70,10)
        self.snp.cell(60,5,"ESTUDIANTES",0,0,'C')
        self.snp.ln(7)
        self.snp.cell(12,5,"ID",1,0,'C')
        self.snp.cell(28,5,"NOMBRES",1,0,'C')
        self.snp.cell(40,5,"APELLIDOS",1,0,'C')
        self.snp.cell(8,5,"EDAD",1,0,'C')
        self.snp.cell(8,5,"PESO",1,0,'C')
        self.snp.cell(30,5,"CATEGORIA",1,0,'C')
        self.snp.cell(35,5,"SUBCATEGORIA",1,0,'C')
        self.snp.cell(15,5,"CINTURON",1,0,'C')
        self.snp.cell(15,5,"CLB",1,0,'C')
        self.snp.ln(5)
    def sinPeleas(self,name,genero):
        cur=self.db.cursor()
        cur.execute("SELECT * FROM %s"%str(name))
        self.snp.set_font('Times','',7)
        for i in cur:
            cur2=self.cnf.execute("SELECT * FROM %s WHERE SubCat=:cat"%str(i[6]+genero),{'cat':str(i[7])})
            for j in cur2:
                categoria=''
                if genero.find('H')>=0:
                    categoria='CategoriaH'
                else:
                    categoria='CategoriaM'
                cur3=self.cnf.execute("SELECT * FROM %s WHERE Categoria=:cate"%str(categoria),{'cate':str(i[6])})
                for k in cur3:
                    self.snp.cell(12,5,str(i[0]),1,0,'C')
                    self.snp.cell(28,5,unicode(i[1]),1,0,'C')
                    self.snp.cell(40,5,unicode(i[2]),1,0,'C')
                    self.snp.cell(8,5,str(i[3]),1,0,'C')
                    self.snp.cell(8,5,str(i[4]),1,0,'C')
                    self.snp.cell(30,5,str(i[6]+" "+unicode(k[1])+"-"+unicode(k[2])),1,0,'C')
                    self.snp.cell(35,5,str(i[7]+" "+unicode(j[1])+"-"+unicode(j[2])),1,0,'C')
                    self.snp.cell(15,5,str(i[5]),1,0,'C')
                    self.snp.cell(15,5,str(i[8]),1,0,'C')
                    self.snp.ln(5)
                cur3.close()
            cur2.close()
        cur.close()
        self.db.commit()
    def salidaPDF(self,name):
        self.snp.output('%s/Documentos/listaSinPelea%s.pdf'%(self.dir,name),'F')
    def cerrarDB(self):
        self.cnf.close()
        self.db.close()
