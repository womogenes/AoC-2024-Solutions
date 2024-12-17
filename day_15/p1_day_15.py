with open("./day_15.in") as fin:
    parts = fin.read().strip().split("\n\n")
    grid = [list(line) for line in parts[0].split("\n")]
    steps = parts[1].replace("\n", "")

n = len(grid)

dirs = {
    "<": [0, -1],
    "v": [1, 0],
    ">": [0, 1],
    "^": [-1, 0]
}

for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            ci, cj = i, j
            break


def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < n)


def move(dir):
    global ci, cj, grid

    newi, newj = ci + dir[0], cj + dir[1]
    if not in_grid(newi, newj):
        return

    # If is box, try pushing box
    di, dj = ci, cj
    while in_grid(di, dj):
        di += dir[0]
        dj += dir[1]
        if not in_grid(di, dj):
            break

        if grid[di][dj] == "#":
            break

        if grid[di][dj] == ".":
            grid[di][dj] = "O"
            grid[ci][cj] = "."
            ci, cj = ci+dir[0], cj+dir[1]
            grid[ci][cj] = "@"
            break
        


for step in steps:
    move(dirs[step])


ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "O":
            ans += (100*i + j)

print("\n".join(["".join(line) for line in grid]))

print(ans)
