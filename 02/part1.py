with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

lookup = {
    'X': {
        'points': 1,
        'A': 3,
        'B': 0,
        'C': 6,
    },
    'Y': {
        'points': 2,
        'A': 6,
        'B': 3,
        'C': 0,
    },
    'Z': {
        'points': 3,
        'A': 0,
        'B': 6,
        'C': 3,
    },
}

points = 0

for line in lines:
    points += lookup[line[-1]]['points'] + lookup[line[-1]][line[0]]

print(points)