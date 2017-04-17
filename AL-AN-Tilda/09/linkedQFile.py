import sys

class Node:
	"""Skapar ett simpelt nod-objekt med ett värde och en next-pekare"""
	def __init__(self, value):
		self.value = value
		self.next = None

class LinkedQ:
	def __init__(self):
		"""Initierar en tom länkad kö"""
		self.__first = None
		self.__last = None

	def enqueue(self, x):
		"""Lägger värdet x sist i kön"""

		new = Node(x) 				# Skapar nod-objektet med value=x 

		if self.__first == None: 	# Om kön är tom så sätts 
			self.__first = new 		# den nya noden till både första och sista värdet
			self.__last = new
		else:
			self.__last.next = new	# Annars pekar det förra sista värdet
			self.__last = new		# på det nya och det nya sätts sist
		
	def dequeue(self):
		"""Ta ut värdet längst fram i kön"""
		if self.__first == None:
			return None
		temp = self.__first 				# Sparar första nodens värde i lokal variabel
		self.__first = self.__first.next	# Skriver över den första noden med nästa nod
		return temp.value


	def isEmpty(self):
		"""Om kön inte har ett första värde returneras True annars False"""
		return self.__first == None


	def peek(self):
		"""Returnerar en kopia av nästa item i kön, utan att ta bort den.
		Nästa item är samma värde som skulle ha blivit returnerat av dequeuen operationen. 
		Ett item kan inte bli dequeued från en tom kö."""
		if not self.isEmpty():
			return self.__first.value
		else:
			return None
