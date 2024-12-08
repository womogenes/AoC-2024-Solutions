import time
from colorama import init, Fore, Back
from itertools import product

init()

CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'

with open("./day_07.in") as fin:
    lines = fin.read().strip().split("\n")

ans = 0
for i, line in enumerate(lines):
    parts = line.split()
    value = int(parts[0][:-1])
    nums = list(map(int, parts[1:]))

    if len(nums) != 7:
        continue

    def test(combo, last):
        ans = nums[0]
        expr = f"{Fore.WHITE}{nums[0]}"
        for i in range(1, len(nums)):
            if combo[i-1] == "+":
                expr += f"{Fore.BLUE}{combo[i-1]}{Fore.WHITE}{nums[i]}"
                ans += nums[i]
            else:
                expr += f"{Fore.MAGENTA}{combo[i-1]}{Fore.WHITE}{nums[i]}"
                ans *= nums[i]
        
        if ans != value:
            if last:
                print(f"{CURSOR_UP_ONE + ERASE_LINE}{Fore.RED}{ans:<14}{expr}")
            else:
                print(f"{CURSOR_UP_ONE + ERASE_LINE}{Fore.WHITE}{ans:<14}{expr}")
        else:
            print(f"{CURSOR_UP_ONE + ERASE_LINE}{Fore.GREEN}{ans:<14}{expr}")
        return ans

    for i, combo in enumerate(product("*+", repeat=len(nums)-1)):
        if test(combo, i == 2**(len(nums)-1) - 1) == value:
            ans += value
            break
        
        time.sleep(0.0000001)

    time.sleep(1.0)
    print()


print(ans)
