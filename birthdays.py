def findProb(N, people):
	notProb = 1
	for mult in range(1, people):
		notProb *= (1 - float(mult)/N)
	return 1 - notProb

def findProbability(N): #number of days
	prob = 0
	people = 0
	while(prob < 0.5):
		people += 1
		prob = findProb(N, people)
	return people

days = int(raw_input())
print(findProbability(days))