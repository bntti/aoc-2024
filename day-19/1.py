import sys
import math

INPUT = sys.argv[1]

towels = []
targets: list[str] = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) == 0:
            continue

        if "," in line:
            towels = line.split(", ")
        else:
            targets.append(line)

res = 0
for target in targets:
    n = len(target)
    pos = [False for _ in range(n + 1)]
    pos[0] = True
    for i in range(n):
        if not pos[i]:
            continue
        for towel in towels:
            if target[i:].startswith(towel):
                pos[i + len(towel)] = True
    if pos[n]:
        res += 1

print(res)
