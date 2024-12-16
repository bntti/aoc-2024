import sys
import math

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

end_pos = 0
q = [0, 0, 0, 0]
for robot in robots:
    pos = robot[0]
    diff = robot[1][0] * 100, robot[1][1] * 100
    x = (pos[0] + diff[0]) % w
    y = (pos[1] + diff[1]) % h

    if x == w // 2 or y == h // 2:
        continue
    qi = int(x < w // 2) + int(y < h // 2) * 2
    q[qi] += 1
print(q)
print(q[0] * q[1] * q[2] * q[3])
