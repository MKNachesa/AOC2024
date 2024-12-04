import numpy as np

inp = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""

with open("day2.txt") as infile:
    inp = infile.read()

max_width = max(len(line) for line in inp.split("\n"))
inp = np.stack([np.pad(np.array(line.split(), dtype=int), (0, max_width-len(line.split()))) for line in inp.split("\n")][:-1], dtype=int)

diff = inp[:, :-1] - inp[:, 1:]

res = np.sum(((0 < diff) & (diff <= 3)).all(axis=-1, where=inp[:, 1:] != 0) + ((-3 <= diff) & (diff < 0)).all(axis=-1, where=inp[:, 1:] != 0))
# res = np.sum((((0 < diff) & (diff <= 3)).sum(axis=-1) == ((inp != 0).sum(axis=-1) - 1)) + (((-3 <= diff) & (diff < 0)).sum(axis=-1) == ((inp != 0).sum(axis=-1) - 1)))
print(f"Part one: {res}")

res1 = np.sum(res)
res = ((0 < diff) & (diff <= 3)).all(axis=-1, where=inp[:, 1:] != 0) + ((-3 <= diff) & (diff < 0)).all(axis=-1, where=inp[:, 1:] != 0)
inp = inp[~res]
diff = diff[~res]
res = ((0 < diff) & (diff <= 3)).all(axis=-1, where=inp[:, 1:] != 0) + ((-3 <= diff) & (diff < 0)).all(axis=-1, where=inp[:, 1:] != 0)
for i in range(max_width):
    tmp_inp = np.concatenate([inp[:, :i], inp[:, i+1:]], axis=-1)
    diff = tmp_inp[:, :-1] - tmp_inp[:, 1:]
    res += ((0 < diff) & (diff <= 3)).all(axis=-1, where=tmp_inp[:, 1:] != 0) + ((-3 <= diff) & (diff < 0)).all(axis=-1, where=tmp_inp[:, 1:] != 0)

res2 = np.sum(res)
res = res1 + res2
# res = np.sum((((0 < diff) & (diff <= 3)).sum(axis=-1, where=inp[:, 1:] != 0) >= ((inp != 0).sum(axis=-1) - 1)) + (((-3 <= diff) & (diff < 0)).sum(axis=-1, where=inp[:, 1:] != 0) >= ((inp != 0).sum(axis=-1) - 1)))
print(f"Part two: {res}")