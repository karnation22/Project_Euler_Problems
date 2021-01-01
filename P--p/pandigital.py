import copy
def findTuplePairs(number):
	listFactor = list()
	for factor in range(1, int(number**0.5)+1):
		if(number%factor==0):
			listFactor.append((factor, number/factor)) #tuple contains pairs
	return listFactor

def isPanDigital(fac1, fac2, number, pandigitalList):
	copyPan = copy.copy(pandigitalList) #stupid aliasing bullshit 
	strNum = str(fac1) + str(fac2) + str(number)
	if(len(strNum) != 9): return False #it has to be a nine digit number 
	for letnum in strNum:
		if(int(letnum) not in copyPan): return False #if a number isn't in the list, it is false
		else: copyPan.remove(int(letnum)) #remove a number after we are done with it
	return True

def findPanDigital(lower, upper): #the limit will really be like 10**4
	sumset = set()
	pandigitalList = [i for i in range(1,10)]
	for number in range(lower, upper):
		listFactors = findTuplePairs(number) #return list of tuples of pairs that multiply up
		for (fac1, fac2) in listFactors:
			if(isPanDigital(fac1, fac2, number, pandigitalList)): 
				print(number, fac1, fac2)
				sumset.add(number)
	return sum(sumset)

print(findPanDigital(10**3, 10**4))


