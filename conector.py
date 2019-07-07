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
		cur.execute("CREATE TABLE IF NOT EXISTS Varon(ID TEXT,Nombre TEXT,Apellido TEXT,CI NUMERIC,Fecha DATE,Edad INT,Colegio TEXT)")
		cur.execute('CREATE TABLE IF NOT EXISTS Mujer(ID TEXT,Nombre TEXT,Apellido TEXT,CI NUMERIC,Fecha DATE,Edad INT,Colegio TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Foto(ID TEXT,Foto TEXT,Qr TEXT,Br TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Tecn(ID TEXT,Club TEXT,Grado TEXT,Altura REAL,Peso REAL,Phone NUMERIC,Tutor TEXT,PhoneT NUMERIC,Casa TEXT,Sangre TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Club(Nombre TEXT,Sigla TEXT,Foto TEXT)')
		cur.execute('CREATE TABLE IF NOT EXISTS Horario(Grupo TEXT,Instructor TEXT,HoraIni TEXT,HoraFin Text)')
		cur.execute('CREATE TABLE IF NOT EXISTS Grados(Cinturon Text,Sigla TEXT,Denominacion TEXT)')
		self.db.commit()
		cur.close()
	def setClub(self,dato):
		if(len(self.getClub())==0):
			cur=self.db.cursor()
			cur.execute("INSERT INTO Club VALUES(?,?,?)",dato)
		else:
			cur=self.db.cursor()
			cur.execute("DELETE FROM Club")
			cur.execute("INSERT INTO Club VALUES(?,?,?)",dato)
		self.db.commit()
		cur.close()
	def getClub(self):
		cur=self.db.cursor()
		cur.execute("SELECT * FROM Club")
		datos=cur.fetchall()
		cur.close()
		return datos
	def delHorarioClub(self):
		cur=self.db.cursor()
		cur.execute("DELETE FROM Horario")
		cur.execute("DELETE FROM Club")
		self.db.commit()
		cur.close()
	def setHorario(self,dato):
		cur=self.db.cursor()
		cur.execute("INSERT INTO Horario VALUES(?,?,?,?)",dato)
		self.db.commit()
		cur.close()