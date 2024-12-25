with open("./day_25.in") as fin:
    lines = fin.read().strip().split("\n\n")

def parse(s):
    lock = s[0][0] == "#"
    
    if lock:
        vals = []
        for j in range(5):
            for i in range(7):
                if s[i][j] == ".":
                    vals.append(i)
                    break
        return vals, lock
    
    vals = []
    for j in range(5):
        for i in range(6, -1, -1):
            if s[i][j] == ".":
                vals.append(6 - i)
                break
    return vals, lock

locks = []
keys = []
for s in lines:
    vals, lock = parse(s.split("\n"))
    if lock:
        locks.append(vals)
    else:
        keys.append(vals)

ans = 0
for lock in locks:
    for key in keys:
        good = True

        for j in range(5):
            if lock[j] + key[j] > 7:
                good = False
                break
        
        ans += good

print(ans)