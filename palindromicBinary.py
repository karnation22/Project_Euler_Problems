def convertBinary(number):
	number = number+1
	index = 0
	strNum = ""
	while(number >= 2**index):
		index += 1
	for power in range(index, 0, -1):
		if(number > 2**(power-1)): 
			strNum += "1"
			number -= 2**(power-1)
		else: strNum += "0"
	return int(strNum)

def isPalindrome(strNum):
	return (strNum == strNum[::-1])

def palindromicSum(limit):
	sum = 0
	for number in range(1, limit):
		binNum = convertBinary(number) #returns int type
		if(number==729): print(binNum)
		strNum = str(number)
		if(isPalindrome(str(binNum)) and isPalindrome(strNum)): #inputs string type
			sum += number
	return sum

print(palindromicSum(10**6))