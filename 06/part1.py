with open('input.txt', 'r') as f:
    msg = ''.join(f.readlines())

for i in range(len(msg) - 4):
    counter = 0
    code = msg[i : i + 4]
    for char in code:
        if code.count(char) == 1:
            counter += 1
        else:
            break
    if counter == 4:
        print(i + 4)
        break



# msg = [line.strip('\n') for line in msg]

# print(msg)

# print(msg[0:4])