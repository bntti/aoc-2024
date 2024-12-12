import copy
import sys

INPUT = sys.argv[1]

grid = []
visited = []
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        grid.append(line)
        visited.append([False for _ in line])

empty_visited = copy.deepcopy(visited)
h = len(grid)
w = len(grid[0])


def sides(visited: list[list[bool]]) -> int:
    res = 0
    for y in range(0, h):
        inside_plus = False
        inside_minus = False

        for x in range(0, w):
            if visited[y][x] and ((y - 1 >= 0 and not visited[y - 1][x]) or (y == 0)):
                inside_minus = True
            elif inside_minus:
                inside_minus = False
                res += 1

            if visited[y][x] and (
                (y + 1 < h and not visited[y + 1][x]) or (y == h - 1)
            ):
                inside_plus = True
            elif inside_plus:
                inside_plus = False
                res += 1

        if inside_minus:
            res += 1
        if inside_plus:
            res += 1

    for x in range(0, w):
        inside_plus = False
        inside_minus = False

        for y in range(0, h):
            if visited[y][x] and ((x - 1 >= 0 and not visited[y][x - 1]) or (x == 0)):
                inside_minus = True
            elif inside_minus:
                inside_minus = False
                res += 1

            if visited[y][x] and (
                (x + 1 < w and not visited[y][x + 1]) or (x == w - 1)
            ):
                inside_plus = True
            elif inside_plus:
                inside_plus = False
                res += 1

        if inside_minus:
            res += 1
        if inside_plus:
            res += 1
    return res


def area(grid, visited, visited2, x, y) -> int:
    if visited[y][x]:
        return 0
    visited[y][x] = True
    visited2[y][x] = True

    a = 1
    val = grid[y][x]
    for dir in dirs:
        new_x = x + dir[0]
        new_y = y + dir[1]
        if not (0 <= new_x < w) or not (0 <= new_y < h):
            continue
        if grid[new_y][new_x] != val:
            continue
        a += area(grid, visited, visited2, new_x, new_y)
    return a


res = 0
for y in range(h):
    print(f"{y+1}/{h}")
    for x in range(w):
        visited2 = copy.deepcopy(empty_visited)
        a = area(grid, visited, visited2, x, y)
        if a == 0:
            continue
        per = sides(visited2)
        # print(grid[y][x], a, per)
        res += a * per

print(res)
