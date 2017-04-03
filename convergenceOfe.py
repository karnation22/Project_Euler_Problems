import sys
from fractions import Fraction 
# 1) build a continued fraction list [2, 1,2,1,1,4,1,1,6,1...] up to length 100

def buildContE(limit):
	count = 1
	baseList = [2]
	while(len(baseList) < limit):
		count += 1
		if(count%3==0): baseList.append(2*count/3)
		else: baseList.append(1)
	return baseList



def findNum(numList):
	if(len(numList)==1): return numList[0]
	else: return numList[0] + float(1) / (findNum(numList[1:]))

sys.setrecursionlimit(150)


def findNumSum(limit):
	return Fraction(findNum(buildContE(limit))).limit_denominator().numerator


def findSumofNum(limit):
	strListNum = [i for i in str(findNumSum(limit))]
	return sum(int(i) for i in strListNum)

#remember, use the pattern, don't trust build-in functions...


