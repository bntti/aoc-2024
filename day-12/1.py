INPUT = "input"
# INPUT = "test1.in"

grid = []
visited = []
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append(line)
        visited.append([False for _ in line])

h = len(grid)
w = len(grid[0])


def check(grid, visited, x, y) -> tuple[int, int]:
    if visited[x][y]:
        return (0, 0)
    visited[x][y] = True

    a = 1
    per = 4
    val = grid[y][x]
    for dir in dirs:
        new_x = x + dir[0]
        new_y = y + dir[1]
        if not (0 <= new_x < w) or not (0 <= new_y < h):
            continue
        if grid[new_y][new_x] != val:
            continue
        per -= 1
        res = check(grid, visited, new_x, new_y)
        a += res[0]
        per += res[1]
    return (a, per)


res = 0
for y in range(h):
    for x in range(w):
        vals = check(grid, visited, x, y)
        res += vals[0] * vals[1]

print(res)
