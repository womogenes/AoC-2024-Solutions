import random
from tqdm import tqdm

with open("./day_24.in") as fin:
    lines = fin.read().strip().split("\n\n")

ins = {}

# Number of wires
N = 44

for line in lines[1].split("\n"):
    w1, op, w2, _, out = line.split(" ")
    ins[out] = (w1, w2, op)

def simulate(x, y):
    wires = {}
    for i in range(N+1):
        wires[f"x{i:02}"] = (x & (1<<i)) >> i
        wires[f"y{i:02}"] = (y & (1<<i)) >> i

    def get(wire):
        if wire in wires:
            return wires[wire]
        
        w1, w2, op = ins[wire]
        if op == "AND":
            wires[wire] = get(w1) & get(w2)
        elif op == "OR":
            wires[wire] = get(w1) | get(w2)
        elif op == "XOR":
            wires[wire] = get(w1) ^ get(w2)
        
        return wires[wire]

    z = 0
    for i in range(N+1):
        z <<= 1
        z ^= get(f"z{i:02}")
    
    return wires, z

x = 0
y = 0
for line in lines[0].split("\n")[:N]:
    x <<= 1
    x ^= int(line.split()[1])
for line in lines[0].split("\n")[N:N*2]:
    y <<= 1
    y ^= int(line.split()[1])

bad = set()
for it in range(1000):
    x = random.randrange(1<<(N+1))
    y = random.randrange(1<<(N+1))
    wires, z_out = simulate(x, y)
    z = x + y

    for i in range(N+2):
        if z & (1<<i) != z_out & (1<<i):
            wire = f"z{i:02}"
            if wire in bad:
                continue
            print(f"it={it:>3} {wire} is bad")
            bad.add(wire)

print(len(bad))
for i in range(N+2):
    if f"z{i:02}" not in bad:
        print(f"z{i:02} is good")
