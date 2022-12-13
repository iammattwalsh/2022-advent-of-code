with open('input.txt', 'r') as f:
    msg = ''.join(f.readlines())

for i in range(len(msg) - 14):
    counter = 0
    code = msg[i : i + 14]
    for char in code:
        if code.count(char) == 1:
            counter += 1
        else:
            break
    if counter == 14:
        print(i + 14)
        break