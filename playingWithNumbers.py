from sys import stdin

def findLargest(strNum): #input strNum, output largest possible int
	
			

def findSmallest(strNum): #input strNum, output largest possible int
	
	

def findWrapper(strNum):
	deleteCount = int(strNum[-1])
	strNum = strNum[:len(strNum) - 2]
	print(findSmallest(strNum, deleteCount))
	print(findLargest(strNum, deleteCount))


test = """3
00123 2
00123 3
234714812741111111111111111111 4"""
sdi = (stdin.readlines())#list of strings
sdi = test.split("\n")
sdi = sdi[1:] #who cares of that first element
for elem in sdi:
	elem = elem.rstrip()
	print(elem)
	print(findWrapper(elem))
