from fpdf import *
from random import randint
import sqlite3

class llaveTk5():
	def __init__(self,db):
		self.pdf=FPDF()
		self.pdf.add_page()
		self.pdf.set_font('Arial','B',18)
		self.pdf.cell(190,7,"Llaves tk5",0,0,'C')
		self.pdf.ln(8)
		self.db=sqlite3.connect(db)
	def subtitulo(self,subt):
		self.pdf.set_font('Arial','I',16)
		self.pdf.cell(50,6,("Genero:  "+str(subt)),1,0,'C')
	def generarTk(self):
		self.subtitulo("Hombres")
		self.generarLlave("EquiposHombre")
		self.pdf.add_page()
		self.subtitulo("Mujer")
		self.generarLlave("EquiposMujer")
	def generarLlave(self,tabla):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM %s"%str(tabla))
		filas=cur.fetchall()
		caso=len(filas)
		if caso>=2 and caso <=4:
			self.llaveFord(filas,caso)
		elif caso>4 and caso<=8:
			self.llaveEigth(filas,caso)
		elif caso>8 and caso<=16:
			self.llaveSixteen(filas,caso)
		self.db.commit()
		cur.close()
	def llaveFord(self,equipos,cantidad):
		self.pdf.set_line_width(0.7)
		self.pdf.set_xy(50,70)
		self.pdf.line(50,70,90,70)
		self.pdf.line(50,110,90,110)
		self.pdf.line(90,70,90,110)
		self.pdf.line(90,90,130,90)
		self.pdf.line(130,90,130,180)
		self.pdf.line(90,180,130,180)
		self.pdf.line(130,135,160,135)
		self.pdf.line(50,160,90,160)
		self.pdf.line(90,160,90,200)
		self.pdf.line(50,200,90,200)
		pos=[]
		for i in range(cantidad):
			pos.append(4-i)
		if cantidad==4:
			self.colocarF(equipos,pos)
		elif cantidad==3:
			self.llenarByte(1)
			self.colocarF(equipos,pos)
		elif cantidad==2:
			self.llenarByte(1)
			self.llenarByte(2)
			self.colocarF(equipos,pos)
	def colocarF(self,equipos,position):
		for i in equipos:
			lugar=randint(0,int(len(position)-1))
			self.ingresarNombreFord(i[0],position[lugar])
			position.pop(lugar)
	def ingresarNombreFord(self,dato,pos):
		if pos==1:
			self.pdf.set_xy(50,60)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(30,60,str(dato))
		elif pos==2:
			self.pdf.set_xy(50,190)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(30,190,str(dato))
		elif pos==3:
			self.pdf.set_xy(50,100)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(30,105,str(dato))
		elif pos==4:
			self.pdf.set_xy(50,150)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(30,155,str(dato))	
	def llaveEight(self,equipos,cantidad):
		self.pdf.set_line_width(0.8)
		self.pdf.add_page()
		self.pdf.set_xy(50,100)
		self.pdf.line(60,60,90,60)
		self.pdf.line(90,60,90,90)
		self.pdf.line(60,90,90,90)
		self.pdf.line(90,75,120,75)
		self.pdf.line(120,75,120,135)
		self.pdf.line(90,135,120,135)
		self.pdf.line(90,120,90,150)
		self.pdf.line(60,120,90,120)
		self.pdf.line(60,150,90,150)
		self.pdf.line(120,115,150,115)
		self.pdf.line(150,115,150,225)
		self.pdf.line(150,175,180,175)
		self.pdf.line(120,225,150,225)
		self.pdf.line(120,195,120,255)
		self.pdf.line(90,195,120,195)
		self.pdf.line(90,255,120,255)
		self.pdf.line(60,180,90,180)
		self.pdf.line(60,210,90,210)
		self.pdf.line(60,240,90,240)
		self.pdf.line(60,270,90,270)
		self.pdf.line(90,180,90,210)
		self.pdf.line(90,240,90,270)
		pos=[]
		for i in range(cantidad):
			pos.append(8-i)
		if cantidad==5:
			self.llenarByte(3)
			self.llenarByte(4)
			self.llenarByte(5)
			self.colocarE(equipos,pos)
		if cantidad==6:
			self.llenarByte(3)
			self.llenarByte(4)
			self.colocarE(equipos,pos)
		if cantidad==7:
			self.llenarByte(3)
			self.colocarE(equipos,pos)
		if cantidad==8:
			self.colocarE(equipos,pos)
	def colocarE(self,equipos,position):
		for i in equipos:
			lugar=randint(0,int(len(position)-1))
			self.ingresarNombreEigth(i[0],position[lugar])
			position.pop(lugar)
	def ingresarNombreEigth(self,dato,pos):
		if pos==1:
			self.pdf.set_xy(60,50)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(30,55,str(dato))
		if pos==2:
			self.pdf.set_xy(60,260)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(30,265,str(dato))
		if pos==3:
			self.pdf.set_xy(60,80)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(30,85,str(dato))
		if pos==4:
			self.pdf.set_xy(60,230)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(30,235,str(dato))
		if pos==5:
			self.pdf.set_xy(60,110)
			self.pdf.cell(5,5,"5",1,1,'C')
			self.pdf.text(30,115,str(dato))
		if pos==6:
			self.pdf.set_xy(60,200)
			self.pdf.cell(5,5,"6",1,1,'C')
			self.pdf.text(30,205,str(dato))
		if pos==7:
			self.pdf.set_xy(60,140)
			self.pdf.cell(5,5,"7",1,1,'C')
			self.pdf.text(30,145,str(dato))
		if pos==8:
			self.pdf.set_xy(60,170)
			self.pdf.cell(5,5,"8",1,1,'C')
			self.pdf.text(30,175,str(dato))
	def llaveSixteen(self,equipos,cantidad):
		self.pdf.set_font('arial','',13.0)
		self.pdf.set_line_width(1)
		self.pdf.add_page()
		for i in range(16):
			var=int(40+(15*i))
			darto=int(47+(30*i))
			darti=int(62+(60*i))
			darti2=int(92+(120*i))
			self.pdf.line(50,var,70,var)
			if i<8:	
				self.pdf.line(70,darto,100,darto)
				d=int(40+(30*i))
				self.pdf.line(70,d,70,d+15)
			if i<4:
				self.pdf.line(100,darti,130,darti)
				c=int(47+(60*i))
				self.pdf.line(100,c,100,c+30)
			if i<2:
				self.pdf.line(130,darti2,160,darti2)
				d=int(62+(120*i))
				self.pdf.line(130,d,130,d+60)
			if i==0:
				self.pdf.line(160,92,160,212)
				self.pdf.line(160,152,180,152)
		self.pdf.set_line_width(0.5)
		pos=[]
		for i in range(cantidad):
			pos.append(16-i)
		if cantidad==9:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.llenarByte(10)
			self.llenarByte(11)
			self.llenarByte(12)
			self.colocarS(equipos,pos)
		if cantidad==10:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.llenarByte(10)
			self.llenarByte(11)
			self.colocarS(equipos,pos)
		if cantidad==11:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.llenarByte(10)
			self.colocarS(equipos,pos)
		if cantidad==12:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.colocarS(equipos,pos)
		if cantidad==13:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.colocarS(equipos,pos)
		if cantidad==14:
			self.llenarByte(6)
			self.llenarByte(7)
			self.colocarS(equipos,pos)
		if cantidad==15:
			self.llenarByte(6)
			self.colocarS(equipos,pos)
		if cantidad==16:
			self.colocarS(equipos,pos)
	def colocarS(self,equipos,position):
		for i in equipos:
			lugar=randint(0,int(len(position)-1))
			self.ingresarNombreSexteen(i[0],position[lugar])
			position.pop(lugar)
	def ingresarNombreSixteen(self,dato,pos):
		if pos==1:
			self.pdf.set_xy(50,33)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(10,35,str(dato))
		if pos==2:
			self.pdf.set_xy(50,258)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(10,260,str(dato))
		if pos==3:
			self.pdf.set_xy(50,48)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(10,45,str(dato))
		if pos==4:
			self.pdf.set_xy(50,243)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(10,245,str(dato))
		if pos==5:
			self.pdf.set_xy(50,63)
			self.pdf.cell(5,5,"5",1,1,'C')
			self.pdf.text(20,65,str(dato))
		if pos==6:
			self.pdf.set_xy(50,228)
			self.pdf.cell(5,5,"6",1,1,'C')
			self.pdf.text(10,230,str(dato))
		if pos==7:
			self.pdf.set_xy(50,78)
			self.pdf.cell(5,5,"7",1,1,'C')
			self.pdf.text(10,80,str(dato))
		if pos==8:
			self.pdf.set_xy(50,213)
			self.pdf.cell(5,5,"8",1,1,'C')
			self.pdf.text(10,215,str(dato))
		if pos==9:
			self.pdf.set_xy(50,93)
			self.pdf.cell(5,5,"9",1,1,'C')
			self.pdf.text(10,95,str(dato))
		if pos==10:
			self.pdf.set_xy(50,198)
			self.pdf.cell(5,5,"10",1,1,'C')
			self.pdf.text(10,200,str(dato))
		if pos==11:
			self.pdf.set_xy(50,108)
			self.pdf.cell(5,5,"11",1,1,'C')
			self.pdf.text(10,110,str(dato))
		if pos==12:
			self.pdf.set_xy(50,183)
			self.pdf.cell(5,5,"12",1,1,'C')
			self.pdf.text(10,185,str(dato))
		if pos==13:
			self.pdf.set_xy(50,123)
			self.pdf.cell(5,5,"13",1,1,'C')
			self.pdf.text(10,125,str(dato))
		if pos==14:
			self.pdf.set_xy(50,168)
			self.pdf.cell(5,5,"14",1,1,'C')
			self.pdf.text(10,170,str(dato))
		if pos==15:
			self.pdf.set_xy(50,138)
			self.pdf.cell(5,5,"15",1,1,'C')
			self.pdf.text(10,140,str(dato))
		if pos==16:
			self.pdf.set_xy(50,153)
			self.pdf.cell(5,5,"16",1,1,'C')
			self.pdf.text(10,155,str(dato))
	def llenarByte(self,pos):
		if pos==1:
			self.pdf.set_xy(50,60)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(30,70,"BYE")
		if pos==2:
			self.pdf.set_xy(50,190)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(30,200,"BYE")
		if pos==3:
			self.pdf.set_xy(60,50)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(50,60,"BYE")
		if pos==4:
			self.pdf.set_xy(60,260)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(50,270,"BYE")
		if pos==5:
			self.pdf.set_xy(60,80)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(50,90,"BYE")
		if pos==6:
			self.pdf.set_xy(50,33)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(20,40,"BYE")
		if pos==7:
			self.pdf.set_xy(50,258)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(20,265,"BYE")
		if pos==8:
			self.pdf.set_xy(50,48)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(20,55,"BYE")
		if pos==9:
			self.pdf.set_xy(50,243)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(20,250,"BYE")
		if pos==10:
			self.pdf.set_xy(50,63)
			self.pdf.cell(5,5,"5",1,1,'C')
			self.pdf.text(20,70,"BYE")
		if pos==11:
			self.pdf.set_xy(50,228)
			self.pdf.cell(5,5,"6",1,1,'C')
			self.pdf.text(20,235,"BYE")
		if pos==12:
			self.pdf.set_xy(50,93)
			self.pdf.cell(5,5,"7",1,1,'C')
			self.pdf.text(20,100,"BYE")
	def salidaPDF(self,nombre):
		self.pdf.output('C:/Registro/Documentos/llavestk5%s.pdf'%nombre,'F')
		self.db.close()
