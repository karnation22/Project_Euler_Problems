def findMultiple(limit):
	strDec = "."
	sol = 1
	for number in range(1,limit):
		strDec += str(number) #create this super duper long string
	for power in range(7):
		sol *= int(strDec[10**power])
		print(power)
	return sol


print(findMultiple(1000000))
