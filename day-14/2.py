import sys
import math
import time

INPUT = sys.argv[1]
w = 101
h = 103

robots = []
with open(INPUT, "r") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        line = line.strip()
        pos_t = line.split("p=")[1].split(" ")[0].split(",")
        vel_t = line.split("v=")[1].split(",")
        pos = int(pos_t[0]), int(pos_t[1])
        vel = int(vel_t[0]), int(vel_t[1])
        robots.append((pos, vel))

num = [[0 for _ in range(w)] for _ in range(h)]
for robot in robots:
    pos = robot[0]
    num[pos[1]][pos[0]] += 1


def check() -> int:
    max_len = 0

    for y in range(h):
        ln = 0
        for x in range(w):
            if num[y][x] > 0:
                ln += 1
            else:
                max_len = max(max_len, ln)
                ln = 0
        max_len = max(max_len, ln)
    for x in range(w):
        ln = 0
        for y in range(h):
            if num[y][x] > 0:
                ln += 1
            else:
                max_len = max(max_len, ln)
                ln = 0
        max_len = max(max_len, ln)
    return max_len


for t in range(100000):
    if check() > 4:
        output = f"\nIteration {t}\n"
        for y in range(h):
            for x in range(w):
                if num[y][x] > 0:
                    output += "#"
                else:
                    output += " "
            output += "\n"
        print(output)
        time.sleep(0.2)

    new_robots = []
    for robot in robots:
        pos = robot[0]
        vel = robot[1][0], robot[1][1]
        num[pos[1]][pos[0]] -= 1

        x = (pos[0] + vel[0]) % w
        y = (pos[1] + vel[1]) % h
        num[y][x] += 1
        new_robots.append(((x, y), vel))

    robots = new_robots
