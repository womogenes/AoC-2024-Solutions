from collections import defaultdict

with open("day_01.in") as fin:
    data = fin.read()

ans = 0
a = []
b = []

for line in data.strip().split("\n"):
    nums = [int(i) for i in line.split("   ")]
    a.append(nums[0])
    b.append(nums[1])

counts = defaultdict(int)
for x in b:
    counts[x] += 1

for x in a:
    ans += x * counts[x]

print(ans)
