INPUT = "input"
# INPUT = "test1.in"

rules = {}
updates = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()

        if "|" in line:
            a = int(line.split("|")[0])
            b = int(line.split("|")[1])
            if a not in rules:
                rules[a] = set()
            rules[a].add(b)
        elif "," in line:
            nums = line.split(",")
            updates.append([int(x) for x in nums])

res = 0
for update in updates:
    ok = True
    for i, x in enumerate(update):

        if x not in rules:
            continue
        for j in range(i):
            if update[j] in rules[x]:
                ok = False
    if ok:
        res += update[len(update) // 2]
print(res)
