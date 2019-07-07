#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *

class ListaEstu(QMdiSubWindow):
	"""Nomina de estudiantes del club"""
	def __init__(self, arg,dire):
		super(ListaEstu, self).__init__(arg)
		self.setGeometry(0,0,885,630)
		self.setWindowTitle("Lista de Estudiantes")
		self.dir=dire
		with open('%s/css/styleMen.css'%self.dir) as f:
			self.setStyleSheet(f.read())