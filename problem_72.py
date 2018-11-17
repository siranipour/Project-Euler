from sympy.ntheory import factorint
from time import time
from tqdm import tqdm

def phi(n):
	temp = list(map(lambda x: (1 - 1 / x), list(factorint(n).keys())))
	result = 1
	for i in range(len(temp)):
		result *= temp[i]
	return round(result * n) 

def main(n):
	t1 = time()
	total = 0
	for i in tqdm(range(2, n + 1)):
		total += phi(i)
	t2 = time()
	print("Result is {} calculated in {}s".format(total, t2 - t1))
