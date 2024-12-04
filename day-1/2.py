a = []
nums = {}

with open("input", "r") as f:
    lines = f.readlines()

for line in lines:
    a.append(int(line.split("  ")[0].strip()))
    b = int(line.split("  ")[1].strip())
    if b not in nums:
        nums[b] = 0
    nums[b] += 1


res = 0
for x in a:
    if x in nums:
        res += nums[x] * x
print(res)
