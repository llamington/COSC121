def warmup():
    """warms up"""
    print("It's great!")

def quadratic(num):
    """return"""
    return (num+1)**2


def date_string(day_num, month_name, year_num):
    """ Turn the date into a string of the form
            day month, year
    """
    return f'{day_num} {month_name}, {year_num}'


def silly_too(x):
    """returns"""
    if x < 0:
        return x**2
    else:
        return x


def caught_speeding(speed, is_birthday):
    """returns"""
    if is_birthday:
        if speed <= 65:
            return 0
        elif 66 <= speed <= 85:
            return 1
        else:
            return 2
    else:
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        else:
            return 2


def fun_join(list_a, list_b):
    """returns"""
    return list_a[:3] + list_b[-3:]


def print_capitalized(strings):
    """returns"""
    capital = []
    for item in strings:
        capital.append(item.capitalize())
    print("\n".join(capital))


def small_sum(number_list, limit):
    """returns"""
    asum = 0
    listed = [i for i in number_list if i <= limit]
    for item in listed:
        asum += item
    return asum


def cubes(data):
    """returns"""
    cubee = []
    for item in data:
        cubee.append(item**3)
    return cubee


def print_names(names):
    """Print the names in the list of names, one per line"""
    i = 0
    while i < len(names):
        print(names[i])
        i += 1


def print_total_marks(filename):
    """prints"""
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            word = line.split()
            numbers = line.split(sep=',')
            formnums = [int(i.strip()) for i in numbers[2:]]
            print(formnums)
            print(f'{word[0]} {word[1][:-1]}: {sum}')


def number_in_range(lower_bound, upper_bound):
    """returns"""
    input_num = int(input(f'Enter an integer between {lower_bound} and {upper_bound}: '))
    while not lower_bound <= input_num <= upper_bound:
        print('Number out of range. Try again.')
        input_num = int(input(f'Enter an integer between {lower_bound} and {upper_bound}: '))
    return input_num


def print_vee(size):
    for i, num in zip(range(size, 1, -1), range(size -1)):
        print(' '*(num) + ' *' + " "*(i-1) + '*')
    print(' '* (size -1 ) + '*')


def local_maxima(data):
    """local"""
    local_max = []
    for num, i in enumerate(data):
        try:
            if i > data[num+1] and i > data[num-1] and len(data) > 2:
                local_max.append(i)
        except IndexError:
            pass
    return local_max


def is_embedded(needle, haystack):
    """returns"""
    # needle_letters = [i for i in needle]
    unique = []
    unique2 = []
    haystack_letters = []
    for i in haystack:
        if i in needle and i not in unique2:
            unique2.append(i)
    for i in haystack:
        if i in haystack_letters and i not in unique:
            unique.append(i)

    return bool("".join(unique2) in "".join(unique))


print(is_embedded('abc', 'aabbcc'))

