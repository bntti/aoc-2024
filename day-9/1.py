INPUT = "input"
# INPUT = "test1.in"

input = ""
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        input = line

data = []
skip = False
id = 0
for c in input:
    num = int(c)
    for i in range(int(c)):
        if skip:
            data.append(-1)
        else:
            data.append(id)
    skip = not skip
    if skip:
        id += 1
print(data)

for i in range(len(data)):
    if i >= len(data):
        break

    if data[i] != -1:
        continue
    while data[-1] == -1:
        data.pop()
    if i >= len(data):
        break
    data[i] = data[-1]
    data.pop()
print(data)

res = 0
for i, x in enumerate(data):
    if x < 0:
        continue
    res += i * x
print(res)
