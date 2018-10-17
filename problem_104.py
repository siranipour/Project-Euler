import sys
import math
sys.setrecursionlimit(1000000)

memo = {}
def memoDec(func):
	def memoWrapper(n):
		if n in memo:
			return memo[n]
		else:
			result = func(n)
			memo[n] = result
			return result

	return memoWrapper

@memoDec
def fib(n):
	if n == 1 or n == 2:
		return 1
	else:
		return fib(n - 1) + fib(n - 2)

def firstDigits(num):
	if num > 10**40:
		num = num // 10 ** 30	
	n = 9
	return num // 10 ** (int(math.log(num, 10)) - n + 1)

def lastDigits(num):
	return num % 10 ** 9

def unique(str):
	count = {}
	for s in str:
		if s in count:
			count[s] += 1
		else:
			count[s] = 1

	valid  = True
	for n in count:
		if count[n] > 1:
			valid = False
			break
	return valid

def test(n):
	end = str(lastDigits(n))
	
	if '0' not in end and unique(end):
		start = str(firstDigits(n))
		if '0' not in start and unique(start):
			return True
	else:
		return False

		
	
def main():
	i = 450
	while not test(fib(i)):
		i += 1
		if i % 10 ** 3 == 0:
			print(i)
	print(i)

