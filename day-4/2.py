puzzle = []
with open("input", "r") as f:
    # with open("test2.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        puzzle.append(line.strip())

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

res = 0
word = "XMAS"
h = len(puzzle)
w = len(puzzle[0])
for y in range(1, h - 1):
    for x in range(1, w - 1):
        if puzzle[y][x] != "A":
            continue

        chars1 = [puzzle[y - 1][x - 1], puzzle[y + 1][x + 1]]
        chars1.sort()

        chars2 = [puzzle[y + 1][x - 1], puzzle[y - 1][x + 1]]
        chars2.sort()
        if (
            chars1[0] == "M"
            and chars1[1] == "S"
            and chars2[0] == "M"
            and chars2[1] == "S"
        ):
            res += 1
print(res)
