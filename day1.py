import numpy as np
from collections import Counter

inp = """3   4
4   3
2   5
1   3
3   9
3   3
"""

with open("day1.txt") as infile:
    inp = infile.read()

inp = np.array([line.split() for line in inp.split("\n")][:-1], dtype=int)

a = np.sort(inp[:, 0])
b = np.sort(inp[:, 1])

dists = np.abs(a - b)
res = np.sum(dists)
print(f"Part one: {res}")

#----------------------------------------------

c = Counter(b)

res = 0

for num in a:
    res += num * c[num]

print(f"Part two: {res}")