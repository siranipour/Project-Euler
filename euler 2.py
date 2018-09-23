import numpy as np
import time
import math
t0 = time.time()

def numDigits(testNum, digit):
    testNum = str(testNum)
    total = 0
    for i in range(len(testNum)):
        if int(testNum[i]) == digit:
            total += 1
    return total

def mFunction(d, numbers = []):
    max = 0
    maxNumbers = []
    for i in numbers:
        if numDigits(i, d) > max:
            maxNumbers = []
            maxNumbers.append(i)
            max = numDigits(i, d)
        elif numDigits(i, d) == max:
            maxNumbers.append(i)
    return maxNumbers

def primeGen(limit):
    a = [True] * limit
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False


n = 10
tempPrimes = primeGen(10**n)

primes = [i for i in tempPrimes if math.log(i,10) > n-1]

sum = 0
for i in range(10):
    sum += np.sum(mFunction(i, primes))

t1 = time.time()
print(sum, ' found in ', t1-t0, 'seconds')
