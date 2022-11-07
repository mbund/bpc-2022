grid = [ [ 1, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
         [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], ]

total = 0

def count_paths(x, y, step):
    global total
    if step == 0:
        total += 1
    if step > 0:
        for (dx, dy) in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= x + dx < 9 and 0 <= y + dy < 6 and grid[y + dy][x + dx] == 0:
                grid[y + dy][x + dx] = 1
                count_paths(x + dx, y + dy, step - 1)
                grid[y + dy][x + dx] = 0


count_paths(0, 0, 20)
print(total)
