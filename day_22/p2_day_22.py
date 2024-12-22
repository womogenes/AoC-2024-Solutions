from tqdm import tqdm

with open("./day_22.in") as fin:
    lines = list(map(int, fin.read().strip().split("\n")))

def mix(a, b):
    return a ^ b

def prune(a):
    return a % 16777216

def next(x):
    x = prune(mix(x, x * 64))
    x = prune(mix(x, x // 32))
    x = prune(mix(x, x * 2048))
    return x

def get_profit(seed):
    seq = [seed % 10]
    profit = {}
    x = seed
    for i in range(2000):
        x = next(x)
        seq.append(x % 10)

        if i >= 5:
            changes = [seq[j] - seq[j-1] for j in range(i-2, i+2)]
            if not tuple(changes) in profit:
                profit[tuple(changes)] = x % 10

    return profit

profits = [get_profit(seed) for seed in tqdm(lines)]

def get_total_profit(seq):
    ans = 0
    for profit in profits:
        if seq in profit:
            ans += profit[seq]
    return ans

seqs = set()
for profit in tqdm(profits):
    seqs = seqs.union(profit.keys())
print(len(seqs))

best = 0
for seq in tqdm(seqs):
    best = max(best, get_total_profit(seq))

print(best)
