import math
import numpy as np
import sys

sys.setrecursionlimit(10**5)
def func(x):
	return np.floor(2**(30.403243784 - (x ** 2))) * (10 ** - (9))

def recur(n):
	if n == 0:
		return -1
	else:
		return func(recur(n - 1))

i = 0
while abs(recur(i + 2) - recur(i)) > 10**-9:
    i += 10

print(recur(i + 1)+recur(i))