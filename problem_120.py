def rmax(a):
    return 2 * a * ((a**2 - 1) // (2 * a))

total = 0

for i in range(3, 1001):
    total += rmax(i)
print(total)