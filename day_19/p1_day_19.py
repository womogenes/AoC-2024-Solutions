with open("./day_19.in") as fin:
    lines = fin.read().strip().split("\n")
    units = lines[0].split(", ")

    designs = lines[2:]


def possible(design):
    n = len(design)
    dp = [False] * len(design)
    for i in range(n):
        if design[:i+1] in units:
            dp[i] = True
            continue

        for u in units:            
            if design[i-len(u)+1:i+1] == u and dp[i - len(u)]:
                # print("  ", i, u, design[-len(u):], dp[i - len(u)])
                dp[i] = True
                break

    # print(design, dp)
    return dp[-1]

ans = 0
for d in designs:
    if possible(d):
        print(d)
        ans += 1

print(ans)
