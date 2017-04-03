def quickStringDigitSum(num): #inputs integer value
	strNum = str(num)
	listNum = [int(letter) for letter in strNum]
	return sum(listNum)

def findMaximumDigitSum():
	maxSum = None
	for a in range(1, 100): #exclusive 100
		for b in range(1, 100): #exclusive 100
			curSum = quickStringDigitSum(a**b)
			if(maxSum == None or curSum > maxSum): maxSum = curSum
	return maxSum

print(findMaximumDigitSum())