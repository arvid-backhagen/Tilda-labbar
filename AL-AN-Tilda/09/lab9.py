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
	print("inne i readGrupp")
	if q.peek().isupper():
		print("Storbokstav uppfylld skickar till readAtom")
		readAtom()
		if q.peek().isalpha():
			readMolekyl()

	if q.peek() == "(":
		print(q.peek(), "hittad")
		q.dequeue()
		readMolekyl()

		if q.peek() == "\n":
			raise Syntaxfel("Saknar högerparantes")

		if q.peek() == ")":
			q.dequeue()
		
			if q.peek().isdigit():
				readNum()
				return
			raise Syntaxfel("Saknar siffra vid radslut")

	# HÄR MÅSTE VI KOLLA OM DET FINNS FLER ATOMER I GRUPPEN	


	#readAtom()
	if not q.isEmpty():
		readNum()
	

def readAtom():
	"""<atom>  ::= <LETTER> | <LETTER><letter>"""
	if q.peek().isalpha():
	
		if q.peek().isupper():
			x = q.dequeue()
			print(x, "I atom 1")
		else:
			raise Syntaxfel("Saknar stor bokstav i början")

		if q.peek() is None:
			return

		if q.peek().islower():
			x = x + q.dequeue()
			print(x, "I atom 2")
		
		if x in ATOMER:
			print(x, "finns i ATOMER")
			return
		else:
			raise Syntaxfel("Okänd atom")

def readNum():
	"""<num>   ::= 2 | 3 | 4 | ..."""
	try:
		if int(q.peek()) >= 2:
			print(q.peek(), "dequeueas i num")
			q.dequeue()
			
		else:
			q.dequeue()
			print("För litet tal vid radslut ")
			sys.exit()
	except (ValueError,TypeError):
		raise Syntaxfel("Inte en siffra")

def readFormel(molekyl):
	"""<formel>::= <mol> \n"""
	q = storeMolekyl(molekyl)
	try:
		readMolekyl()
		return 'Följer syntaxen!'
	except Syntaxfel as error:
		return str(error)


def main():
	
	molekyl = input("skriv en molekyl: ")
	resultat = readFormel(molekyl)
	print(resultat)
	main()


if __name__ == '__main__':
	main()

#Si(C3(COOH)2)4(H2O)7