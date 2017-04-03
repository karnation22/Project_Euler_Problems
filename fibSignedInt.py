def binsearch(x, A, n):
	(lower, upper) = (0,n)
	while(lower <= upper):
		mid = int(lower + 0.5*(upper - lower))
		if(A[lower] == x): return lower
		if(A[mid] == x): lower = mid + 1
		else: upper = mid
		
	return -1

print(binsearch(8, [0,1,2,3,4,5,6], 7))