import string
from nltk.tokenize import word_tokenize
from nltk.corpus import words
def listifyCipher():
	file = open('cipher.txt', 'r')
	cipherList = list()
	for line in file:
		listLine = line.split(',')
		cipherList += listLine
	return cipherList

def isEnglish(plaintext): #takes plaintext string, outputs bool
	listWords = word_tokenize(plaintext) #now we have a list (includes)
	(count, total) = (0,0) 
	for word in listWords:
		try: #this is for the integers
			if(type(int(word)) == int):
				count += 1
				total += 1 
		except: #this is for the normal words
			if(word in words.words()):
				count += 1
				total += 1
	return (float(count) / total) > 0.95 #lets assume

def createPlainText():
	xorList = listifyCipher()
	plaintext = "" #remember, this is the actual string
	for let1 in range(ord('a'), ord('z') + 1):
		for let2 in range(ord('a'), ord('z') + 1):
			for let3 in range(ord('a'), ord('z') + 1):
				letList = [let1, let2, let3] #remember, these are ASCII ints, NOT actual chars
				for num in range(len(xorList)): #use indices of xorlist
					plaintext += chr(int(xorList[num]) ^ letList[num%3]) #magic number 3 len of lenlist
				if(isEnglish(plaintext)): return plaintext
	return None

		
def getTotalAscii():
	text = createPlainText() #asssume text NOT none type AND is correct
	total = 0
	for let in text:
		total += ord(let)
	return total

print(getTotalAscii())

