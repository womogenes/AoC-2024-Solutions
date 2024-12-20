with open("./day_19.in") as fin:
    lines = fin.read().strip().split("\n")
    units = lines[0].split(", ")

    designs = lines[2:]


def possible(design):
    n = len(design)
    dp = [0] * len(design)
    for i in range(n):
        if design[:i+1] in units:
            dp[i] = 1

        for u in units:            
            if design[i-len(u)+1:i+1] == u:
                # print("  ", i, u, dp[i - len(u)])
                dp[i] += dp[i - len(u)]

    # print(design, dp)
    return dp[-1]

ans = 0
for d in designs:
    ans += possible(d)

print(ans)
