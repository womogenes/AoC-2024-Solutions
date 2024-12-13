from tqdm import tqdm
import matplotlib.pyplot as plt

with open("./day_11.in") as fin:
    nums = list(map(int, fin.read().strip().split()))

def blink(arr):
    res = []
    for x in arr:
        if x == 0:
            res.append(1)
        elif len(str(x)) % 2 == 0:
            l = len(str(x))
            res += [int(str(x)[:l//2]), int(str(x)[l//2:])]
        else:
            res += [x * 2024]
    
    return res


plot = []
for i in tqdm(range(25)):
    nums = blink(nums)
    plot.append(len(nums))

plt.plot(plot)
plt.show()

print(len(nums))
