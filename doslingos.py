import string
def all_distinct(stringA): 
	#inputs list of strings, and length of string
	#returns boolean value
	n = len(stringA)
	stringA = sorted(stringA) #sort list of strings
	for i in range(0, n-1): #goes through all of the strings
		if(stringA[i] == stringA[i+1]): return False
	return True

def count_distinct(stringA):
	n = len(stringA)
	if(n==0): return 0
	stringA = sorted(stringA)
	count = 1
	for i in range(0, n-1):
		if(stringA[i] != stringA[i+1]): count += 1
	return count

def remove_duplicates(stringA):
	n = len(stringA)
	if(n ==0): return [ ]
	stringA = sorted(stringA)
	distinct = count_distinct(stringA)
	ans = [0] * distinct
	index = 0
	for i in range(0, n): #iterate through all of the stringA
		if(i==0): 
			ans[index] = stringA[i] #ok, we took care of the zeroth element
			index += 1
		elif(stringA[i-1] != stringA[i]):
			ans[index] = stringA[i]
			index += 1
	return ans
	
print(remove_duplicates(["AAAA", "AAAA", "ABCD", "BCDF", "BCDF"])) #3
print(remove_duplicates(["AAAA", "AAAA", "AACC"]))
print(remove_duplicates(["BBDD", "BBDD", "ADCF", "SDSD", "SDFWEF", "SDFWEF"]))
print(remove_duplicates(["AAAA"])) # 1 
print(count_distinct([])) 

"""def linSearch(word, Alist):
	length = len(Alist)
	for index in range(0, length):
		if(Alist[index] == word): return index
	return -1
def count_vocab(vocabList, freqList, tweetfile, fast):
	v = len(vocabList)
	noShow = 0
	for word in tweetfile:
		index = linSearch(word, vocabList)
		if(index == -1): noShow += 1
		else: freqList[index] += 1
	return (noShow, freqList)

ListAlphabet = [i for i in string.ascii_lowercase]
freqList = [i for i in range(26)]
tweetfile = ["a", "aa", "b", "c", "d", "dd", "e", "ee"] #

print(count_vocab(ListAlphabet, freqList, tweetfile, True)) #return (4, [1,2,3,4,4...])




List = ["WSDSD", "SDSD", "ADSF", "SDfsdfdsfsdf", "Tyhytgf"]

List = sorted(List)
print(List)"""