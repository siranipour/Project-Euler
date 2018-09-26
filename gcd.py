def gcd(a,b):
	x = max(a,b)
	y = min(a,b)

	if x % y == 0:
		return y
	else:
		return gcd(y, x % y) 
