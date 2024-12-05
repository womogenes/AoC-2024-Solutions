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

ans = 0

for update in updates:
    good, mid = follows_rules(update)
    if good:
        ans += mid

print(ans)
