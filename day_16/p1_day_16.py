# Python heap implementation
from heapq import heappush, heappop

with open("./day_16.in") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)
for i in range(n):
    for j in range(n):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)

dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]

# DIjkstra's
q = [(0, 0, *start)]
seen = set()
while len(q) > 0:
    top = heappop(q)
    cost, d, i, j = top
    if (d, i, j) in seen:
        continue
    seen.add((d, i, j))

    if grid[i][j] == "#":
        continue

    if grid[i][j] == "E":
        print(cost)
        break
    
    ii = i + dd[d][0]
    jj = j + dd[d][1]

    for nbr in [(cost + 1, d, ii, jj),
                (cost + 1000, (d + 1) % 4, i, j),
                (cost + 1000, (d + 3) % 4, i, j)]:
        if nbr[1:] in seen:
            continue
        heappush(q, nbr)
