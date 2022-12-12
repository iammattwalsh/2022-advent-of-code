from string import ascii_letters

priority = '0' + ascii_letters

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

total = 0

for line in lines:
    for char in line[0 : len(line) // 2]:
        if char in line[len(line) // 2 :]:
            print(char)
            total += priority.index(char)
            break

print(total)