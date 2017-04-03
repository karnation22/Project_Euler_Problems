def findCount(nDig):
	count = 0
	while(nDig < 100): #arbritrary upper n bound
		for baseNum in range(1, 10):
			print(baseNum, nDig)
			if(len(str(baseNum**nDig)) == nDig): count += 1
		nDig += 1
	return count
#we know the base is between 1 nad 9 inclusive

print(findCount(1))







