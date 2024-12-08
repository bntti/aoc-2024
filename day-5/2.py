INPUT = "input"
# INPUT = "test1.in"

rules = {}
revrules = {}
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
            if b not in revrules:
                revrules[b] = set()
            rules[a].add(b)
            revrules[b].add(a)
        elif "," in line:
            nums = line.split(",")
            updates.append([int(x) for x in nums])

res = 0
for update in updates:
    ok = True
    waiting = {}
    for i, x in enumerate(update):
        waiting[i] = set()
        if x in revrules:
            for y in update:
                if y in revrules[x]:
                    waiting[i].add(y)

        if x not in rules:
            continue
        for j in range(i):
            if update[j] in rules[x]:
                ok = False
    if ok:
        continue

    print()
    result = []
    while len(waiting) > 0:
        added = -1
        print(waiting)
        for key in waiting:
            wset = waiting[key]
            if len(wset) > 0:
                continue
            added = key
            break

        value = update[added]
        result.append(value)
        del waiting[added]
        for key in waiting:
            if value in waiting[key]:
                waiting[key].remove(value)
    print(result)
    res += result[len(update) // 2]

print(res)
