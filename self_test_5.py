"""PRACTICE THIS"""


def num_rushes(slope_height, rush_height_gain, back_sliding):
    """num""" 
    rushes = 0
    current_height = 0

    while current_height < slope_height:
        current_height = max(current_height - back_sliding, 0)
        rushes += 1
        current_height += rush_height_gain
    return rushes


def reverseron(strings):
    """reverse"""
    reversed_list = []
    for item in strings:
        reversed_list.append(item[::-1].capitalize())
    strings.clear()
    strings += reversed_list


def print_odd_cubes_to_number(number):
    """prints"""
    if number < 1:
        print('ERROR: number must be at least 1')
    else:
        for num in range(1, number+1):
            if (num + 1) % 2 == 0:
                print(f'{num} * {num} * {num} = {num**3}')


def column_sums(square):
    """sums"""
    col_list = [0]*len(square[0])
    for row in square:
        for num, cell in enumerate(row):
            col_list[num] += cell
    return col_list


def print_hundred(nums):
    """prints hundred"""
    asum = 0
    ind = 0
    while asum <= 100 and ind < len(nums):
        print(nums[ind])
        asum += nums[ind]
        ind += 1


def my_enumerate(items):
    """enums"""
    ind = 0
    ret_list = []
    while ind < len(items):
        ret_list.append((ind, items[ind]))
        ind += 1
    return ret_list

ans = my_enumerate([10, 20, 30])
print(ans)