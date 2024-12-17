import sys
import time
from tqdm import tqdm
import math

INPUT = sys.argv[1]

init_reg = [0, 0, 0]
ops = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for shift, line in enumerate(lines):
        line = line.strip()
        if line.startswith("Register A: "):
            init_reg[0] = int(line.split(": ")[1])
        elif line.startswith("Register B: "):
            init_reg[1] = int(line.split(": ")[1])
        elif line.startswith("Register C: "):
            init_reg[2] = int(line.split(": ")[1])
        elif line.startswith("Program: "):
            data = line.split(": ")[1].split(",")
            for bitmask in data:
                ops.append(int(bitmask))


results = []


def run(a) -> int:
    global results
    oa = a
    b = 0
    c = 0
    i = 0
    while a > 0:
        # The instructions
        b = (a & 7) ^ 3
        c = a >> b
        a >>= 3
        b = b ^ 5 ^ c

        out = b & 7
        if ops[i] != out:
            return i
        if i == len(ops):
            return i
        i += 1

    if i == len(ops):
        if oa not in results:
            results.append(oa)
            mn = min(results)
            print(f"Result found {oa} {oa==mn=}\nCurrent min: {mn} ")
        return -1
    return i


# Contains some arbitrary values that seem to work
def solve(i, opts) -> list[int]:
    # i is the number of solved numbers so far
    t = i + 1  # Target of nums correct

    new_opts = []
    for x in tqdm(range(1 << 18)):
        for opt in opts:
            a = opt | (x << (i * 3))
            res = run(a)

            # Make sure we don't mess up later numbers
            # by fixing the lower ones
            if res >= t + 3 or res == -1:
                str_val = str(bin(a))[-(t * 3) :]
                val = int("0b" + str_val, 2)

                if val not in new_opts:
                    new_opts.append(val)
    return new_opts


opts = [0]
for i in range(16):
    print(i, opts)
    opts = solve(i, opts)
