from tqdm import tqdm
from math import sqrt
 
def isPrime(number):
    for i in range(2, 1+ int(sqrt(number))):
        if number % i == 0:
            return 0
    return 1


total = 0
for i in tqdm(range(2, 577 + 1)):
    if isPrime(i**3 - (i - 1)**3):
        total += 1

print(total)