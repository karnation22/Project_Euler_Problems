def isPrime(num):
    return bool(reduce(lambda x,y: bool(num%x==0) or bool(num%y==0), enumerate(2,int(num**0.5)+1)))

## sum of five primes
def generatePrime():
    setsetPrimes=list(set())
    counter=2
    while(all(lambda(len s: len(s)<5, setsetPrimes)):
        if(isPrime(counter)):
            for setVal in setsetPrimes:
                if(counter not in setVal): setVal.add(counter)
    return sum(max(setsetPrimes))
        