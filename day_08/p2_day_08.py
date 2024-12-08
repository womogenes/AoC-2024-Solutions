from collections import defaultdict
from itertools import combinations

with open("./day_08.in") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)

def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n

def get_antinodes(a, b):
    ax, ay = a
    bx, by = b
    
    dx, dy = bx - ax, by - ay

    i = 0
    while True:
        if in_bounds(ax - dx * i, ay - dy * i):
            yield (ax - dx * i, ay - dy * i)
        else:
            break
        i += 1
    
    i = 0
    while True:
        if in_bounds(bx + dx * i, by + dy * i):
            yield (bx + dx * i, by + dy * i)
        else:
            break
        i += 1


antinodes = set()

all_locs = defaultdict(list)
for i in range(n):
    for j in range(n):
        if grid[i][j] != ".":
            all_locs[grid[i][j]].append((i, j))


for freq in all_locs:
    locs = all_locs[freq]
    for a, b in combinations(locs, r=2):
        for antinode in get_antinodes(a, b):
            antinodes.add(antinode)


for i in range(n):
    for j in range(n):
        if (i, j) in antinodes:
            print("#", end="")
        else:
            print(grid[i][j], end="")
    print()


print(len(antinodes))
