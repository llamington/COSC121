"""
17
"atoot", "tootle"
[7, 12, -4, 7]
['bat', 'wom', 'wom', 'bat', 'bat']
[10, 10, 10, 10]
[-10, -10, -10, -10]
['xero', 'yero', 'yactl', 'y']
open(filename, 'w')
"""


def bad_fuse(list_1, list_2):
    """concat"""
    return list_1[:-1] + list_2[1:]


def should_shutdown(battery_level, time_on):
    """shuts down"""
    if battery_level < 4.7 and time_on < 60:
        return True
    elif time_on >= 60 and battery_level < 4.8:
        return True
    else:
        return False


def print_slice(size):
    """prints slice"""
    for i in range(size, 0, -1):
        print('*' * i)


def num_doublings(initial_population, final_population):
    """calculates num double"""
    days = 0
    i = initial_population
    while i < final_population:
        i *= 2
        days += 1
    return days


def sum_numbers_in_file(filename):
    """sums nums in file"""
    asum = 0
    with open(filename) as file:
        lines = file.readlines()
        for i in lines:
            asum += int(i)
    return asum


def max_num_in_file(filename):
    """finds max num"""
    with open(filename) as file:
        lines = file.readlines()
        int_list = [int(i) for i in lines]
    return max(int_list)


def print_numbered_lines(filename):
    """prints num"""
    with open(filename) as file:
        lines = file.readlines()
        for num, i in enumerate(lines, start=1):
            print(f'{num}: {i.rstrip()}')


def print_reversed(filename):
    """prints reversed"""
    with open(filename) as file:
        lines = file.readlines()
        for i in range(len(lines) - 1, -1, -1):
            print(lines[i].rstrip())


def print_daily_totals(filename):
    """prints daily totals"""
    with open(filename) as file:
        lines = file.readlines()
        for i in lines:
            split_string = i.split(sep=',')
            inted = [float(j) for j in split_string[1:]]
            print(f'{split_string[0]} = {sum(inted):.2f}')


def file_size(filename):
    """returns file size"""
    with open(filename) as file:
        file_string = file.read()
        return len(file_string)


def generate_daily_totals(input_filename, output_filename):
    """prints daily totals"""
    with open(input_filename) as input_file, open(output_filename, 'w') as output_file:
        lines = input_file.readlines()
        for i in lines:
            split_string = i.split(sep=',')
            inted = [float(j) for j in split_string[1:]]
            output_file.write(f'{split_string[0]} = {sum(inted):.2f}\n')


def write_reversed_file(input_filename, output_filename):
    """writes reversed file"""
    with open(input_filename) as input_file, open(output_filename, 'w') as output_file:
        lines = input_file.readlines()
        lines.reverse()
        for i in lines:
            output_file.write(i)
