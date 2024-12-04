import numpy as np
from scipy.signal import convolve2d

inp = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""

with open("day4.txt") as infile:
    inp = infile.read()

xmas = np.array([list(line) for line in inp.split("\n")[:-1]])

xmases = 0
for line in xmas:
    line = "".join(line)
    xmases += line.count("XMAS")
    xmases += line[::-1].count("XMAS")

for i in range(len(xmas[0])):
    line = "".join(xmas[:, i])
    xmases += line.count("XMAS")
    xmases += line[::-1].count("XMAS")

diaglen = max(xmas.shape)

minus = -(len(xmas[0])-1)
plus = len(xmas[0])
for k in range(minus, plus):
    a = np.array(list(zip(range(diaglen), range(diaglen))))
    a[:, 1] += k
    line = "".join([xmas[i:i+1, j:j+1][0][0] if len(xmas[i:i+1, j:j+1]) == 1 else ""  for i, j in list(filter(lambda x: x[1] >= 0 and x[1] < len(xmas[0]), a.tolist()))])
    xmases += line.count("XMAS")
    xmases += line[::-1].count("XMAS")

for k in range(minus, plus):
    a = np.array(list(zip(range(diaglen), range(diaglen)[::-1])))
    a[:, 1] += k
    line = "".join([xmas[i:i+1, j:j+1][0][0] if len(xmas[i:i+1, j:j+1]) == 1 else ""  for i, j in list(filter(lambda x: x[1] >= 0 and x[1] < len(xmas[0]), a.tolist()))])
    xmases += line.count("XMAS")
    xmases += line[::-1].count("XMAS")

res = xmases
print(f"Part one: {res}")

#-------------------------------------------------------
x_to_num = {"A": 26, "S": 4, "M": 100, "X": 1000}
xmas = np.array([list(map(lambda x: x_to_num[x], list(line))) for line in inp.split("\n")[:-1]])
x = np.array([[-2,0,1],
              [0,4,0],
              [1,0,-2]])

conv = convolve2d(xmas, x, "valid")
res = np.sum(conv == 0)
print(f"Part two: {res}")