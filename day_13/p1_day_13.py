import re

with open("./day_13.in") as fin:
    lines = fin.read().strip().split("\n\n")


def parse(x):
    lines = x.split("\n")
    a = list(map(int, re.findall(r"Button A: X\+(\d+), Y\+(\d+)", lines[0])[0]))
    b = list(map(int, re.findall(r"Button B: X\+(\d+), Y\+(\d+)", lines[1])[0]))
    p = list(map(int, re.findall(r"Prize: X=(\d+), Y=(\d+)", lines[2])[0]))
    return a, b, p


prices = []
for a, b, p in [parse(line) for line in lines]:
    def test(i, j):
        x = a[0] * i + b[0] * j
        y = a[1] * i + b[1] * j
        return (x, y) == tuple(p)

    va = 1<<30
    for i in range(100):
        for j in range(100):
            if test(i, j):
                va = min(va, 3*i + j)
    
    if va < 1<<30:
        prices.append(va)
    

spent = 0
print(sum(prices))
