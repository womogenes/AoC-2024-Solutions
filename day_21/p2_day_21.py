from itertools import product, combinations
from tqdm import tqdm
from functools import lru_cache

with open("./day_21.in") as fin:
    lines = fin.read().strip().split("\n")

numeric_keypad = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}
direction_keypad = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

dd = {
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
    "^": (-1, 0)
}


def get_combos(ca, a, cb, b):
    # char a, char b, int a, int b
    for idxs in combinations(range(a + b), r=a):
        res = [cb] * (a + b)
        for i in idxs:
            res[i] = ca
        yield "".join(res)


@lru_cache(None)
def generate_ways(a, b, keypad):
    keypad = direction_keypad if keypad else numeric_keypad

    cur_loc = keypad[a]
    next_loc = keypad[b]
    di = next_loc[0] - cur_loc[0]
    dj = next_loc[1] - cur_loc[1]

    moves = []
    if di > 0:
        moves += ["v", di]
    else:
        moves += ["^", -di]
    if dj > 0:
        moves += [">", dj]
    else:
        moves += ["<", -dj]
    
    raw_combos = list(set(["".join(x) + "A" for x in get_combos(*moves)]))
    combos = []
    for combo in raw_combos:
        ci, cj = cur_loc
        good = True
        for c in combo[:-1]:
            di, dj = dd[c]
            ci, cj = ci + di, cj + dj
            if not (ci, cj) in keypad.values():
                good = False
                break
        if good:
            combos.append(combo)

    return combos

@lru_cache(None)
def get_cost(a, b, keypad, depth=0):
    # Cost of going from a to b on given keypad and recursion depth
    if depth == 0:
        assert keypad
        return min([len(x) for x in generate_ways(a, b, True)])

    ways = generate_ways(a, b, keypad)
    print(ways)
    best_cost = 1<<60
    for seq in ways:
        seq = "A" + seq
        cost = 0
        for i in range(len(seq)-1):
            a, b = seq[i], seq[i+1]
            cost += get_cost(a, b, True, depth-1)
        
        best_cost = min(best_cost, cost)
    
    return best_cost


def get_code_cost(code, depth):
    code = "A" + code
    cost = 0
    for i in range(len(code)-1):
        a, b = code[i], code[i+1]
        cost += get_cost(a, b, False, depth)
    return cost


ans = 0
for line in lines:
    ans += get_code_cost(line, 25) * int(line[:-1])

print(ans)
