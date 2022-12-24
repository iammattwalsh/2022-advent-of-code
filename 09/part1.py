with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

g_x, g_y, g_u, g_d, g_l, g_r = 0, 0, 0, 0, 0, 0

for inst in lines:
    dir = inst[0]
    dist = int(inst[2:])
    if dir == 'U':
        g_y += dist
        if g_y > g_u:
            g_u = g_y
    elif dir == 'D':
        g_y -= dist
        if g_y < g_d:
            g_d = g_y
    elif dir == 'R':
        g_x += dist
        if g_x > g_r:
            g_r = g_x
    elif dir == 'L':
        g_x -= dist
        if g_x < g_l:
            g_l = g_x

height = abs(g_u) + abs(g_d) + 1
width = abs(g_r) + abs(g_l) + 1
pos_head = {'x': width - g_r - 1, 'y': height - g_u - 1}
pos_tail = {'x': width - g_r - 1, 'y': height - g_u - 1}
grid = [['.'] * width for row in range(height)]

for inst in lines:
    dir = inst[0]
    dist = int(inst[2:])
    for move in range(dist):
        pos_head['prev_x'], pos_head['prev_y'] = pos_head['x'], pos_head['y']
        pos_tail['prev_x'], pos_tail['prev_y'] = pos_tail['x'], pos_tail['y']
        if dir == 'U':
            pos_head['y'] -= 1
        elif dir == 'D':
            pos_head['y'] += 1
        elif dir == 'L':
            pos_head['x'] -= 1
        elif dir == 'R':
            pos_head['x'] += 1


        if abs(pos_tail['x'] - pos_head['x']) > 1 or abs(pos_tail['y'] - pos_head['y']) > 1:
            pos_tail['x'], pos_tail['y'] = pos_head['prev_x'], pos_head['prev_y']

        grid[pos_tail['y']][pos_tail['x']] = 'T'

print([cell for row in grid for cell in row].count('T'))