from linkedQFile import *
import sys
import string
from molgrafik import *

q = LinkedQ()

par=[]

ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']


class Syntaxfel(Exception):
	pass


def storeMolekyl(molekyl):
	for symbol in molekyl:
		q.enqueue(symbol)
	return q

def readMolekyl():

	if q.isEmpty():
		if len(par) > 0:
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
		return
		
	mol = readGrupp()
	if not q.isEmpty() and q.peek() != ")":
		mol.next = readMolekyl()
		
	readMolekyl()

def readGrupp():

	if q.peek().isdigit() or q.peek() == None:
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")


	if q.peek().isalpha():
		atomruta = Ruta(atom = readAtom())
		if q.peek() is None:
			return
		if q.peek().isdigit():
			atomruta.num = readNum()
		readMolekyl()
	

	if q.peek() == "(":
		paratesruta = Ruta()
		par.append(q.dequeue())
		parantesruta.down = readMolekyl()


	if q.isEmpty():
		return

	if q.peek() == ")":

		if len(par) >= 1:
			par.pop()
			q.dequeue()
		else:
			raise Syntaxfel("Felaktig gruppstart vid radslutet ")

		if q.peek() is None:
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			parantesruta.num = readNum()	

	else: 
		raise Syntaxfel("Saknad högerparentes vid radslutet ")


def readAtom():
	"""<atom>  ::= <LETTER> | <LETTER><letter>"""

	if q.peek().isupper():
		x = q.dequeue()
	else:
		raise Syntaxfel("Saknad stor bokstav vid radslutet ")

	if q.peek() != None:
		if q.peek().islower():
			x = x + q.dequeue()
	
	if x in ATOMER:
		return x
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
			return int(num)
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
		
		return readMolekyl()
	except Syntaxfel as error:
		return str(error) + printQ()

def main():
	#kodupprepning på alla raise Syntaxfel

	mg = Molgrafik() # Skapar objekt för att rita upp molekyl

	molekyl = input("Molekyl: ")
	if molekyl != "#":
		resultat = readFormel(molekyl)
		del par[:]
		q.clear()
		print(resultat)
		mg.show(resultat)
		main()


if __name__ == '__main__':
	main()


