import re
import numpy as np

inp = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

with open("day3.txt") as infile:
    inp = infile.read()

muls = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", inp)

nums = np.stack([np.array(mul[4:-1].split(","), dtype=int) for mul in muls])

res = np.sum(np.prod(nums, axis=-1))

print(f"Part one: {res}")

# inp = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

muls = re.findall(r"(mul\([0-9]{1,3},[0-9]{1,3}\)|don't|do)", inp)

i = 0
do = True
while i != len(muls):
    mul = muls[i]
    if mul == "don't":
        do = False
    elif mul == "do":
        do = True
        del muls[i]
    if not do:
        del muls[i]
    else:
        i += 1

nums = np.stack([np.array(mul[4:-1].split(","), dtype=int) for mul in muls])

res = np.sum(np.prod(nums, axis=-1))

print(f"Part two: {res}")