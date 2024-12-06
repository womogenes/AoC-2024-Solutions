import copy
from tqdm import tqdm

with open("./day_06.in") as fin:
    grid = [list(line) for line in fin.read().strip().split("\n")]

n = len(grid)
m = len(grid[0])

found = False
for i in range(n):
    for j in range(m):
        if grid[i][j] == "^":
            found = True
            break

    if found:
        break

ii = i
jj = j

dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def will_loop(oi, oj):
    if grid[oi][oj] == "#":
        return False
    
    grid[oi][oj] = "#"
    i, j = ii, jj

    dir = 0
    seen = set()
    while True:
        if (i, j, dir) in seen:
            grid[oi][oj] = "."
            return True
        seen.add((i, j, dir))

        next_i = i + dd[dir][0]
        next_j = j + dd[dir][1]

        if not (0 <= next_i < n and 0 <= next_j < n):
            return False

        if grid[next_i][next_j] == "#":
            grid[oi][oj] = "."
            dir = (dir + 1) % 4
        else:
            i, j = next_i, next_j

ans = 0
for oi in tqdm(range(n)):
    for oj in range(n):
        loop = will_loop(oi, oj)
        ans += loop
    
    print(ans)

print(ans)
