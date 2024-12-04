import re

with open("./day_03.in") as fin:
    line = fin.read().strip()

matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line)

enabled = True

ans = 0
for match in matches:
    if match[2] == "" and enabled:
        ans += int(match[0]) * int(match[1])
    else:
        if match[2] == "do()":
            enabled = True
        else:
            enabled = False

print(ans)
