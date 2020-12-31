from sys import stdin
from itertools import permutations
def factorial(n):
    if(n<0): return Exception
    elif(n==0 or n==1): return 1
    else: return reduce(lambda x,y: x*y, [i for i in range(2,n)])
	
def findPowerList(str_num_L,saveCount):
    len_l = len(str_num_L)
    n_combos = factorial(len_l)/(factorial(saveCount)*factorial(len_l-saveCount))	
    perm = list(set(filter(lambda perm: len(perm)==saveCount, list(permutations(str_num_L)))))
    return list(map(lambda x: int("".join(x)), perm ))	     

def findLargestSmallest(strNum, deleteCount): #input strNum, output largest possible int
    saveCount=None,None,len(strNum-deleteCount)
    strNum_l=strNum.split("")
    powerList = sorted(findPowerList(str_num_L,saveCount)) 
    return powerList[0],powerList[-1]
	

def findWrapper(strNum):
	strNumP_l = strNum.split(" ")
	strNum, deleteCount = strNumP_l[0], strNumP_l[1]
	print(findLargestSmallest(strNum, deleteCount))
	


test = """3
00123 2
00123 3
234714812741111111111111111111 4"""
sdi = (stdin.readlines())#list of strings
sdi = test.split("\n")
sdi = sdi[1:] #who cares of that first element(length of list python native)
for elem in sdi:
	elem = elem.strip()
	print(elem)
	print(findWrapper(elem))
