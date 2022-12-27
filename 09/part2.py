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
pos_head = {'x': width - g_r - 1, 'y': height + g_d - 1}
pos_tail = [{'x': width - g_r - 1, 'y': height + g_d - 1} for _ in range(9)]
grid = [['.'] * width for row in range(height)]
grid_tail = [['.'] * width for row in range(height)]

for inst in lines:
    dir = inst[0]
    dist = int(inst[2:])
    for move in range(dist):
        pos_head['prev_x'], pos_head['prev_y'] = pos_head['x'], pos_head['y']
        for knot in pos_tail:
            knot['prev_x'], knot['prev_y'] = knot['x'], knot['y']
        if dir == 'U':
            pos_head['y'] -= 1
        elif dir == 'D':
            pos_head['y'] += 1
        elif dir == 'L':
            pos_head['x'] -= 1
        elif dir == 'R':
            pos_head['x'] += 1

        prev_knot = {'x': pos_head['x'], 'y': pos_head['y'], 'prev_x': pos_head['prev_x'], 'prev_y': pos_head['prev_y']}
        for i, knot in enumerate(pos_tail):
            if abs(knot['x'] - prev_knot['x']) > 1 or abs(knot['y'] - prev_knot['y']) > 1:
                if knot['x'] == prev_knot['x'] or knot['y'] == prev_knot['y']:
                    if knot['x'] == prev_knot['x']:
                        knot['x'], knot['y'] = prev_knot['x'], prev_knot['prev_y']
                    elif knot['y'] == prev_knot['y']:
                        knot['x'], knot['y'] = prev_knot['prev_x'], prev_knot['y']
                else:
                    if prev_knot['x'] > knot['x']:
                        knot['x'] += 1
                    elif prev_knot['x'] < knot['x']:
                        knot['x'] -= 1
                    if prev_knot['y'] > knot['y']:
                        knot['y'] += 1
                    elif prev_knot['y'] < knot['y']:
                        knot['y'] -= 1
            
            prev_knot = {'x': knot['x'], 'y': knot['y'], 'prev_x': knot['prev_x'], 'prev_y': knot['prev_y']}

            if grid[pos_head['prev_y']][pos_head['prev_x']] == 'H':
                grid[pos_head['prev_y']][pos_head['prev_x']] = '.'
            grid[pos_head['y']][pos_head['x']] = 'H'
            if grid[pos_tail[i]['prev_y']][pos_tail[i]['prev_x']] == (str(i + 1)):
                grid[pos_tail[i]['prev_y']][pos_tail[i]['prev_x']] = '.'
            if grid[pos_tail[i]['y']][pos_tail[i]['x']] == '.':
                grid[pos_tail[i]['y']][pos_tail[i]['x']] = str(i + 1)

        grid_tail[pos_tail[-1]['y']][pos_tail[-1]['x']] = 'T'

print([cell for row in grid_tail for cell in row].count('T'))