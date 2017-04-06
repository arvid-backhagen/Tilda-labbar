import timeit
import random
from binTreeFile import *

class Lat:
	""" Kallas av readfile; skapar objekt per varje låt.
		IN: 4 låt-data strängar, OUT: None """
	def __init__(self, trackid, lattid, artist, lattitel):
		self.trackid = trackid
		self.lattid = lattid
		self.artist = artist
		self.lattitel = lattitel

	def __lt__(self, other):
		return self.artist < other.artist

	def __str__(self):
		return "TrackID: " + self.trackid + " Låttid: " + self.lattid + " Artist: " + self.artist + " Låttitel: " + self.lattitel

def readfile(filename):
	"""Här ska vi läsa filen med låtar"""
	latList = []
	latDict = {}
	latTree = Bintree()
	artistTree = Bintree()

	with open(filename, "r", encoding = "ISO-8859-1") as fil:
		for rad in fil:
			attr = rad.split('<SEP>')
			lat = Lat(attr[0], attr[1], attr[2] , attr[3])
			
			latList.append(lat)

			latDict[lat.artist] = lat

			artistTree.put(lat.artist)


	return latList, latDict, artistTree

def linsok(listan, nyckel):
	"""Hämtad från föreläsning 3"""
	for x in listan:
		if x == nyckel:
			return True
	return False

def binsok(listan, nyckel):
	"""Hämtad från föreläsning 3
	Söker i "listan" efter "nyckel". Returnerar True om den hittas, False annars"""
	vanster = 0
	hoger = len(listan)-1
	found = False

	while vanster <= hoger and not found:
		mitten = (vanster + hoger)//2
		if listan[mitten].artist == nyckel:
			found = True
		else:
			if nyckel < listan[mitten].artist:
				hoger = mitten-1
			else:
				vanster = mitten+1
	return found

def main():

	filename = "unique_tracks.txt"

	lista, dictionary, artistTree = readfile(filename)
	n = len(lista)
	print("Antal element =", n)

	sista = lista[n-1]
	testartist = sista.artist

	sorteradLista = sorted(lista, key=lambda x: x.artist)

	linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10)
	print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")
	
	bintid = timeit.timeit(stmt = lambda: binsok(sorteradLista, testartist), number = 10)
	print("Binärsökningen i sorterad lista tog", round(bintid, 4) , "sekunder")
	
	dicttid = timeit.timeit(stmt = lambda: dictionary[testartist], number = 10)
	print("Dictionarysökningen tog", round(dicttid, 4) , "sekunder")
	
	bintreetid = timeit.timeit(stmt = lambda: testartist in artistTree, number = 10)
	print("Bintreesökningen tog", round(bintreetid, 4) , "sekunder")
	

if __name__ == '__main__':
	main()