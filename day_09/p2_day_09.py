from tqdm import tqdm

with open("./day_09.in") as fin:
    line = fin.read().strip()

# Allocate a lot of space
size = [0] * len(line)
loc = [0] * len(line)

def make_filesystem(diskmap):
    global loc, size

    blocks = []

    is_file = True
    id = 0
    for x in diskmap:
        x = int(x)
        if is_file:
            loc[id] = len(blocks)
            size[id] = x
            blocks += [id] * x
            id += 1
            is_file = False
        else:
            blocks += [None] * x
            is_file = True
    
    return blocks

filesystem = make_filesystem(line)

def move(arr):
    # Current file to move
    big = 0
    while size[big] > 0:
        big += 1
    big -= 1

    for to_move in tqdm(range(big, -1, -1)):
        # Find first free space that works
        free_space = 0
        first_free = 0
        while first_free < loc[to_move] and free_space < size[to_move]:
            first_free = first_free + free_space
            free_space = 0
            while arr[first_free] != None:
                first_free += 1
            while first_free + free_space < len(arr) and arr[first_free + free_space] == None:
                free_space += 1
        
        if first_free >= loc[to_move]:
            continue
        
        # Move file by swapping block values
        for idx in range(first_free, first_free + size[to_move]):
            arr[idx] = to_move
        for idx in range(loc[to_move], loc[to_move] + size[to_move]):
            arr[idx] = None
        
    return arr

def checksum(arr):
    ans = 0
    for i, x in enumerate(arr):
        if x != None:
            ans += i * x
    return ans

moved = move(filesystem)

print(checksum(moved))
