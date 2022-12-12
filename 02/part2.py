with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

lookup = {
    'X': {
        'points': 0,
        'A': 3,
        'B': 1,
        'C': 2,
    },
    'Y': {
        'points': 3,
        'A': 1,
        'B': 2,
        'C': 3,
    },
    'Z': {
        'points': 6,
        'A': 2,
        'B': 3,
        'C': 1,
    },
}

points = 0

for line in lines:
    points += lookup[line[-1]]['points'] + lookup[line[-1]][line[0]]

print(points)