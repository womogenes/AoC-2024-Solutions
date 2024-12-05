from collections import defaultdict

with open("./day_05.in") as fin:
    raw_rules, updates = fin.read().strip().split("\n\n")
    rules = []
    for line in raw_rules.split("\n"):
        a, b = line.split("|")
        rules.append((int(a), int(b)))
    updates = [list(map(int, line.split(","))) for line in updates.split("\n")]


def follows_rules(update):
    idx = {}
    for i, num in enumerate(update):
        idx[num] = i
    
    for a, b in rules:
        if a in idx and b in idx and not idx[a] < idx[b]:
            return False, 0
        
    return True, update[len(update) // 2]


# Topological sort, I guess
def sort_correctly(update):
    my_rules = []
    for a, b in rules:
        if not (a in update and b in update):
            continue
        my_rules.append((a, b))

    indeg = defaultdict(int)
    for a, b in my_rules:
        indeg[b] += 1
    
    ans = []
    while len(ans) < len(update):
        for x in update:
            if x in ans:
                continue
            if indeg[x] <= 0:
                ans.append(x)
                for a, b in my_rules:
                    if a == x:
                        indeg[b] -= 1
    
    return ans


ans = 0

for update in updates:
    if follows_rules(update)[0]:
        continue

    seq = sort_correctly(update)
    ans += seq[len(seq) // 2]

print(ans)
