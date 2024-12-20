from heapq import heappush, heappop

with open("./day_18.in") as fin:
    lines = fin.read().strip().split("\n")
    coords = set([tuple(map(int, line.split(","))) for line in lines][:1024])

dd = [[1, 0], [0, 1], [-1, 0], [0, -1]]

N = 70

# Heuristic for A*
def h(i, j):
    return abs(N - i) + abs(N - j)

def in_grid(i, j):
    return 0 <= i <= N and 0 <= j <= N and (i, j) not in coords

q = [(h(0, 0), 0, 0)]
cost = {}
while len(q) > 0:
    c, i, j = heappop(q)
    if (i, j) in cost:
        continue
    cost[(i, j)] = c - h(i, j)

    if (i, j) == (N, N):
        print(cost[(i, j)])
        break

    for di, dj in dd:
        ii, jj = i + di, j + dj
        if in_grid(ii, jj):
            heappush(q, (cost[(i, j)] + 1 + h(ii, jj), ii, jj))
