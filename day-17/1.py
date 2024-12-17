import sys
import math

INPUT = sys.argv[1]

reg = [0, 0, 0]
ops = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if line.startswith("Register A: "):
            reg[0] = int(line.split(": ")[1])
        elif line.startswith("Register B: "):
            reg[1] = int(line.split(": ")[1])
        elif line.startswith("Register C: "):
            reg[2] = int(line.split(": ")[1])
        elif line.startswith("Program: "):
            data = line.split(": ")[1].split(",")
            for x in data:
                ops.append(int(x))

names = ["Adiv", "Bxor", "Bmod", "Jump", "BxorC", "Out", "BdivA", "CdivA"]
used = set()
i = 0
out = []
while i < len(ops):
    ins, op = ops[i], ops[i + 1]
    val = op
    if ins not in [1, 3] and op > 3:
        val = reg[op - 4]

    if ins not in used:
        print(ins)
        used.add(ins)
    # print(f"\n{i} -> {names[ins]} {val}({op})")
    # print(reg)

    if ins == 0:
        reg[0] //= 2**val
    elif ins == 1:
        reg[1] ^= val
    elif ins == 2:
        reg[1] = val % 8
    elif ins == 3:
        if reg[0] != 0:
            i = val - 2
    elif ins == 4:
        reg[1] ^= reg[2]
    elif ins == 5:
        out.append(val % 8)
    elif ins == 6:
        reg[1] = reg[0] // (2**val)
    elif ins == 7:
        reg[2] = reg[0] // (2**val)

    i += 2
    # print(reg)

print(",".join([str(x) for x in out]))
