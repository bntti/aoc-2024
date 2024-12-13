import sys
import sys
from mip import INTEGER, Model, OptimizationStatus

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


# I'm to lazy to do this properly
# You probably would just check if the vectors A and B are linearly dependent
# and otherwise just check if the one unique solution exists.
def solve(ax, bx, total):
    m = Model()
    a = m.add_var(var_type=INTEGER)
    b = m.add_var(var_type=INTEGER)

    m.objective = 3 * a + b

    m += a * ax[0] + b * bx[0] == total[0]
    m += a * ax[1] + b * bx[1] == total[1]

    status = m.optimize()
    if status == OptimizationStatus.OPTIMAL:
        return int(a.x * 3 + b.x)
    else:
        return 0


res = 0
for case in test_cases:
    ax = case[0]
    bx = case[1]
    total = [case[2][0] + 10000000000000, case[2][1] + 10000000000000]
    print(f"Starting case {ax} {bx} {total}")
    res += solve(ax, bx, total)


print(res)
