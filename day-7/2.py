# INPUT = "input"
INPUT = "test1.in"

inputs = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        total = int(line.split(": ")[0])
        nums = line.split(": ")[1].split(" ")

        new_input = [total]
        for num in nums:
            new_input.append(int(num))
        inputs.append(new_input)

res = 0
for input in inputs:
    target = input[0]
    poss = [input[1]]
    for num in input[2:]:
        new_poss = []
        for pos in poss:
            new_poss.append(pos * num)
            new_poss.append(pos + num)
            new_poss.append(int(str(pos) + str(num)))
        poss = new_poss
    for num in poss:
        if num == target:
            res += target
            break
print(res)
