# Generate a new day with all files and stuff
import os

import datetime as dt
day = (dt.datetime.now() + dt.timedelta(hours=4, minutes=30)).day
year = dt.datetime.now().year

prefix = f"day_{str(day).zfill(2)}"

if not prefix in os.listdir():
    os.mkdir(prefix)
    os.chdir(prefix)
    with open(f"./p1_{prefix}.py", "w") as fout:
        fout.write(rf"""with open("./{prefix}.in") as fin:
    lines = fin.read().strip().split("\n")
""")

    open(f"./p2_{prefix}.py", "w")

    open(f"./{prefix}.in", "w")
