from collections import defaultdict
import sys

sys.setrecursionlimit(2**30)

with open("./day_11.in") as fin:
    raw_nums = list(map(int, fin.read().strip().split()))

nums = defaultdict(int)
for x in raw_nums:
    nums[x] += 1


def blink(nums: dict):
    new_nums = defaultdict(int)
    for x in nums:
        l = len(str(x))
        if x == 0:
            new_nums[1] += nums[0]
        elif l % 2 == 0:
            new_nums[int(str(x)[:l//2])] += nums[x]
            new_nums[int(str(x)[l//2:])] += nums[x]
        else:
            new_nums[x * 2024] += nums[x]
    
    return new_nums


for i in range(75):
    nums = blink(nums)

ans = 0
for x in nums:
    ans += nums[x]
print(ans)
