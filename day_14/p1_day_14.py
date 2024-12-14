with open("./day_14.in") as fin:
    lines = fin.read().strip().split("\n")


n = 103
m = 101


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


for _ in range(100):
    # for i in range(n):
    #     for j in range(m):
    #         x = count_robots(i, i+1, j, j+1)
    #         if x > 0:
    #             print(x, end="")
    #         else:
    #             print(".", end="")
    #     print()

    # print()
    
    update()

q0 = count_robots(0, n//2, 0, m//2)
q1 = count_robots(n//2+1, n, 0, m//2)
q2 = count_robots(0, n//2, m//2+1, m)
q3 = count_robots(n//2+1, n, m//2+1, m)

print(q0, q1, q2, q3)
print(q0 * q1 * q2 * q3)
