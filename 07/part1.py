from copy import deepcopy

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [line.strip('\n') for line in lines]

struct = {'/': {}}
current_dir_list = []
dir_sizes = {}
answer = 0

def find_location(location, keys):
    for key in keys:
        location = location[key]
    return location

def add_sizes(keys, size):
    for key in keys:
        # key = full_path()
        dir_sizes[key] += size

def full_path():
    file_path = ''
    for dir in current_dir_list:
        file_path += dir
    return file_path

for line in lines:
    split_line = line.split()

    current_dir = find_location(struct, current_dir_list)

    # if command
    if split_line[0] == '$':
        if split_line[1] == 'cd' and split_line[2] == '..':
            current_dir_list.pop()
        elif split_line[1] == 'cd':
            current_dir_list.append(split_line[2])
            file_path = full_path()
            if file_path not in dir_sizes:
                # print(file_path)
                dir_sizes[file_path] = 0
    # if dir
    elif split_line[0] == 'dir':
        if split_line[1] not in current_dir:
            current_dir[split_line[1]] = {}
    # if file
    else:
        current_dir[split_line[1]] = split_line[0]
        add_sizes(current_dir_list, int(split_line[0]))

for dir in dir_sizes:
    # if dir_sizes[dir] <= 100000 and dir_sizes[dir] > answer:
    #     answer = dir_sizes[dir]
    if dir_sizes[dir] <= 100000:
        answer += dir_sizes[dir]
        # print(dir, ': ', dir_sizes[dir])
    # print(dir_sizes[dir])

# print(dir_sizes)
# print(struct)

import pprint

pprint.pformat(struct)
pprint.pprint(struct)

print(answer)