
from linkedQFile import *
import sys

q = LinkedQ()

class Syntaxfel(Exception):
	pass

def storeMolekyl(molekyl):
	number = ''
	for symbol in molekyl:
		if symbol.isdigit():
			q.enqueue(str(symbol))
			print(symbol, "enqueueas")
		else:
			q.enqueue(symbol)
			print(symbol, "enqueueas")
	if number:
		q.enqueue(number)
		print(number, "enqueueas")
	return q

def readMolekyl():
	readAtom()
	if q.peek() == '':
		q.dequeue()
	else:
		readNum()

def readAtom():
	readVersal()
	if q.peek() is None or q.peek().isdigit():
		return 
	else:
		readGemen() 

def readVersal():
	versal = q.dequeue()
	#print(versal, "dequeueas i versal")
	if versal.isupper():
		return
	raise Syntaxfel("Den är inte versal: " + versal)

def readGemen():
	gemen = q.dequeue()
	#print(gemen, "dequeueas i gemen")
	if gemen.islower():
		return
	raise Syntaxfel("Det är inte en gemen: " + gemen)

def readNum():
	num = ''
	if q.isEmpty():
		return
	while not q.isEmpty():

		print(q.peek(), "dequeueas som num")
	#print("nu är num: ", num)
		if q.peek() == None:
			pass
		elif q.peek().isdigit():
			num += q.dequeue()
		#print("nu är num: ", num)
		else:
			raise Syntaxfel("För lång atom: " + q.peek())

	if int(num)>=2:
		return
	else:
		raise Syntaxfel("För litet tal: " + num)

def checksyntax(molekyl):
	q = storeMolekyl(molekyl)
	try:
		readMolekyl()
		return 'Följer syntaxen!'
	except Syntaxfel as error:
		return str(error)


def main():
	
	molekyl = input("skriv en molekyl: ")
	resultat = checksyntax(molekyl)
	print(resultat)
	


if __name__ == '__main__':
	main()




