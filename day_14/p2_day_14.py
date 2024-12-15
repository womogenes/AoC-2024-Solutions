with open("./day_14.in") as fin:
    lines = fin.read().strip().split("\n")


n = 103
m = 101

# n = 7
# m = 11


p = []
v = []

for line in lines:
    a, b = line.split(" ")
    p.append(list(map(int, a.split("=")[1].split(","))))
    v.append(tuple(map(int, b.split("=")[1].split(","))))

    p[-1] = [p[-1][1], p[-1][0]]
    v[-1] = [v[-1][1], v[-1][0]]

N = len(p)

def update():
    global p, v
    for i in range(N):
        p[i][0] = (p[i][0] + v[i][0] + n) % n
        p[i][1] = (p[i][1] + v[i][1] + m) % m


def count_robots(i0, i1, j0, j1):
    ans = 0
    for i in range(i0, i1):
        for j in range(j0, j1):
            for ii, jj in p:
                if i == ii and j == jj:
                    ans += 1
    return ans


seen = {}
step = 0
while True:
    picture = [["  "] * (m) for _ in range(n)]
    for i, j in p:
        picture[i][j] = "##"

    picture = "\n".join(["".join(line) for line in picture])
    if picture in seen:
        print(f"Saw this picture at step {seen[picture]}, stopping...")
        break
    seen[picture] = step

    print(picture)
    print("\n" * 2)
    
    update()

    step += 1
