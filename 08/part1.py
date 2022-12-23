with open('input.txt', 'r') as f:
    grid = [[int(num) for num in line.strip('\n')] for line in f.readlines()]

def check_up():
    if y == 0:
        return True
    for y_up in range(y):
        cell_up_val = grid[y_up][x]
        if cell_up_val >= cell_val:
            return False
    return True
        

def check_down():
    if y == y_edge:
        return True
    for y_down in range(y + 1, len(grid)):
        cell_down_val = grid[y_down][x]
        if cell_down_val >= cell_val:
            return False
    return True

def check_left():
    if x == 0:
        return True
    for x_left in range(x):
        cell_left_val = grid[y][x_left]
        if cell_left_val >= cell_val:
            return False
    return True

def check_right():
    if x == x_edge:
        return True
    for x_right in range(x + 1, len(grid[y])):
        cell_right_val = grid[y][x_right]
        if cell_right_val >= cell_val:
            return False
    return True

x_edge = len(grid[0]) - 1
y_edge = len(grid) - 1
num_vis = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        cell_val = grid[y][x]
        if check_up() or check_down() or check_left() or check_right():
            num_vis += 1

print(num_vis)