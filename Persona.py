#!/usr/bin/env python
#-*- coding: utf-8 -*-
class Persona(object):
	"""docstring for Persona"""
	def __init__(self):
		super(Persona, self).__init__()
		self.id=""
	def setId(self,iden):
		self.id=iden
	def getId(self):
		return self.id
		