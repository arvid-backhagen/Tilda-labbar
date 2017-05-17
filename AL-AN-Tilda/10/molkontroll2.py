from linkedQFile import *
import sys
import string
from molgrafik import *
from hashtest import *

q = LinkedQ()

par=[]

ATOMER = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Fl', 'Lv']

hashadeAtomer = lagraHashtabell(skapaAtomlista())

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

	mol = readGrupp()
	if q.isEmpty():
		return mol
	elif q.peek() == ")":
		if len(par) < 1:
			raise Syntaxfel("Felaktig gruppstart vid radslutet ") 
		return mol
	else:
		mol.next = readMolekyl()
	return mol

def readGrupp():
	"""<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
	"""readgroup() anropar antingen readatom() eller läser en parentes och anropar readmol()"""

	rutan = Ruta()

	if q.isEmpty():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")
	if q.peek().isdigit():
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

	if q.peek().isalpha():
		rutan.atom = readAtom()
		if q.peek() is None:
			return rutan
		if q.peek().isdigit():
			rutan.num = int(readNum())

	elif q.peek() == "(":
		par.append(q.dequeue())
		rutan.down = readMolekyl()

		if q.peek() != ")":
			raise Syntaxfel("Saknad högerparentes vid radslutet ")
				

		if q.isEmpty():
			raise Syntaxfel("Saknad siffra vid radslutet ")
		else:
			par.pop()
			q.dequeue()
			if q.isEmpty():
				raise Syntaxfel("Saknad siffra vid radslutet ")
			rutan.num = int(readNum())
	else:
		raise Syntaxfel("Felaktig gruppstart vid radslutet ")

	return rutan

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
			return num
		else:
			raise Syntaxfel("För litet tal vid radslutet ")
	else:
		raise Syntaxfel("Saknad siffra vid radslutet ")

def printQ():
	rest = ""
	while not q.isEmpty():
		rest = rest + q.dequeue()
	return rest

def readVikt(ruta):

	if ruta.atom == "()":
		if ruta.down != None:
			x = float(readVikt(ruta.down))*float(ruta.num)

	else:
		x = float(hashadeAtomer.search(ruta.atom).value.vikt)*float(ruta.num)

	if ruta.next != None:
		y = readVikt(ruta.next)
		return x+y
	else:
		return x




def readFormel(molekyl):
	"""<formel>::= <mol> \n"""
	q = storeMolekyl(molekyl)
	try:
		mol = readMolekyl()
		if len(par) > 0:
			raise Syntaxfel('Saknad högerparentes vid radslutet ')
		print('Formeln är syntaktiskt korrekt')
		print("Vikten av din molekyl är: " + str(readVikt(mol)))
		return mol
	except Syntaxfel as error:
		return str(error) + printQ()

def main():
	#kodupprepning på alla raise Syntaxfel
	molekyl = input("Molekyl: ")
	mg = Molgrafik()
	if molekyl == "exit":
		pass
	else:
		mol = readFormel(molekyl)
		mg.show(mol)
		
		del par[:]
		printQ()
		q.clear()
		main()

if __name__ == '__main__':
	main()

