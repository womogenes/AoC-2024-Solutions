import json

with open("./day_24.in") as fin:
    raw_in = fin.read().strip()
    lines = raw_in.split("\n\n")

ins = {}

# Number of wires
N = 44

for line in lines[-1].split("\n"):
    w1, op, w2, _, out = line.split()
    w1, w2 = sorted([w1, w2])
    ins[out] = (w1, w2, op)

# Make a new file called names.json with empty "{}"
with open("./names.json") as fin:
    name = json.load(fin)

for wire in ins:
    w1, w2, op = ins[wire]
    if w1[0] == "x" and w2[0] == "y":
        ix = int(w1[1:])
        iy = int(w2[1:])
        assert ix == iy

        if wire[0] == "z":
            print(f"uh oh, {w1} {op} {w2} -> {wire}")
        
        if op == "AND":
            if ix > 0:
                name[wire] = f"icarry2_{ix:02}"
            else:
                name[wire] = f"carry_{ix+1:02}"
        elif op == "XOR":
            name[wire] = f"out_{ix:02}"
    
    if w1.startswith("carry_") and w2.startswith("out_"):
        i1 = int(w1[-2:])
        i2 = int(w2[-2:])
        assert i2 == i1, ("bad carry and", wire, ins[wire])

        if op == "AND":
            name[wire] = f"icarry1_{i2:02}"
        elif op == "XOR":
            assert wire == f"z{i2:02}", (f"bad z out! {wire} should be z{i2:02}", wire, ins[wire])
    
    if w1.startswith("icarry1_") and w2.startswith("icarry2_"):
        i1 = int(w1[-2:])
        i2 = int(w2[-2:])
        assert i2 == i1, ("bad icarry or", wire, ins[wire])
        assert op == "OR"

        print(wire)
        name[wire] = f"carry_{i1+1:02}"


# NOTES:
# kwb should be z12
# qkf should be z16
# tgr should be z24
# cph should be jqn

print(",".join(sorted(["kwb", "qkf", "tgr", "cph", "z12", "z16", "z24", "jqn"])))


with open("./names.json", "w") as fout:
    json.dump(name, fout, indent=2)

def get_name(wire):
    return name[wire] if wire in name else wire

with open("./day_24.in", "w") as fout:
    fout.write(lines[0] + "\n")

    for og, renamed in sorted(name.items(), key=lambda x: x[1]):
        if not og in ins:
            continue
        w1, w2, op = ins[og]
        fout.write(f"{get_name(w1):<12} {op:<3} {get_name(w2):<12} -> {renamed}\n")

    fout.write("\n")

    for wire in ins:
        if not wire in name:
            w1, w2, op = ins[wire]
            fout.write(f"{get_name(w1):<12} {op:<3} {get_name(w2):<12} -> {wire}\n")
