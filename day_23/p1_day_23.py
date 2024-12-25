from collections import defaultdict

with open("./day_23.in") as fin:
    lines = fin.read().strip().split("\n")

adj = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    adj[a].append(b)
    adj[b].append(a)

triangles = set()
for a in dict(adj):
    for i in adj[a]:
        for j in adj[a]:
            if j in adj[i]:
                triangles.add(tuple(sorted([a, i, j])))
    
ans = 0
for a, b, c in triangles:
    if "t" in [a[0], b[0], c[0]]:
        ans += 1

print(ans)
