class base64sin(object):
	"""docstring for base64sin"""
	def __init__(self):
		super(base64sin, self).__init__()
		self.dic=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 
				"A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
				"K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
				"U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d",
				"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", 
				"o", "p", "q", "r", "s", "t", "u", "v", "w", "x", 
				"y", "z", "+", "/"]
	def convertir(self,valor):
		quotiet=1
		remainder=int()
		word=""
		while quotiet>0:
			quotiet=valor/64
			remainder=valor%64
			word=self.dic[remainder]+word
			valor=quotiet
		return word
		
