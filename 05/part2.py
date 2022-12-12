with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

stacks = []
instructions = []

for line in lines:
    if line.startswith('move'):
        move = line.split(' ')
        moveDict = {
            'move': int(move[1]),
            'from': int(move[3]),
            'to': int(move[5]),
        }
        instructions.append(moveDict)
    elif '[' in line:
        if stacks == []:
            for _ in range((len(line) // 4) + 2):
                stacks.append([])
        for i in range(len(line)):
            char = line[i]
            if char != ' ' and char != '[' and char != ']':
                stacks[(i // 4) + 1].insert(0, char)

for step in instructions:
    for x in range(step['move']):
        stacks[step['to']].append(stacks[step['from']].pop((step['move'] * -1) + x))

answer = ''

for stack in stacks:
    if stack != []:
        answer += stack.pop()

print(answer)