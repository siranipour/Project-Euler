import numpy as np

#Generating generalised pentagonal numbers
def pent(k):
	return int(k * (3 * k - 1) / 2)

#Decorating a memoization feature
def memoDec(func):
	memo = {}

	def memoWrapper(n):
		if n not in memo:
			memo[n] = func(n)
		return memo[n]
	return memoWrapper


@memoDec
def p(n):
	if n == 0:
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
		return sum(list(map(func, k)))

n = 0
while p(n) % (10 ** 6) != 0:
	n += 1

print("P(n) = 0 (mod 10^6) for n = {}" .format(n))