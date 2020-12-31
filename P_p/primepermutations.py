import itertools
def isPrime(number):
	for factor in range(2, int(number**0.5)+1):
		if(number%factor == 0): return False
	return True

def threePermutations(number): #returns set of all prime number permutations, inputs number
	setComb = set()
	listnum = [i for i in str(number)]
	combos = list(itertools.permutations(listnum))
	for tup in combos: #combs through all of the tuples of permutations
		strTup = ""
		for letter in tup: 
			strTup += letter
		intTupe = int(strTup)
		if(len(str(intTupe)) == 4 and isPrime(intTupe)): setComb.add(intTupe)
	
	return setComb if len(setComb) >=3 else None

def findArithmetic(setCombo): #inputs a set, returns None/arithmetic list
	listCombo = list(setCombo)
	listCombo = sorted(listCombo) #numberically sorted list
	arithmeticList = [ ] #assume only one arithmetic sequence in list
	for index in range(0, len(listCombo)-1): #up until the end
		arithmeticList.append(listCombo[index])
		for newIndex in range(index + 1, len(listCombo)):
			difference = listCombo[newIndex] - listCombo[index]
			arithmeticList.append(listCombo[newIndex])
			if( (listCombo[newIndex] + difference) in listCombo): 
				arithmeticList.append(listCombo[newIndex] + difference)
				return arithmeticList
			else: arithmeticList = [listCombo[index]]
		arithmeticList = [ ]
	return None


def primePermutations(lower, upper): #go from 10**3 --> 10**4
	listCombo = list()
	for number in range(lower, upper): 
		if(threePermutations(number) != None and findArithmetic(threePermutations(number)) != None): #property 1&2, arithmetic
			if(findArithmetic(threePermutations(number)) not in listCombo):
			    listCombo.append(findArithmetic(threePermutations(number))) #pop in a list

	return listCombo


print(primePermutations(10**3, 10**4))