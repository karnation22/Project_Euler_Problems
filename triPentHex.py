def isPentagonal(number): #takes in hexIndex
	#inverse function - determine if int
	# number*2 = 3*n^2 - n - (number*2 C)
	# n = (1/6) (1 + sqrt(1 + 24*number) )
	test = float((1 + (1 + 24*number)**0.5))
	test /= 6 #turn test into int
	return test == int(test) #

def isTriangle(number):# hexindex input
	# n^2 + n = number*2
	# n^2 + n - number*2 = 0
	test = float(-1 + (1 + 8*number)**0.5)
	test /= 2
	return test == int(test)

def createHexagonal(n): #takes in integer input
	return int(n*(2*n -1))

def findTriPentHex(): #no inputs
	found = 2 #first one is 40755
	index = 1
	answer = None
	while(found > 0):
		index += 1 #first number to check is 2
		hexIndex = createHexagonal(index) #grow by hexagonal
		if(isTriangle(hexIndex) and isPentagonal(hexIndex)):
			print("hexindex is " + str(hexIndex))
			answer = hexIndex
			found -= 1
	return answer

print(findTriPentHex())

#1533776805