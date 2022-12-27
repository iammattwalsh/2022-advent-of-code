with open('input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]

cycles = ['_']
cycle_vals = [1]

for line in lines:
    cycles.extend(line.split(' ')) if ' ' in line else cycles.append(line)

for cycle in cycles:
    cycle_val = cycle_vals[-1]
    try:
        cycle_val += int(cycle)
    except:
        pass
    cycle_vals.append(cycle_val)

sig_str_cycles = [20, 60, 100, 140, 180, 220]
sig_str_tot = 0

for cycle in sig_str_cycles:
    sig_str_tot += cycle_vals[cycle] * cycle

print(sig_str_tot)