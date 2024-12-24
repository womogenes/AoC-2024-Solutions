with open("./day_24.in") as fin:
    lines = fin.read().strip().split("\n\n")

wires = {}

for line in lines[0].split("\n"):
    wire, value = line.split(": ")
    value = int(value)
    wires[wire] = value

print(wires)

while True:
    good = True
    for line in lines[1].split("\n"):
        w1, op, w2, _, out = line.split(" ")
        if not (w1 in wires and w2 in wires):
            good = False
            continue
        
        if op == "AND":
            wires[out] = wires[w1] & wires[w2]
        elif op == "OR":
            wires[out] = wires[w1] | wires[w2]
        elif op == "XOR":
            wires[out] = wires[w1] ^ wires[w2]

    if good:
        break

values = sorted([(k, v) for k, v in wires.items() if k.startswith("z")])
print(values)
print(int("".join([str(x[1]) for x in values][::-1]), 2))
