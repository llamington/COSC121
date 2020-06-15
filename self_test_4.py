def tuplinator(string):
    """returns tup"""
    return string, string*2, string*3


def double_first(data, wipeout):
    """doubles"""
    data_return = []
    if wipeout:
        for item in data:
            data_return += [item, item]
    else:
        data_return.append(data[0])
        data_return += data
    return data_return


def upper_case(strings):
    """upper case"""
    upper_strings = []
    for s in strings:
        upper_strings.append(s.upper())
    return upper_strings


def almost_last(data):
    """almost"""
    return data[-2]


def big_sum(number_list, limit):
    """sums"""
    asum = 0
    for item in number_list:
        if item >= limit:
            asum += item

    return asum


def odds(numbers):
    """return odd"""
    odd_list = []
    for number in numbers:
        if (number + 1) % 2 == 0:
            odd_list.append(number)

    return odd_list

