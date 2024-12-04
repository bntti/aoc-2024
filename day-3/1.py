import re

with open("input", "r") as f:
    lines = f.readlines()

res = 0
for line in lines:
    matches = re.findall("mul\\(\\d+,\\d+\\)", line.strip())
    for match in matches:
        match = match.split("(")[1]
        match = match.split(")")[0]
        a = int(match.split(",")[0])
        b = int(match.split(",")[1])
        res += a * b
print(res)
