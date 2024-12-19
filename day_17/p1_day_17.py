with open("./day_17.in") as fin:
    lines = fin.read().strip().split("\n")
    A, B, C = [int(lines[i].split(" ")[2]) for i in range(3)]
    program = list(map(int, lines[4].split(" ")[1].split(",")))


def run(program, A, B, C):
    ptr = 0

    def combo():
        x = program[ptr+1]
        if x <= 3:
            return x
        if x == 4:
            return A
        if x == 5:
            return B
        if x == 6:
            return C
    
    def lit():
        return program[ptr+1]

    while True:
        if ptr >= len(program):
            return
        
        opcode = program[ptr]
        
        # print(f"ptr: {ptr} ({A}, {B}, {C}), opcode: {opcode}, lit: {lit()}, combo: {combo()}")

        if opcode == 0:
            res = A // pow(2, combo())
            A = res
        elif opcode == 1:
            res = B ^ lit()
            B = res
        elif opcode == 2:
            res = combo() % 8
            B = res
        elif opcode == 3:
            if A != 0:
                ptr = lit()
            else:
                ptr += 2
        elif opcode == 4:
            res = B ^ C
            B = res
        elif opcode == 5:
            res = combo() % 8
            yield res
        elif opcode == 6:
            res = A // pow(2, combo())
            B = res
        elif opcode == 7:            
            res = A // pow(2, combo())
            C = res

        if opcode != 3:
            ptr += 2


ans = run(program, A, B, C)
print(",".join(map(str, ans)))
