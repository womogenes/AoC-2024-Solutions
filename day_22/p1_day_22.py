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

def get_idx(seed, idx):
    x = seed
    for _ in range(idx):
        x = next(x)
    return x

res = [get_idx(x, 2000) for x in lines]
print(res)
print(sum(res))