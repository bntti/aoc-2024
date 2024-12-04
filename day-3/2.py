import re

with open("input", "r") as f:
    # with open("test2.in", "r") as f:
    lines = f.readlines()

res = 0
enabled = True
for line in lines:
    matches = re.findall("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)", line.strip())
    for match in matches:
        print(match)
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled:
            assert match.startswith("mul(")
            match = match.split("(")[1]
            match = match.split(")")[0]
            a = int(match.split(",")[0])
            b = int(match.split(",")[1])
            res += a * b
print(res)
