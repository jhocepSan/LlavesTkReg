#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sqlite3

class Conector(object):
	"""Clase que ara la coneccion de la base de datos"""
	def __init__(self, dire):
		super(Conector, self).__init__()
		self.dir = dire
		self.db=sqlite3.connect('%s/baseData/Club/infoClub.db'%self.dir)
		self.createTable()
	def createTable(self):
		cur=self.db.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS Varon(ID TEXT,Nombre TEXT,Apellido TEXT,CI NUMERIC,Fecha TEXT,Edad INT,Colegio TEXT)")
		cur.execute('CREATE TABLE IF NOT EXISTS Mujer(ID TEXT,Nombre TEXT,Apellido TEXT,CI NUMERIC,Fecha TEXT,Edad INT,Colegio TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Foto(ID TEXT,Foto TEXT,Qr TEXT,Br TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Tecn(ID TEXT,Club TEXT,Grado TEXT,Altura REAL,Peso REAL,Phone NUMERIC,Tutor TEXT,PhoneT NUMERIC,Casa TEXT,Sangre TEXT,Alergia TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS MesIni(ID TEXT,FechaIni TEXT,GradoIni TEXT,Cluba TEXT,Modalidad TEXT,Horario TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Club(Nombre TEXT,Sigla TEXT,Foto TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Horario(Grupo TEXT,Instructor TEXT,HoraIni TEXT,HoraFin Text,Dias TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Grados(Cinturon Text,Sigla TEXT,Denominacion TEXT)')
		self.db.commit()
		cur.close()
	def setClub(self,dato):
		if self.getClub()!=0:
			cur=self.db.cursor()
			cur.execute("INSERT INTO Club VALUES(?,?,?)",dato)
		else:
			cur=self.db.cursor()
			cur.execute("DELETE FROM Club")
			cur.execute("INSERT INTO Club VALUES(?,?,?)",dato)
		self.db.commit()
		cur.close()
	def getClub(self):
		try:
			cur=self.db.cursor()
			cur.execute("SELECT * FROM Club")
			datos=cur.fetchall()
			cur.close()
			return datos[0]
		except IndexError:
			return 0
	def delHorarioClub(self):
		cur=self.db.cursor()
		cur.execute("DELETE FROM Horario")
		cur.execute("DELETE FROM Club")
		self.db.commit()
		cur.close()
	def setHorario(self,dato):
		cur=self.db.cursor()
		cur.execute("INSERT INTO Horario VALUES(?,?,?,?,?)",dato)
		self.db.commit()
		cur.close()
	def getHorario(self):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Horario")
		dato=cur.fetchall()
		cur.close()
		self.db.commit()
		return dato
	def setGrado(self,dato):
		cur=self.db.cursor()
		cur.execute("INSERT INTO Grados VALUES(?,?,?)",dato)
		self.db.commit()
		cur.close()
	def delGrado(self):
		cur=self.db.cursor()
		cur.execute("DELETE FROM Grados")
		self.db.commit()
		cur.close()
	def getGrado(self):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Grados")
		dato=cur.fetchall()
		self.db.commit()
		cur.close()
		return dato
	def setEstudiante(self,tabla,dato):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM %s WHERE ID=:n"%str(tabla),{"n":str(dato[0])})
		row=cur.fetchone()
		try:
			if len(row) is not None:
				datos=dato[1:]
				datos.append(dato[0])
				cur.execute("UPDATE %s SET Nombre=?,Apellido=?,CI=?,Fecha=?,Edad=?,Colegio=? WHERE ID=?"%str(tabla),datos)
				self.db.commit()
				cur.close()
		except TypeError:
			cur.execute("INSERT INTO %s VALUES(?,?,?,?,?,?,?)"%tabla,dato)
			self.db.commit()
			cur.close()
	def getEstudiante(self,tabla,ide):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM %s WHERE ID=:n"%str(tabla),{"n":str(ide)})
		row=cur.fetchall()
		cur.close()
		self.db.commit()
		return row[0]
	def setDatoTec(self,dato):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Tecn WHERE ID=:n",{"n":str(dato[0])})
		row=cur.fetchone()
		try:
			if len(row) is not None:
				datos=dato[1:]
				datos.append(dato[0])
				cur.execute("UPDATE Tecn SET Club=?,Grado=?,Altura=?,Peso=?,Phone=?,Tutor=?,PhoneT=?,Casa=?,Sangre=?,Alergia=? WHERE ID=?",datos)
				self.db.commit()
				cur.close()
		except TypeError:
			cur.execute("INSERT INTO Tecn VALUES(?,?,?,?,?,?,?,?,?,?,?)",dato)
			self.db.commit()
			cur.close()
	def getDatosTec(self,ide):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Tecn WHERE ID=:n",{"n":str(ide)})
		row=cur.fetchall()
		self.db.commit()
		cur.close()
		return row[0]
	def setDatoMes(self,dato):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM MesIni WHERE ID=:n",{"n":str(dato[0])})
		row=cur.fetchone()
		try:
			if len(row) is not None:
				datos=dato[1:]
				datos.append(dato[0])
				cur.execute("UPDATE MesIni SET FechaIni=?,GradoIni=?,Cluba=?,Modalidad=?,Horario=? WHERE ID=?",datos)
				self.db.commit()
				cur.close()
		except TypeError:
			cur.execute("INSERT INTO MesIni VALUES(?,?,?,?,?,?)",dato)				
			self.db.commit()
			cur.close()
	def getDatoMes(self,ide):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM MesIni WHERE ID=:n",{"n":str(ide)})
		row=cur.fetchall()
		self.db.commit()
		cur.close()
		return row[0]