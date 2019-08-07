#!/usr/bin/env python
#-*- coding: utf-8 -*-
from PySide.QtGui import *
from PySide.QtCore import *
import conector

class buscarEst(QGroupBox):
	"""docstring for buscarEst"""
	def __init__(self, parent,dire):
		super(buscarEst, self).__init__(parent)
		self.dir=dire
		self.setCheckable(True)
		self.setChecked(False)
		self.componentes()
		self.position()
		self.setTitle("Buscar")
		self.estudiante=[]
		self.db=conector.Conector(self.dir)
	def componentes(self):
		self.buscar=QLineEdit(self)
		self.buscar.editingFinished.connect(self.formalizar)
		self.id=QCheckBox("ID",self)
		self.id.stateChanged.connect(self.activado)
		self.ci=QCheckBox("Carnet",self)
		self.ci.stateChanged.connect(self.activado)
		self.name=QCheckBox("Nombre",self)
		self.name.stateChanged.connect(self.activado)
	def position(self):
		self.buscar.setGeometry(10,20,200,40)
		self.id.setGeometry(10,70,40,40)
		self.ci.setGeometry(60,70,70,40)
		self.name.setGeometry(140,70,80,40)
	def formalizar(self):
		pass
	def activado(self):
		if self.id.isChecked() and not self.ci.isChecked() and not self.name.isChecked():
			self.estudiante=self.db.getEstudiante(self.buscar.text().upper())
		elif not self.id.isChecked() and self.ci.isChecked() and not self.name.isChecked():
			self.estudiante=self.db.getEstudianteCi(self.buscar.text())
			print self.estudiante
		elif not self.id.isChecked() and not self.ci.isChecked() and self.name.isChecked():
			self.estudiante=self.db.getEstudianteName(self.buscar.text().title())
	def getPersona(self):
		return self.estudiante
	def cleanPersona(self):
		self.estudiante=[]