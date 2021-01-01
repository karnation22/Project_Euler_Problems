from itertools import permutations

def valFound(num, numDict):
	for elem in numDict:
		if num in numDict[elem]: return True
	return False

def isFour(num):
	return len(str(num)) == 4

def sixclyic(lower, upper): #10**3 inclusive, 10**4 exclusive
	numDict = dict()
	for num in range(lower, upper):
		if(valFound(num, numDict)): continue
		else:
			SixLicList = set(int(''.join(p)) for p in permutations(str(num)))
			numDict[num] = filter(isFour, SixLicList)
	return numDict

def is_tri(n):
    ans = any((x*((x+1))/2 == n for x in range(n+1)))
    return ans
def is_square(n):
    ans = any((x**2 == n for x in range(n+1)))
    return ans
def is_pent(n):
    ans = any((x*((3*x)-1))/2 == n for x in range(n+1))
    return ans
def is_hex(n):
	ans = any((x*((2*x)-1)) == n for x in range(n+1))
	return ans
def is_hept(n):
	ans = any((x*((5*x)-3))/2 == n for x in range(n+1))
	return ans
def is_oct(n):
	ans = any((x*((3*x)-2)) == n for x in range(n+1))
	return ans

def findValid(numDictElem): 
#takes in a list of 4 digit integers -> returns either a sum or a bool!
	#polySet = {"tri", "square", "pent", "hex", "hept", "oct"}
	triSet = set(filter(is_tri, numDictElem))
	squareSet = set(filter(is_square, numDictElem))
	pentSet = set(filter(is_pent, numDictElem))
	hexSet = set(filter(is_hex, numDictElem))
	heptSet = set(filter(is_hept, numDictElem))
	octSet = set(filter(is_oct, numDictElem))

	polySet = [triSet, squareSet, pentSet, hexSet, octSet]
	if(any(map((lambda x : len(x) == 0), polySet))): return None
	else: 

def findOrdered(numDict):
	for elem in numDict:
		if len(numDict[elem]) < 6: continue
		else: 
			print(findValid(numDict[elem]), numDict[elem])
			if(findValid(numDict[elem]) != None): 
				return findValid(numDict[elem])
	return ("YOU DUN GOOFED")

###INCREDIBLY WEAK AND INEFFICIENT ALGORITHM!!!




	
