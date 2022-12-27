with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

cycles = []
display = ''
register = 1

for line in lines:
    cycles.extend(line.split(' ')) if ' ' in line else cycles.append(line)

for i, cycle in enumerate(cycles):
    sprite_regs = [register - 1, register, register + 1]
    if i % 40 in sprite_regs:
        display += '#'
    else:
        display += '.'

    try:
        register += int(cycle)
    except:
        pass

for i in range(6):
    print(display[(i * 40):(i + 1) * 40])