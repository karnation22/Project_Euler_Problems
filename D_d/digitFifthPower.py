def isLegal(candidate, power):
	if(candidate == 0 or candidate == 1): return False
	total = 0
	oldCandidate = candidate #must keep original copy (good think we don't worry about aliasing)
	while(candidate > 0):
		total += (candidate%10)**power
		candidate //=10
	return(oldCandidate==total)
def digitCount(number):
	count = 0
	while(number>0):
		count += 1
		number //=10
	return count
def getPower(number, power):
	return digitCount(number)*(9**power)
def findLimit(power):
	number = 9
	newpower = 9**power
	while(number < newpower):
		number = 10*number + 9
		newpower = getPower(number, power)
	return newpower
def bruteForcePower(power):
	total = 0
	limit = findLimit(power)
	for candidate in range(int(10**6 * 0.4)):
		if(isLegal(candidate, power)): 
			print(candidate)
			total += candidate
	return ("total is " + str(total))

print(bruteForcePower(5))