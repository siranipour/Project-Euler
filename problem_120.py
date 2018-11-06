# This problem is solved by the following logic:
# The remainder is always 2an and we wish to find the maximum value
# of this modulo a^2. We know the minimum is when 2*a*n = a^2 so the maximum happens
# when 2*a*n = a^2 - 1. However, this doesn't always give integer n, so we must take the
# floor i.e ineger division.


def rmax(a):
    return 2 * a * ((a**2 - 1) // (2 * a))

total = 0

for i in range(3, 1001):
    total += rmax(i)

print(total)