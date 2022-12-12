with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]
splitLines = []

for line in lines:
    newLine = []
    splitLine = line.split(',')
    for split in splitLine:
        newLine.append(split.split('-'))
    splitLines.append(newLine)

for i in range(len(splitLines)):
    for j in range(len(splitLines[i])):
        for k in range(len(splitLines[i][j])):
            splitLines[i][j][k] = int(splitLines[i][j][k])

total = 0

for line in splitLines:
    stop = False
    for i in range(2):
        for j in range(2):
            if line[i][0] <= line[1 - i][j] <= line[i][1]:
                total += 1
                stop = True
                break
        if (stop):
            break

print(total)