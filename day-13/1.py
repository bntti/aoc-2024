import sys

INPUT = sys.argv[1]

test_cases = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    test_case = []
    for i, line in enumerate(lines):
        line = line.strip()
        if "Button A:" in line or "Button B:" in line:
            x = int(line.split("X+")[1].split(", ")[0])
            y = int(line.split("Y+")[1])
            test_case.append([x, y])
        elif "Prize:" in line:
            x = int(line.split("X=")[1].split(", ")[0])
            y = int(line.split("Y=")[1])
            test_case.append([x, y])
            test_cases.append(test_case)
            test_case = []

print(test_cases)
res = 0
for case in test_cases:
    a = case[0]
    b = case[1]
    total = case[2]
    best = int(1e9)
    for i in range(101):
        for j in range(101):
            if a[0] * i + b[0] * j == total[0] and a[1] * i + b[1] * j == total[1]:
                best = min(best, i * 3 + j)
    if best != int(1e9):
        res += best
print(res)
