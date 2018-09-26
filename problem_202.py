from gcd import gcd

reflections = 12017639147

m = int((reflections + 3) / 2)

total = 0
for i in range(int(m/2)+1):
    x, y = [i, m - i]
    if (x - y) % 3 == 0 and gcd(x, y) == 1:
        total += 1
    if i % 1000000 == 0:
        print(i/ (m/2))
print(2 * total)

