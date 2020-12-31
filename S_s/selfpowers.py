#keep a sum, and keep on modding it
def selfPower(lower, upper): #brute force it at first (upper is 1001)
	last = 0
	for number in range(lower, upper): #no exponents, just rules of math
		last += (number**number)
	return last
print(selfPower(1, 1001))

