with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

groupedNums = [[]]
i = 0

while len(lines) > 0:
    if lines[0] == '':
        i += 1
        lines.pop(0)
        groupedNums.append([])
    else:
        groupedNums[i].append(int(lines.pop(0)))

totaledNums = []
i = 0

for group in groupedNums:
    total = 0
    for num in group:
        total += num
    totaledNums.append(total)
    i += 1

totaledNums.sort()

print(totaledNums[-1] + totaledNums[-2] + totaledNums[-3])