a = []
b = []

with open("input", "r") as f:
    lines = f.readlines()

for line in lines:
    a.append(int(line.split("  ")[0].strip()))
    b.append(int(line.split("  ")[1].strip()))

a.sort()
b.sort()
res = 0
for i in range(len(a)):
    res += abs(a[i] - b[i])
print(res)
