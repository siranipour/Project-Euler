import math
import numpy as np
import time

start = time.time()
def testNum(n):
    n = str(n)
    if n[::2] == '1234567890':
        return True
    else:
        return False

min = int(np.floor(math.sqrt(1020304050607080900)))
max = int(np.ceil(math.sqrt(1929394959697989990))) + 1


for i in range(min,max):
    if (i - min) % 10000 == 0:
        print((i - min) / (max - min))
    if testNum(i ** 2):
        print(i)
        break

end = time.time()
print('Calculated in', end - start ,'seconds')