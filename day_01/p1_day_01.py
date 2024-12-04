with open("day_01.in") as fin:
    data = fin.read()

ans = 0
a = []
b = []

for line in data.strip().split("\n"):
    nums = [int(i) for i in line.split("   ")]
    a.append(nums[0])
    b.append(nums[1])

a.sort()
b.sort()

for i in range(len(a)):
    ans += abs(a[i] - b[i])

print(ans)
