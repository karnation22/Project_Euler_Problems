##Build cubes from ground up; dictionary stores first permu and num, and all other permus (tuple data types)
import itertools

def isPermu(strNum1, strNum2):
	return (sorted(list(strNum1)) == sorted(list(strNum2)))

def powerOfTen(index): #no mapreduce... 
	if(index < 20): return index == 10
	indList = list(str(index))
	(head, maptail) = (indList[0], map((lambda x: x == "0"),(indList[1:])))
	return (head == "1" and reduce((lambda x, y: x and y), maptail))

def buildUp(permu): #starts @ one, builds double list
	permDict = dict()
	permDict[1] = [1] #values contain numbers, but key also contains number
	index = 2
	while(True):
		for perm in permDict: 
			foundOne = False
			if( len(str(perm**3)) == len(str(index**3)) 
			   and isPermu(str(perm**3), str(index**3))):
					permDict[perm].append(index)
					foundOne = True
					break
		if(not foundOne): permDict[index] = [index]
		else: foundOne = False
		for perm in permDict:
			if len(permDict[perm]) == permu: return permDict[perm]
		index += 1
		if(index % 500 == 0): print(index)

#FIND A FASTER ALGORITHM THAN JUST APPENDING A DICTIONARY (592.2 seconds too slow...)


print(buildUp(5))






