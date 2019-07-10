import sys
class allegedRC4(object):
	"""docstring for allegedRC4"""
	def __init__(self):
		super(allegedRC4, self).__init__()
	def KSA(self,key):
		keylength = len(key)
		S = range(256)
		j = 0
		for i in range(256):
			j = (j + S[i] + key[i % keylength]) % 256
			S[i], S[j] = S[j], S[i]  # swap
		return S
	def PRGA(self,S):
		i = 0
		j = 0
		while True:
			i = (i + 1) % 256
			j = (j + S[i]) % 256
			S[i], S[j] = S[j], S[i]  # swap
			K = S[(S[i] + S[j]) % 256]
		yield K
	def RC4(self,key):
		S = self.KSA(key)
		return self.PRGA(S)
	def convert_key(self,s):
		return [ord(c) for c in s]
	def codigoRC4(self,message="",key=""):
		codigo=""
		key = self.convert_key(key)
		keystream = self.RC4(key)
		for c in message:
			codigo=codigo+("%02X-" % (ord(c) ^ keystream.next()))
		return codigo[:len(codigo)-1]