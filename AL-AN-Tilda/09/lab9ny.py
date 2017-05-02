from linkedQFile import *
import sys
import string

q = LinkedQ()

par=[]

ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
	pass


def storeMolekyl(molekyl):
	"""Lägger in strängen i kön"""
	for symbol in molekyl:
		q.enqueue(symbol)
	return q

def readMolekyl():
	"""<mol>   ::= <group> | <group><mol>"""
	"""readmol() anropar readgroup() och sedan eventuellt sej själv
	(men inte om inmatningen är slut eller om den just kommit tillbaka från ett parentesuttryck)"""

	if q.isEmpty():
			if len(par) > 0:
				raise Syntaxfel("Saknad högerparentes vid radslutet ")
			return

	readGrupp()
	if not q.isEmpty() and q.peek() != ")":
		readMolekyl()
		
	readMolekyl()
	#print("readMolekyl klar")

def readGrupp():
	"""<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
	"""readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol()"""

	if q.peek().isdigit() or q.peek() == None:
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")


	if q.peek().isalpha():
		#print("Kallar på readAtom i readGrupp")
		readAtom()
		if q.peek() is None:
			return
		if q.peek().isdigit():
			readNum()
		readMolekyl()

	

	if q.peek() == "(":
		par.append(q.dequeue())
		#print("Kallar på readMol vid peek = (")
		readMolekyl()

	#print("Kön är: " + str(q))
	#print ("Paranteslistan är: " + str(par))

	if q.isEmpty():
		return

	if q.peek() == ")":
		#print("Hittat ): " + str(par))

		if len(par) >= 1:
			par.pop()
			q.dequeue()
		else:
			raise Syntaxfel("Felaktig gruppstart vid radslutet ")

		if q.peek() is None:
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			#print("Kallar på readNum när peek = None")
			readNum()	

	else: 
		raise Syntaxfel("Saknad högerparentes vid radslutet ")

	

	

	#print("readGrupp klar")

def readAtom():
	"""<atom>  ::= <LETTER> | <LETTER><letter>"""

	# VI SKA ENDAST KOMMA HIT OM .ISALPHA() ÄR UPPFYLLT
	if q.peek().isupper():
		x = q.dequeue()
		#print(x, "readAtom stor bokstav")
	else:
		raise Syntaxfel("Saknad stor bokstav vid radslutet ")

	if q.peek() != None:
		if q.peek().islower():
			x = x + q.dequeue()
			#print("Atomen är", x)
	
	if x in ATOMER:
		return
	else:
		raise Syntaxfel("Okänd atom vid radslutet ")


def readNum():
	"""<num>   ::= 2 | 3 | 4 | ..."""

	if q.peek().isdigit():
		if q.peek() == "0":
			q.dequeue()
			raise Syntaxfel("För litet tal vid radslutet ")

		num = ""
		while q.peek() != None:
			if q.peek().isdigit():
				num = num + q.dequeue()
			else:
				break
		if int(num) >= 2:
			#print(num)
			return
		else:
			raise Syntaxfel("För litet tal vid radslutet ")
	else:
		raise Syntaxfel("Saknad siffra vid radslutet ")

def printQ():
	rest = ""
	while not q.isEmpty():
		rest = rest + q.dequeue()
	return rest

def readFormel(molekyl):
	"""<formel>::= <mol> \n"""
	q = storeMolekyl(molekyl)
	try:
		readMolekyl()
		return 'Formeln är syntaktiskt korrekt'
	except Syntaxfel as error:
		return str(error) + printQ()

def main():
	#kodupprepning på alla raise Syntaxfel
	molekyl = input()
	if molekyl != "#":
		resultat = readFormel(molekyl)
		del par[:]
		q.clear()
		print(resultat)
		main()

if __name__ == '__main__':
	main()

