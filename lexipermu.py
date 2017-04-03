import math
def fact(n):
	index = 1
	while (n > 0):
		index *=n
		n -=1
	return index

def determineLexiIndex(L, index): #takes in list and index
	index = index-1
	if(fact(len(L)) <= index): return None
	strNum = ""
	for round in range(len(L)):
		if(round > 0): print(L, index)
		LIndex = math.floor(index/fact(len(L) - 1))
		LIndex = int(LIndex)
		strNum += str(L[LIndex])
		index -= LIndex*(fact(len(L) - 1))
		L.pop(LIndex)
	return strNum

print(determineLexiIndex([0,1,2,3,4,5,6,7,8,9], 10**6))
#2783915460