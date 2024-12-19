# WARNING: only works with my specific input
# May modify in the future to work on general inputs

with open("./day_17.in") as fin:
    lines = fin.read().strip().split("\n")
    A, B, C = [int(lines[i].split(" ")[2]) for i in range(3)]
    program = list(map(int, lines[4].split(" ")[1].split(",")))

valid = {}
tree = {}
cur = 0

for cur in range(len(program)):
    # Stores set of possible 10 bits at given position
    valid[cur] = set()
    out = program[cur]

    def get_compatible(cur, bits, prev):
        for prev_bits in valid[prev]:
            overlap = 10 - (cur-prev)*3
            prefix = prev_bits >> (10-overlap)
            if prefix == bits % (1<<overlap):
                yield (prev, prev_bits)

    for bits in range(2**10):
        tree[(cur, bits)] = set()
        R = bits % 8

        # This is the section that's specific to my input
        if (R ^ (bits >> (R^6)) ^ 2) % 8 == out:
            # Vet this valid section with existing valids
            for prev in range(cur-3, cur):
                if prev < 0: continue
                tree[(cur, bits)].update(get_compatible(cur, bits, prev))
            
            if cur == 0 or len(tree[(cur, bits)]) > 0:
                valid[cur].add(bits)


# Follow the tree
possible_A = []
stack = []

for bits in valid[len(program)-1]:
    if bits >= 256:
        continue

    stack.append((0, len(program)-1, bits))

print(stack)
ans = []

while len(stack) > 0:
    A, cur, bits = stack.pop()
    A = (A<<3) ^ (bits % 8)

    if cur == 0:
        ans.append(A)

    for child in tree[(cur, bits)]:
        if child[0] != cur - 1:
            continue
        stack.append((A, *child))

print(sorted(ans)[0])
