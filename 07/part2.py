with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

current_dir_list = []
dir_sizes = {}
total_file_size = 0

def add_sizes(keys, size):
    for key in keys:
        dir_sizes[key] += size

def full_path():
    file_path = ''
    for dir in current_dir_list:
        file_path += dir + ('/' if len(file_path) > 0 else '')
    return file_path

def full_path_for_each():
    full_dir_list = []
    for i in range(len(current_dir_list)):
        current_dir = ''
        j = 0
        while j <= i:
            current_dir += current_dir_list[j] + ('/' if len(current_dir) > 0 else '')
            j += 1
        full_dir_list.append(current_dir)
        i += 1
    return full_dir_list

for line in lines:
    split_line = line.split()
    # if command
    if split_line[0] == '$':
        if split_line[1] == 'cd' and split_line[2] == '..':
            current_dir_list.pop()
        elif split_line[1] == 'cd':
            current_dir_list.append(split_line[2])
            file_path = full_path()
            if file_path not in dir_sizes:
                dir_sizes[file_path] = 0
    # if file
    elif split_line[0] != 'dir':
        add_sizes(full_path_for_each(), int(split_line[0]))
        total_file_size += int(split_line[0])

total_disk_size = 70000000
size_needed = 40000000
size_to_clear = total_file_size - size_needed
best_candidate_size = total_disk_size - total_file_size

for dir in dir_sizes:
    dir_size = dir_sizes[dir]
    if dir_size >= size_to_clear and dir_size < best_candidate_size:
        best_candidate_size = dir_size

print(best_candidate_size)