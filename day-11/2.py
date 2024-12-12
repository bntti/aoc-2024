INPUT = "input"
# INPUT = "test1.in"

nums = {}
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        for x in line.split(" "):
            x = int(x)
            if x not in nums:
                nums[x] = 0
            nums[x] += 1


def add(dict, x, num) -> None:
    if x not in dict:
        dict[x] = 0
    dict[x] += num


for _ in range(75):
    new_nums = {}
    for x in nums:
        num = nums[x]

        if x == 0:
            add(new_nums, 1, num)
        elif len(str(x)) % 2 == 0:
            n = len(str(x)) // 2
            add(new_nums, int(str(x)[:n]), num)
            add(new_nums, int(str(x)[n:]), num)
        else:
            add(new_nums, x * 2024, num)
    nums = new_nums

res = 0
for key in nums:
    res += nums[key]
print(res)
