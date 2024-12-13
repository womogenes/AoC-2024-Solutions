with open("./day_12.in") as fin:
    grid = fin.read().strip().split("\n")

n = len(grid)

dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < n)

seen = set()
plots = []

for i in range(n):
    for j in range(n):
        if (i, j) in seen:
            continue

        stack = [(i, j)]
        plots.append([grid[i][j], []])

        print(f"looking at i={i}, j={j}, grid[i][j]={grid[i][j]}")

        while len(stack) > 0:
            ci, cj = stack.pop()
            if (ci, cj) in seen:
                continue
            if not in_grid(ci, cj):
                continue
            if grid[ci][cj] != grid[i][j]:
                continue
            seen.add((ci, cj))

            plots[-1][1].append((ci, cj))
            for di, dj in dd:
                ii, jj = ci + di, cj + dj
                stack.append((ii, jj))

def count_free(i, j, plot):
    ans = 0
    for di, dj in dd:
        ii, jj = i + di, j + dj
        if not in_grid(ii, jj):
            ans += 1
        elif grid[ii][jj] != grid[i][j]:
            ans += 1
    return ans

def perim(plot):
    ans = 0
    for i, j in plot:
        ans += count_free(i, j, plot)
    return ans

ans = 0
for c, plot in plots:
    print(c, plot, perim(plot))
    ans += perim(plot) * len(plot)

print(ans)
