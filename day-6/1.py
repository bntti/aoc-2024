INPUT = "input"
# INPUT = "test1.in"

grid = []
visited = []
start = (0, 0)
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir = 0
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append(line)
        visited.append([False for _ in range(len(line))])
        if "^" in line:
            start = (line.find("^"), i)


res = 0
pos = start
while True:
    (x, y) = pos
    if not visited[y][x]:
        visited[y][x] = True
        res += 1
    new_x = x + dirs[dir][1]
    new_y = y + dirs[dir][0]
    if not (0 <= new_x < len(grid[0])) or not (0 <= new_y < len(grid)):
        break
    if grid[new_y][new_x] == "#":
        dir = (dir + 1) % 4
    else:
        pos = (new_x, new_y)
print(res)

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if visited[y][x]:
            print("!", end="")
        else:
            print(grid[y][x], end="")
    print()
