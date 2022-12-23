with open('input.txt', 'r') as f:
    grid = [[int(num) for num in line.strip('\n')] for line in f.readlines()]

def check_all():
    return check_up() * check_down() * check_left() * check_right()

def check_up():
    if y == 0:
        return 0
    cell_vis = 0
    for y_up in reversed(range(y)):
        cell_up_val = grid[y_up][x]
        cell_vis += 1
        if cell_up_val >= cell_val:
            break        
    return cell_vis

def check_down():
    if y == y_edge:
        return 0
    cell_vis = 0
    for y_down in range(y + 1, len(grid)):
        cell_down_val = grid[y_down][x]
        cell_vis += 1
        if cell_down_val >= cell_val:
            break
    return cell_vis

def check_left():
    if x == 0:
        return 0
    cell_vis = 0
    for x_left in reversed(range(x)):
        cell_left_val = grid[y][x_left]
        cell_vis += 1
        if cell_left_val >= cell_val:
            break
    return cell_vis

def check_right():
    if x == x_edge:
        return 0
    cell_vis = 0
    for x_right in range(x + 1, len(grid[y])):
        cell_right_val = grid[y][x_right]
        cell_vis += 1
        if cell_right_val >= cell_val:
            break
    return cell_vis

x_edge = len(grid[0]) - 1
y_edge = len(grid) - 1
max_vis = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        cell_val = grid[y][x]
        cell_vis = check_all()
        if cell_vis > max_vis:
            max_vis = cell_vis

print(max_vis)