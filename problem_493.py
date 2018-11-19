def fact(n):
	if n == 1:
		return 1
	else:
		return n * fact(n - 1)

def nCr(n, r):
	return fact(n) // (fact(n-r)*fact(r))

print(7 * (1- (nCr(60,20)/(nCr(70,20)))))
