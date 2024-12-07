from itertools import product

with open("./day_07.in") as fin:
    lines = fin.read().strip().split("\n")

ans = 0
for i, line in enumerate(lines):
    parts = line.split()
    value = int(parts[0][:-1])
    nums = list(map(int, parts[1:]))

    def test(combo):
        ans = nums[0]
        for i in range(1, len(nums)):
            if combo[i-1] == "+":
                ans += nums[i]
            elif combo[i-1] == "|":
                ans = int(f"{ans}{nums[i]}")
            else:
                ans *= nums[i]
        return ans

    for combo in product("*+|", repeat=len(nums)-1):
        if test(combo) == value:
            print(f"[{i:02}/{len(lines)}] WORKS", combo, value)
            ans += value
            break


print(ans)
