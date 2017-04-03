from fractions import Fraction 


def createDecVal(order):
	OrdDict = dict()
	OrdDict[0] = 0
	for num in range(1, order+1):
		OrdDict[num] = float(1) / (2 + OrdDict[num-1])
		print(OrdDict[num])
	return OrdDict[order]


def createVal(order):
	return 1 + createDecVal(order)

print(Fraction(createVal(777)).limit_denominator())

def findCount(upper):
	total = 0
	for count in range(1, upper+1):
		if(len(str(Fraction(createVal(count)).limit_denominator().numerator)) > 
		   len(str(Fraction(createVal(count)).limit_denominator().denominator))):
		   print(count)
		   total +=1
	return total

