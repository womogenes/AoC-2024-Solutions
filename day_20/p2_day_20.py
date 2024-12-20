from collections import defaultdict, deque
from tqdm import tqdm
import copy

with open("./day_20.in") as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]

N = len(grid)
def in_grid(i, j):
    return 0 <= i < N and 0 <= j < N

for i in range(N):
    for j in range(N):
        if grid[i][j] == "S":
            si, sj = i, j
        elif grid[i][j] == "E":
            ei, ej = i, j

dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

# Determine OG path
path = [(si, sj)]
while path[-1] != (ei, ej):
    i, j = path[-1]
    for di, dj in dd:
        ii, jj = i + di, j + dj
        if not in_grid(ii, jj):
            continue
        if len(path) > 1 and (ii, jj) == path[-2]:
            continue
        if grid[ii][jj] == "#":
            continue
        
        path.append((ii, jj))
        break

og = len(path) - 1

times = {}
for t, coord in enumerate(path):
    times[coord] = og - t

max_len = 20
counts = defaultdict(int)
saved = {}
for t, coord in enumerate(tqdm(path, ncols=80)):
    i, j = coord
    for ii in range(i - max_len, i + max_len + 1):
        for jj in range(j - max_len, j + max_len + 1):
            time_used = abs(ii - i) + abs(jj - j)
            if not in_grid(ii, jj) or time_used > max_len or grid[ii][jj] == "#":
                continue

            rem_t = times[(ii, jj)]
            saved[(i, j, ii, jj)] = og - (t + rem_t + time_used)

ans = 0
for v in saved.values():
    if v >= 0: counts[v] += 1
    if v >= 100: ans += 1

print(ans)
