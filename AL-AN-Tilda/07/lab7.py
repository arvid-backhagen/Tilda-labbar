import timeit

class DictHash:
	def __init__(self):
		self.dict = {}
		
	def store(self, key, data):
		self.dict[key] = data

	def search(self, key):
		return self.dict[key]


def storeArtist():
	with open("unique_tracks.txt", "r", encoding = "ISO-8859-1") as fil:
		for rad in fil:
			attr = rad.split('<SEP>')
			hasha.store(attr[0], attr[2])

def searchArtist(key):
	return hasha.search(key)

def main():
	storeArtist()
	key = input("Välj key: ")
	dicttid = timeit.timeit(stmt = lambda: searchArtist(key), number = 1000000)
	print("Dictionarysökningen tog", round(dicttid, 4) , "sekunder")
	print(searchArtist(key))

if __name__ == '__main__':
	hasha = DictHash()
	main()