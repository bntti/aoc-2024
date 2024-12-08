INPUT = "input"
# INPUT = "test1.in"


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def escape(grid: list[str], start: tuple[int, int]) -> bool:
    h = len(grid)
    w = len(grid[0])
    pos = start
    dir = 0
    visited = [[False for _ in range(w)] for _ in range(h)]
    for _ in range(w * h * 4):
        (x, y) = pos
        if not visited[y][x]:
            visited[y][x] = True
        new_x = x + dirs[dir][1]
        new_y = y + dirs[dir][0]
        if not (0 <= new_x < len(grid[0])) or not (0 <= new_y < len(grid)):
            return True
        if grid[new_y][new_x] == "#":
            dir = (dir + 1) % 4
        else:
            pos = (new_x, new_y)
    return False


grid = []
start = (0, 0)
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append(line)
        if "^" in line:
            start = (line.find("^"), i)


res = 0
h = len(grid)
w = len(grid[0])
for y in range(h):
    for x in range(w):
        if grid[y][x] != ".":
            continue
        grid[y] = grid[y][:x] + "#" + grid[y][x + 1 :]
        if not escape(grid, start):
            res += 1
        grid[y] = grid[y][:x] + "." + grid[y][x + 1 :]
print(res)
