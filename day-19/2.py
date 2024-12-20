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
    pos = [0 for _ in range(n + 1)]
    pos[0] = 1
    for i in range(n):
        for towel in towels:
            if target[i:].startswith(towel):
                pos[i + len(towel)] += pos[i]
    res += pos[n]

print(res)
