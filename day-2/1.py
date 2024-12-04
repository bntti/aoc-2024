with open("input", "r") as f:
    lines = f.readlines()


res = 0
for line in lines:
    nums = line.strip().split(" ")

    diff = 0
    safe = True
    for i in range(1, len(nums)):
        new_diff = int(nums[i]) - int(nums[i - 1])

        if abs(new_diff) == 0 or abs(new_diff) > 3:
            safe = False
        elif diff < 0 and new_diff > 0:
            safe = False
        elif diff > 0 and new_diff < 0:
            safe = False

        diff = new_diff

    if safe:
        res += 1
print(res)
