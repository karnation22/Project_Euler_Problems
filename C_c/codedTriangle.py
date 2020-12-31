import string
def getTNum(line):
	TSum = 0
	for letter in line:
		if letter in string.ascii_uppercase: 
			TSum += string.ascii_uppercase.index(letter) + 1
	return TSum

def isTNum(tSum):
	for number in range(1, 2*int(tSum**0.5)+1):
		if 0.5*number*(number+1) == tSum: return True
	return False 

def findAllTriangles():
	sum = 0
	f = open('words.txt', 'r')
	lines = f.readlines()
	lines = lines[0] #first we make it a string
	lines = lines.split(",") #now we make it a list
	for line in lines:
		tSum = getTNum(line)
		if(isTNum(tSum)): sum += 1
	return sum

print(findAllTriangles())
tup = (1,2,3)
lit = list(tup)
print(lit)

def factorial(num):
        if(num == 0 or num == 1): return 1
        ans = 1
        while(num > 1):
       		ans *= num
        	num -= 1
        return ans
print(factorial(7))
		



