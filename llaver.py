from fpdf import *
from random import randint
class crearLlavePdf():
	def __init__(self):
		self.pdf=FPDF()
	def titulo(self,titulo):
		self.pdf.set_font('Arial','B',17)
		self.pdf.set_xy(2,40)
		self.pdf.cell(190,7,("Llaves de "+str(titulo)),0,0,'C')
	def header(self,cat,subcat,genero,cinturon):
		self.pdf.set_font('arial','',12.0)
		self.pdf.set_line_width(0.5)
		self.pdf.set_xy(40,50)
		self.pdf.cell(30,10, 'Categoria:', 0, 0, 'L')
		self.pdf.cell(60,10,str(cat),0,0,'L')
		self.pdf.cell(30,10,'Sub-Categoria:',0,0,'L')
		self.pdf.cell(60,10,str(subcat),0,0,'L')
		self.pdf.set_xy(40,60)
		self.pdf.cell(30, 10, 'Cinturon:', 0, 0, 'L')
		self.pdf.cell(60,10,str(cinturon),0,0,'L')
		self.pdf.cell(30,10,'Genero:',0,0,'L')
		self.pdf.cell(60,10,str(genero),0,0,'L')
		self.pdf.ln(10)
	def llaveFord(self,dato,participan,gen,titulo):
		self.pdf.set_font('arial','',14.0)
		self.pdf.set_line_width(0.5)
		self.pdf.add_page()
		self.titulo(titulo)
		self.pdf.set_xy(70,90)
		self.pdf.line(70,90,110,90)
		self.pdf.line(70,130,110,130)
		self.pdf.line(70,180,110,180)
		self.pdf.line(70,220,110,220)
		self.pdf.line(110,90,110,130)
		self.pdf.line(110,180,110,220)
		self.pdf.line(110,110,150,110)
		self.pdf.line(110,200,150,200)
		self.pdf.line(150,110,150,200)
		self.pdf.line(150,155,190,155)
		pos=[]
		for j in range(participan):
			pos.append(4-j)
		if participan==2:
			self.llenarByte(1)
			self.llenarByte(2)
			self.colocarF(dato,pos,gen)
		elif participan==3:
			self.llenarByte(1)
			self.colocarF(dato,pos,gen)
		elif participan==4:	
			self.colocarF(dato,pos,gen)
	def llenarByte(self,pos):
		if pos==1:
			self.pdf.set_xy(70,85)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(50,90,"BYE")
		if pos==2:
			self.pdf.set_xy(70,215)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(50,220,"BYE")
		if pos==3:
			self.pdf.set_xy(60,130)
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
	def ingresarNombreFord(self,dato,pos):
		if pos==1:
			self.pdf.set_xy(70,85)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(20,85,unicode(dato[0]))
			self.pdf.text(20,90,unicode(dato[1]))
			self.pdf.text(20,95,unicode(dato[2]))
		elif pos==2:
			self.pdf.set_xy(70,215)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(20,215,unicode(dato[0]))
			self.pdf.text(20,220,unicode(dato[1]))
			self.pdf.text(20,225,unicode(dato[2]))
		elif pos==3:
			self.pdf.set_xy(70,125)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(20,125,unicode(dato[0]))
			self.pdf.text(20,130,unicode(dato[1]))
			self.pdf.text(20,135,unicode(dato[2]))
		elif pos==4:
			self.pdf.set_xy(70,175)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(20,175,unicode(dato[0]))
			self.pdf.text(20,180,unicode(dato[1]))
			self.pdf.text(20,185,unicode(dato[2]))
	def llaveEight(self,dato,parti,gen,titulo):
		self.pdf.set_font('arial','',14.0)
		self.pdf.set_line_width(0.8)
		self.pdf.add_page()
		self.titulo(titulo)
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
		for i in range(parti):
			pos.append(8-i)
		if parti==5:
			self.llenarByte(3)
			self.llenarByte(4)
			self.llenarByte(5)
			self.colocarE(dato,pos,gen)
		if parti==6:
			self.llenarByte(3)
			self.llenarByte(4)
			self.colocarE(dato,pos,gen)
		if parti==7:
			self.llenarByte(3)
			self.colocarE(dato,pos,gen)
		if parti==8:
			self.colocarE(dato,pos,gen)
	def ingresarNombreEigth(self,dato,pos):
		if pos==1:
			self.pdf.set_xy(60,50)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(20,50,unicode(dato[0]))
			self.pdf.text(20,55,unicode(dato[1]))
			self.pdf.text(20,60,unicode(dato[2]))
		if pos==2:
			self.pdf.set_xy(60,260)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(20,260,unicode(dato[0]))
			self.pdf.text(20,265,unicode(dato[1]))
			self.pdf.text(20,270,unicode(dato[2]))
		if pos==3:
			self.pdf.set_xy(60,80)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(20,80,unicode(dato[0]))
			self.pdf.text(20,85,unicode(dato[1]))
			self.pdf.text(20,90,unicode(dato[2]))
		if pos==4:
			self.pdf.set_xy(60,230)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(20,230,unicode(dato[0]))
			self.pdf.text(20,235,unicode(dato[1]))
			self.pdf.text(20,240,unicode(dato[2]))
		if pos==5:
			self.pdf.set_xy(60,110)
			self.pdf.cell(5,5,"5",1,1,'C')
			self.pdf.text(30,110,unicode(dato[0]))
			self.pdf.text(30,115,unicode(dato[1]))
			self.pdf.text(30,120,unicode(dato[2]))
		if pos==6:
			self.pdf.set_xy(60,200)
			self.pdf.cell(5,5,"6",1,1,'C')
			self.pdf.text(20,200,unicode(dato[0]))
			self.pdf.text(20,205,unicode(dato[1]))
			self.pdf.text(20,210,unicode(dato[2]))
		if pos==7:
			self.pdf.set_xy(60,140)
			self.pdf.cell(5,5,"7",1,1,'C')
			self.pdf.text(20,140,unicode(dato[0]))
			self.pdf.text(20,145,unicode(dato[1]))
			self.pdf.text(20,150,unicode(dato[2]))
		if pos==8:
			self.pdf.set_xy(60,170)
			self.pdf.cell(5,5,"8",1,1,'C')
			self.pdf.text(20,170,unicode(dato[0]))
			self.pdf.text(20,175,unicode(dato[1]))
			self.pdf.text(20,180,unicode(dato[2]))
	def llaveSixteen(self,dato,num,gen,titulo):
		self.pdf.set_font('arial','',13.0)
		self.pdf.set_line_width(1)
		self.pdf.add_page()
		self.titulo(titulo)
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
		for i in range(num):
			pos.append(16-i)
		if num==9:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.llenarByte(10)
			self.llenarByte(11)
			self.llenarByte(12)
			self.colocarS(dato,pos,gen)
		if num==10:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.llenarByte(10)
			self.llenarByte(11)
			self.colocarS(dato,pos,gen)
		if num==11:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.llenarByte(10)
			self.colocarS(dato,pos,gen)
		if num==12:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.llenarByte(9)
			self.colocarS(dato,pos,gen)
		if num==13:
			self.llenarByte(6)
			self.llenarByte(7)
			self.llenarByte(8)
			self.colocarS(dato,pos,gen)
		if num==14:
			self.llenarByte(6)
			self.llenarByte(7)
			self.colocarS(dato,pos,gen)
		if num==15:
			self.llenarByte(6)
			self.colocarS(dato,pos,gen)
		if num==16:
			self.colocarS(dato,pos,gen)
	def colocarF(self,dato,pos,gen):
		ini=True
		for i in dato:
			if ini:
				self.header(str(i[6]),str(i[7]),str(gen),str(i[5]))
				ini=False
			lugar=randint(0,int(len(pos)-1))
			self.ingresarNombreFord([i[1],i[2],i[8]],pos[lugar])
			pos.pop(lugar)
			if len(pos)==0:
				break
	def colocarE(self,dato,pos,gen):
		ini=True
		for i in dato:
			if ini:
				self.header(str(i[6]),str(i[7]),str(gen),str(i[5]))
				ini=False
			lugar=randint(0,int(len(pos)-1))
			self.ingresarNombreEigth([i[1],i[2],i[8]],pos[lugar])
			pos.pop(lugar)
			if len(pos)==0:
				break
	def colocarS(self,dato,pos,gen):
		ini=True
		for i in dato:
			if ini:
				self.header(str(i[6]),str(i[7]),str(gen),str(i[5]))
				ini=False
			lugar=randint(0,int(len(pos)-1))
			self.ingresarNombreSixteen([i[1],i[2],i[8]],pos[lugar])
			pos.pop(lugar)
			if len(pos)==0:
				break
	def ingresarNombreSixteen(self,dato,pos):
		if pos==1:
			self.pdf.set_xy(50,33)
			self.pdf.cell(5,5,"1",1,1,'C')
			self.pdf.text(10,35,unicode(dato[0]))
			self.pdf.text(10,40,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==2:
			self.pdf.set_xy(50,258)
			self.pdf.cell(5,5,"2",1,1,'C')
			self.pdf.text(10,260,unicode(dato[0]))
			self.pdf.text(10,265,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==3:
			self.pdf.set_xy(50,48)
			self.pdf.cell(5,5,"3",1,1,'C')
			self.pdf.text(10,45,unicode(dato[0]))
			self.pdf.text(10,50,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==4:
			self.pdf.set_xy(50,243)
			self.pdf.cell(5,5,"4",1,1,'C')
			self.pdf.text(10,245,unicode(dato[0]))
			self.pdf.text(10,250,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==5:
			self.pdf.set_xy(50,63)
			self.pdf.cell(5,5,"5",1,1,'C')
			self.pdf.text(20,65,unicode(dato[0]))
			self.pdf.text(20,70,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==6:
			self.pdf.set_xy(50,228)
			self.pdf.cell(5,5,"6",1,1,'C')
			self.pdf.text(10,230,unicode(dato[0]))
			self.pdf.text(10,235,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==7:
			self.pdf.set_xy(50,78)
			self.pdf.cell(5,5,"7",1,1,'C')
			self.pdf.text(10,80,unicode(dato[0]))
			self.pdf.text(10,85,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==8:
			self.pdf.set_xy(50,213)
			self.pdf.cell(5,5,"8",1,1,'C')
			self.pdf.text(10,215,unicode(dato[0]))
			self.pdf.text(10,220,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==9:
			self.pdf.set_xy(50,93)
			self.pdf.cell(5,5,"9",1,1,'C')
			self.pdf.text(10,95,unicode(dato[0]))
			self.pdf.text(10,100,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==10:
			self.pdf.set_xy(50,198)
			self.pdf.cell(5,5,"10",1,1,'C')
			self.pdf.text(10,200,unicode(dato[0]))
			self.pdf.text(10,205,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==11:
			self.pdf.set_xy(50,108)
			self.pdf.cell(5,5,"11",1,1,'C')
			self.pdf.text(10,110,unicode(dato[0]))
			self.pdf.text(10,115,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==12:
			self.pdf.set_xy(50,183)
			self.pdf.cell(5,5,"12",1,1,'C')
			self.pdf.text(10,185,unicode(dato[0]))
			self.pdf.text(10,190,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==13:
			self.pdf.set_xy(50,123)
			self.pdf.cell(5,5,"13",1,1,'C')
			self.pdf.text(10,125,unicode(dato[0]))
			self.pdf.text(10,130,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==14:
			self.pdf.set_xy(50,168)
			self.pdf.cell(5,5,"14",1,1,'C')
			self.pdf.text(10,170,unicode(dato[0]))
			self.pdf.text(10,175,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==15:
			self.pdf.set_xy(50,138)
			self.pdf.cell(5,5,"15",1,1,'C')
			self.pdf.text(10,140,unicode(dato[0]))
			self.pdf.text(10,145,unicode(dato[1])+" "+unicode(dato[2]))
		if pos==16:
			self.pdf.set_xy(50,153)
			self.pdf.cell(5,5,"16",1,1,'C')
			self.pdf.text(10,155,unicode(dato[0]))
			self.pdf.text(10,160,unicode(dato[1])+" "+unicode(dato[2]))
	def salidaPDF(self,name):
		self.pdf.output('C:/Registro/Documentos/%s.pdf'%(name),'F')
