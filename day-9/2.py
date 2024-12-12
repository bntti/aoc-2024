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
pos = []
for c in input:
    if not skip:
        pos.append(len(data))
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


def lenn(i: int, data: list[int]) -> int:
    x = data[i]
    num = 1
    for j in range(i + 1, len(data)):
        if data[j] != x:
            break
        num += 1
    return num


print(pos)
for i in range(len(pos) - 1, -1, -1):
    num = lenn(pos[i], data)
    for j in range(0, pos[i]):
        if data[j] == -1 and lenn(j, data) >= num:
            print(f"Moving {i} (x{num}) from {pos[i]} to {j}")
            for k in range(num):
                data[j + k] = i
                data[pos[i] + k] = -1
            break
    print(i)

print(data)

res = 0
for i, x in enumerate(data):
    if x < 0:
        continue
    res += i * x
print(res)
