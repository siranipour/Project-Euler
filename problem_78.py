import numpy as np

#Generating generalised pentagonal numbers
def pent(k):
	return int(k * (3 * k - 1) / 2)

#Cache used for memoization
cache = {}
def p(n):
	if n in cache:
		return cache[n]
	elif n == 0:
		return 1
	elif n < 0:
		return 0
	else:
		upper = int(np.ceil((np.sqrt(24 * n + 1) + 1) / 6))
		lower = int(np.floor(-(np.sqrt(24 * n + 1)- 1) / 6)) 

		k = [i for i in range(lower, upper + 1)]
		k.remove(0)
		k = list(k)
		#Recursion formula from wiki article
		func = lambda x: int((-1) ** (abs(x) - 1)) * p(n - pent(x))
		result =  sum(list(map(func, k)))
		cache[n] = result
		return result

# n = 0
# while p(n) % (10 ** 6) != 0:
# 	n += 1


# print(n)