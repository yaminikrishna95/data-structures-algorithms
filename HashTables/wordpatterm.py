def wordPattern(word,pattern):
	pattern=pattern.split(" ")
	if len(word)!=len(pattern):
		return False
	charToword={}
	wordToChar={}
	for c,w in zip(word,pattern):
		if c  in charToword and charToword[c] != w:
			return False
		if w in wordToChar and wordToChar[w] != c:
			return False
		charToword[c]=w
		wordToChar[w]=c
	return True






if __name__ == "__main__":
	word="abba"
	pattern="geeks for for fish"
	print(wordPattern(word,pattern))
	print(wordPattern2(word, pattern))