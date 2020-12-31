##the very very inefficient version
def setTerms(aLimit, bLimit):
	numSet = set()
	for aNum in range(2, aLimit+1): 
		for bNum in range(2, aLimit+1): #brute force this shit
			if (aNum**bNum not in numSet):
				numSet.add(aNum**bNum)
			else: continue
	return len(numSet)

print(setTerms(100, 100))



