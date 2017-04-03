import string
"""def gapbuf_forward(gapbuf, limit, gap_start, gap_end): # ["t", "e", "s", "t", "<<", ">>"] start = 3 end = 5
	sign = gapbuf[gap_start]
	gapbuf[gap_start] = gapbuf[gap_end]
	for space in range(gap_start+1, gap_end+1):
		newSign = gapbuf[space]
		gapbuf[space] = sign
		sign = newSign
	return gapbuf

def gapbuf_backward(gapbuf, limit, gap_start, gap_end):
	sign = gapbuf[gap_end-1]
	gapbuf[gap_end-1] = gapbuf[gap_start-1]
	for space in range(gap_end-2, gap_start-2, -1):
		newSign = gapbuf[space]
		gapbuf[space] = sign
		sign = newSign
	return gapbuf


print(gapbuf_forward (["t", "e", "s", ".", "..", "...", "....", "t", "a", "b", "d"], 10, 3, 7)) 
print(gapbuf_backward(["t", "e", "s", ".", "..", "...", "....", "t", "a", "b", "d"], 10, 3, 7))"""


def createSub8(alphalist, index):
	list1 = [0]*16
	list2 = [0]*16
	count = 0
	for i1 in range(0, index):
		list1[i1] = alphalist[count]
		count += 1
	for j1 in range(index, index+8):
		list1[j1] = "."
	for k1 in range(index+8, 16):
		list1[k1] = alphalist[count]
		count += 1
	for i2 in range(0, 8):
		list2[i2] = "."
	for j2 in range(8, 16):
		list2[j2] = alphalist[count]
		count += 1
	return(list1, list2)

def createOver8(alphalist, index):
	index = index - 8
	list1 = [0]*16
	list2 = [0]*16
	count = 0
	for i1 in range(0, 8):
		list1[i1] = alphalist[count]
		count += 1
	for j1 in range(8, 16):
		list1[j1] = "."
	for i2 in range(0, index):
		list2[i2] = alphalist[count]
		count += 1
	for j2 in range(index, index+8):
		list2[j2] = "."
	for k2 in range(index+8, 16):
		list2[k2] = alphalist[count]
		count += 1
	return(list1, list2)

def create8(alphalist):
	list1 = [0]*16
	list2 = [0]*16
	for i in range(0, 8):
		list1[i] = alphalist[i]
		list2[i] = "."
	for j in range(8, 16):
		list1[j] = "."
		list2[j] = alphalist[j]
	return(list1, list2)

alphalist = [i for i in string.ascii_lowercase[0:16]]

print(createSub8(alphalist, 3))
print(createOver8(alphalist, 12))
print(create8(alphalist))

