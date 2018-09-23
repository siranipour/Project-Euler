def gcd(a,b):
	a = max(a,b)
	b = min(a,b)
	if a%b == 0:
		return b
	else:
		r = a % b
		return gcd(b,r) 
	a = max(a,b)
	b = min(a,b)
	if a%b == 0:
		return b
	else:
		r = a % b
		return gcd(b,r) 
