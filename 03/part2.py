from string import ascii_letters

priority = '0' + ascii_letters

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

total = 0
i = 0

while i < len(lines):
    for char in lines[i]:
        if char in lines[i + 1] and char in lines[i + 2]:
            total += priority.index(char)
            break
    i += 3

print(total)