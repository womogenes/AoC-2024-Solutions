with open("./day_06.in") as fin:
    grid = fin.read().strip().split("\n")

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

dir = 0
dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]

seen = set()
while True:
    seen.add((i, j))

    next_i = i + dd[dir][0]
    next_j = j + dd[dir][1]

    if not (0 <= next_i < n and 0 <= next_j < n):
        break

    if grid[next_i][next_j] == "#":
        dir = (dir + 1) % 4
    else:
        i, j = next_i, next_j

print(len(seen))