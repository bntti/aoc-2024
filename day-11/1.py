INPUT = "input"
# INPUT = "test1.in"

nums = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        nums = [int(x) for x in line.split(" ")]


for _ in range(25):
    new_nums = []
    for num in nums:
        if num == 0:
            new_nums.append(1)
        elif len(str(num)) % 2 == 0:
            n = len(str(num)) // 2
            new_nums.append(int(str(num)[:n]))
            new_nums.append(int(str(num)[n:]))
        else:
            new_nums.append(num * 2024)
    # print(new_nums)
    nums = new_nums

print(len(nums))
