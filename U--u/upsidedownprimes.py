
def isPrime(num):
	if(num < 2): return  False
	if(num == 2): return True
	for factor in xrange(2, int(num**0.5)+1):
		if(num%factor == 0): return False
	return True


def isLegal(sdi):
	if(("3" in sdi) or ("4" in sdi) or ("7" in sdi)): return False
	or1 = isPrime(int(sdi))
	sdi = sdi[::-1]
	sdi = sdi.replace("6", "#")
	sdi = sdi.replace("9", "6")
	sdi = sdi.replace("#", "9")
	or2 = isPrime(int(sdi))
	return or1 and or2


sdi = (raw_input())
if(isLegal(sdi)): print("yes")
else: print("no")
