with open("input", "r") as f:
    # with open("test.in", "r") as f:
    lines = f.readlines()


def remove(a, i):
    return a[:i] + a[i + 1 :]


def tryy(lst: list[str]) -> bool:
    diff = 0
    safe = True
    for i in range(1, len(lst)):
        new_diff = int(lst[i]) - int(lst[i - 1])

        if abs(new_diff) == 0 or abs(new_diff) > 3:
            safe = False
        elif diff < 0 and new_diff > 0:
            safe = False
        elif diff > 0 and new_diff < 0:
            safe = False

        diff = new_diff
    return safe


res = 0
for line in lines:
    nums = line.strip().split(" ")

    for i in range(len(nums)):
        safe = tryy(remove(nums, i))

        if safe:
            res += 1
            break
print(res)
