import numpy as np 
from tqdm import tqdm

limit = 64 * (10**6)

grid = np.zeros(limit - 1, dtype = 'uint64')


for i in tqdm(range(1,limit)):
    grid[i-1::i] += i**2


root = np.sqrt(grid).astype(int)
condition = np.square(root) == grid
answer = np.dot(condition, np.arange(1, limit))

print("The answer is {}".format(answer))