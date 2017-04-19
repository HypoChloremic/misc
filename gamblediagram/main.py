# GambleDiagram med python processing

class constants:
	na = 0
	k  = 0
	mg = 0
	ca = 0

	cl   = 0 
	hco3 = 0
	BB   = 48
	res  = 0

	

def setup():
	size(300,500)

class Gamble:
	def __init__(self, na=140, k=4, mg=2, ca=2, cl=100, hco3=24, BB=48, res=7, ph=7.4, pka=6.1):
		self.na = na
		self.k  = k
		self.mg = mg
		self.ca = ca
		self.cl = cl
		self.hco3 = hco3

	
	def hco3(self, pco2 = 4)
		self.hco3 = 0.23*pco2*10**(ph-pka) 


	def gamble(na=140, k=4, mg=2, ca=2, cl=100, hco3=24, BB=48, res=7):
		cation = na + k + mg + ca
		anion  = cl + BB + hco3 + res