import copy
def isSmallestPermuted(index):
	digitList = [ ] #list contains digits of all the index
	for numstr in str(index): digitList.append(numstr) #append string number
	listTest = [2*index, 3*index, 4*index, 5*index, 6*index] 
	for test in listTest: #iterate though all of the numbers
		newDigitList = copy.copy(digitList) #create non-carbon copy
		for numstr in str(test): #check w/ string number (no need to convert to int)
			if numstr not in newDigitList: return False #each string number MUST BE IN THE DIGIT LIST
			else: newDigitList.remove(numstr)
		if(newDigitList != [ ]): return False #NEED EMPTY LIST @ THE END !!
	return True

def findSmallestPermuted(): #steps from smallest to largest number
	index = 1
	notFound = True
	while(notFound):
		index += 1
		print(index)
		if(isSmallestPermuted(index)): notFound = False 
	return(index, 2*index, 3*index, 4*index, 5*index, 6*index)

print(findSmallestPermuted())