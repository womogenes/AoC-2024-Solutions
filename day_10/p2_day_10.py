from functools import lru_cache

with open("./day_10.in") as fin:
    grid = fin.read().strip().split("\n")


n = len(grid)


dd = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def in_grid(i, j):
    return (0 <= i < n) and (0 <= j < n)

@lru_cache(None)
def rating(i, j):
    if grid[i][j] == "9":
        return 1
    
    ans = 0
    for di, dj in dd:
        ii, jj = i + di, j + dj
        if not in_grid(ii, jj):
            continue

        if int(grid[ii][jj]) == int(grid[i][j]) + 1:
            ans += rating(ii, jj)
    
    return ans


ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == "0":
            ans += rating(i, j)

print(ans)
