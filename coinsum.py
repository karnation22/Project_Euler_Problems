def findIterations(target):
	coins = [1,2,5,10,20,50,100, 200]
	ways = [0]*(target+1)
	ways[0] = 1 
	for index in range(0, len(coins)): #determine total combos for all coins
		for subindex in range(coins[index], target+1):
			ways[subindex] += ways[subindex - coins[index]]
	return ways

print(findIterations(200))



