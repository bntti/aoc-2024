INPUT = "input"
# INPUT = "test1.in"

grid = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append([int(c) for c in line])

h = len(grid)
w = len(grid[0])


def test(grid, used, x, y, v) -> int:
    if not (0 <= x < w):
        return 0
    if not (0 <= y < h):
        return 0
    if grid[y][x] != v:
        return 0

    if used[y][x]:
        return 0
    used[y][x] = 1

    if v == 9:
        return 1
    res = 0
    res += test(grid, used, x + 1, y, v + 1)
    res += test(grid, used, x - 1, y, v + 1)
    res += test(grid, used, x, y + 1, v + 1)
    res += test(grid, used, x, y - 1, v + 1)
    return res


res = 0
for y in range(h):
    for x in range(w):
        used = [[0 for _ in range(w)] for _ in range(h)]
        res += test(grid, used, x, y, 0)
        # print(x, y, res)
        # for z in used:
        #     print(z)
        # print(0)
        # for z in grid:
        #     print(z)
        # if res > 0:
        #     exit(0)

print(res)
