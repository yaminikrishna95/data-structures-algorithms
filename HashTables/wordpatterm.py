def wordPattern(word,pattern):
	pattern=pattern.split(" ")
	if len(word)!=len(pattern):
		return False



if __name__ == "__main__":
	word="abba"
	pattern="geeks for for geeks"
	print(wordPattern(word,pattern))