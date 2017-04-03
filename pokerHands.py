#first split list to tuple to list
#[ (LHS1, RHS1), (LHS2, RHS2), (LHS3, RHS3)...] LSHx, RHSx are strings w/ spaces
def createTupleList(): #returns tuple list as described above
	tupleList = [ ]
	file = open('poker.txt', 'r')
	for line in file:
		(leftHand, rightHand) = (line[0:14], line[15:len(line)-1])
		tupleList.append((leftHand, rightHand))
	return tupleList



def getPRank(element): #takes in string input (determines rank of five card combination)
	pass
	

def determineScore(): #skeleton function that returns score
	tupleList = createTupleList()
	print(tupleList)
	p1Win = 0
	for element in tupleList: #iterate through all of the tuple
		P1Rank = getPRank(element[0])
		P2Rank = getPRank(element[1])
		if(P1Rank > P2Rank): p1Win += 1
	return p1Win

