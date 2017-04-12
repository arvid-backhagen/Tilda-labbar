from linkedQFile import *
import sys

q = LinkedQ()

ATOMER = ["H", "He", "Li", "Be", "B", "C2", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd","In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Hf",
"Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Fl", "Lv"]

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
	if not q.peek() == ")":
		try:
			readMolekyl()
		except Syntaxfel:
			pass

def readGrupp():
	"""<group> ::= <atom> |<atom><num> | (<mol>) <num>"""
	
	if q.peek() == "(":
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

	readAtom()
	if not q.isEmpty():
		readNum()
	

def readAtom():
	"""<atom>  ::= <LETTER> | <LETTER><letter>"""
	readVersal()
	if q.peek() is None or q.peek().isdigit():
		return 
	else:
		readGemen() 

def readVersal():
	"""<LETTER>::= A | B | C | ... | Z"""
	versal = q.dequeue()
	print(versal, "dequeueas i versal")
	if versal.isupper():
		return
	raise Syntaxfel("Följer inte syntaxen, versal!")

def readGemen():
	"""<letter>::= a | b | c | ... | z"""
	gemen = q.dequeue()
	print(gemen, "dequeueas i gemen")
	if gemen.islower():
		return
	raise Syntaxfel("Följer inte syntaxen, gemen!")

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
