from collections import defaultdict
from itertools import product
from tqdm import tqdm

with open("./day_23.in") as fin:
    lines = fin.read().strip().split("\n")

adj = defaultdict(list)
for line in lines:
    a, b = line.split("-")
    adj[a].append(b)
    adj[b].append(a)

def is_clique(nodes):
    n = len(nodes)
    for i in range(n):
        for j in range(i+1, n):
            if not nodes[i] in adj[nodes[j]]:
                return False
    return True


big_clique = []

for node in tqdm(adj):
    nbrs = adj[node]
    for mask in product((False, True), repeat=len(nbrs)):
        nodes = [node]
        for i, x in enumerate(mask):
            if x:
                nodes.append(nbrs[i])

        if is_clique(nodes):
            if len(nodes) > len(big_clique):
                big_clique = nodes

print(len(big_clique))
print(",".join(sorted(big_clique)))
