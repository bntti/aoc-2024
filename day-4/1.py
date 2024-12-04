puzzle = []
with open("input", "r") as f:
    # with open("test.in", "r") as f:
    lines = f.readlines()
    for line in lines:
        puzzle.append(line.strip())

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

res = 0
word = "XMAS"
h = len(puzzle)
w = len(puzzle[0])
for y in range(h):
    for x in range(w):
        if puzzle[y][x] != "X":
            continue

        for dir in dirs:
            for i in range(1, 4):
                new_x = x + i * dir[0]
                new_y = y + i * dir[1]
                if not (0 <= new_x < w):
                    continue
                if not (0 <= new_y < h):
                    continue
                if puzzle[new_y][new_x] != word[i]:
                    break
                if i == 3:
                    res += 1
print(res)
