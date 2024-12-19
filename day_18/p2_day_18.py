from heapq import heappush, heappop

with open("./day_18.in") as fin:
    lines = fin.read().strip().split("\n")
    coords = [tuple(map(int, line.split(","))) for line in lines]

dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

N = 70

# Heuristic for A*
def h(i, j):
    return abs(N - i) + abs(N - j)

def doable(idx):
    # Can we get to the index with first `idx` coords blocked?
    def in_grid(i, j):
        return 0 <= i <= N and 0 <= j <= N and (i, j) not in coords[:idx]
        
    q = [(h(0, 0), 0, 0)]
    cost = {}
    while len(q) > 0:
        c, i, j = heappop(q)
        if (i, j) in cost:
            continue
        cost[(i, j)] = c - h(i, j)

        if (i, j) == (N, N):
            return True

        for di, dj in dd:
            ii, jj = i + di, j + dj
            if in_grid(ii, jj):
                heappush(q, (cost[(i, j)] + 1 + h(ii, jj), ii, jj))
    
    return False

# Binary search for first coord that is not doable
lo = 0
hi = len(coords) - 1
while hi > lo:
    mid = (lo + hi) // 2
    if doable(mid):
        lo = mid + 1
    else:
        hi = mid

print(",".join(map(str, coords[lo-1])))
