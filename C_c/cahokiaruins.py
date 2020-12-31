import sys

def FindTime(strNum):
	(height, width) = (int(strNum[0]), int(strNum[1]))
	strNum = strNum[2:]
	left = strNum[:int(0.5*len(strNum))]
	right = strNum[int(0.5*len(strNum)):]
	minCount = None
	for i in range(int(0.5*len(strNum))):
		print(left[i], right[i])
		curCount = width - int(left[i]) - int(right[i])

		if(minCount == None or curCount < minCount):
			minCount = curCount
	return float(minCount) / 2


