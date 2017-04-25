from linkedQFile import *
import sys
import string

q = LinkedQ()

ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
	pass

def storeMolekyl(molekyl):
	"""Lägger in strängen i kön"""
	for symbol in molekyl:
		q.enqueue(symbol)
	#q.enqueue('\n')
	return q

def readMolekyl():
	"""<mol>   ::= <group> | <group><mol>"""
	readGrupp()
	if q.peek() == None:
		return
	if q.peek() != ")":
		try:
			readMolekyl()
		except Syntaxfel:
			pass

def readGrupp():
	"""<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
	
	if q.peek().isupper():
		readAtom()
		try:
			if q.peek().isalpha():
				readMolekyl()
		except:
			pass

	if q.peek() == "(":
		q.dequeue()
		readMolekyl()

	if q.peek() == "\n":
		rest = ""
		while not q.isEmpty():
			rest = rest + q.dequeue()
		raise Syntaxfel("Saknad högerparantes vid radslutet " + rest)

	if q.peek() == ")":
		q.dequeue()
		if q.peek().isdigit():
			readNum()
			return
		rest = ""
		while not q.isEmpty():
			rest = rest + q.dequeue()
		raise Syntaxfel("Saknar siffra vid radslut " + rest)

	if not q.isEmpty():
		if q.peek().isdigit():
			readNum()
		else:
			rest = ""
			while not q.isEmpty():
				rest = rest + q.dequeue()
			raise Syntaxfel("Saknad stor bokstav vid radslutet " + rest)
		readMolekyl()
	

def readAtom():
	"""<atom>  ::= <LETTER> | <LETTER><letter>"""
	if q.peek().isalpha():
	
		if q.peek().isupper():
			x = q.dequeue()
			print(x, "readAtom stor bokstav")
		else:
			rest = ""
			while not q.isEmpty():
				rest = rest + q.dequeue()
			raise Syntaxfel("Saknad stor bokstav vid radslutet " + rest)

		if q.peek() is None:
			return

		if q.peek().islower():
			x = x + q.dequeue()
		
		if x in ATOMER:
			return
		else:
			rest = ""
			while not q.isEmpty():
				rest = rest + q.dequeue()
			raise Syntaxfel("Okänd atom vid radslutet " + rest)

def readNum():
	"""<num>   ::= 2 | 3 | 4 | ..."""

	# HUR HANTERAR VI OM DET STÅR Na12 ???
	try:
		if int(q.peek()) >= 2:
			print(q.peek(), "dequeuas i readNum")
			q.dequeue()
		else:
			q.dequeue()
			rest = ""
			while not q.isEmpty():
				rest = rest + q.dequeue()
			raise Syntaxfel("För litet tal vid radslutet " + rest)
			sys.exit()
	except (ValueError,TypeError):
		print("fastna i readNum Value eller TypeError")
		sys.exit()

def readFormel(molekyl):
	"""<formel>::= <mol> \n"""
	q = storeMolekyl(molekyl)
	try:
		readMolekyl()
		return 'Formeln är syntaktiskt korrekt'
	except Syntaxfel as error:
		return error


def main():
	
	molekyl = input("skriv en molekyl: ")
	if molekyl != "#":
		resultat = readFormel(molekyl)
		print(resultat)
		main()


if __name__ == '__main__':
	main()

#Si(C3(COOH)2)4(H2O)7