from tqdm import tqdm

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

boxes = []
walls = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == "@":
            ci, cj = i, j*2
        elif grid[i][j] == "O":
            boxes.append([i, j*2])
        elif grid[i][j] == "#":
            walls.append([i, j*2])
            walls.append([i, j*2+1])


def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < 2*n)


def move(dir):
    global ci, cj, grid

    newi, newj = ci + dir[0], cj + dir[1]
    if not in_grid(newi, newj):
        return

    if [newi, newj] in walls:
        return
    
    stack = []
    if [newi, newj] in boxes:
        stack.append([newi, newj])
    if [newi, newj-1] in boxes:
        stack.append([newi, newj-1])
    
    # Determine dependencies
    can_move = True

    seen = set()
    while len(stack) > 0:
        topi, topj = stack.pop()
        ni, nj = topi + dir[0], topj + dir[1]
        if not in_grid(ni, nj):
            can_move = False
            break

        if [ni, nj] in walls or [ni, nj+1] in walls:
            can_move = False
            break

        if (topi, topj) in seen:
            continue
        seen.add((topi, topj))

        if [ni, nj] in boxes:
            stack.append([ni, nj])
        if [ni, nj-1] in boxes:
            stack.append([ni, nj-1])
        if [ni, nj+1] in boxes:
            stack.append([ni, nj+1])
    
    if not can_move:
        return
    
    # Can move, hooray!
    for i, box in enumerate(boxes):
        if tuple(box) in seen:
            boxes[i][0] += dir[0]
            boxes[i][1] += dir[1]
    
    ci += dir[0]
    cj += dir[1]


def print_grid(boxes, walls, ci, cj):
    for i in range(n):
        for j in range(n*2):
            if [i, j] in walls:
                print("#", end="")
            elif [i, j] in boxes:
                print("[", end="")
            elif [i, j-1] in boxes:
                print("]", end="")
            elif (i, j) == (ci, cj):
                print("@", end="")
            else:
                print(".", end="")
        print()



for step in tqdm(steps):
    move(dirs[step])

ans = 0
for i, j in boxes:
    ans += i*100 + j

print(ans)
