def hashKey(key):
		result = 0
		for i in range(len(key)):
			result = (result + ord(key[i])*(i+1))
		print(result)
		return result%2000003

print(hashKey("abba"))