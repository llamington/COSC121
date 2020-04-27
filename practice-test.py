def print_message():
    """prints message"""
    print("It's pleasing!")


def print_date(year, month, day):
    """ Print out the date, formatted as
            year-month-day
    """
    print(f'{year}-{month}-{day}')


def linear_func(x):
    """retuns linear"""
    return 2*x + 3


def my_abs(value):
    """returns absolute value"""
    if value < 0:
        return -1*value
    else:
        return value


def censor(s):
    """returns censored"""
    if len(s) == 4:
        return "****"
    else:
        return s


def silly(i, j):
    """Does something silly"""
    return bool(j <= i and i > 3 and j < 12)


def alarm_clock(day, on_vacation):
    """returns alarm time"""
    if on_vacation:
        if 1 <= day <= 5:
            return "10:00"
        else:
            return "off"
    else:
        if 1 <= day <= 5:
            return "7:00"
        else:
            return "10:00"


def double_char(s):
    """returns"""
    s = list(s)
    for num, i in enumerate(s):
        s[num] = i + s[num]
    return "".join(s)


def num_words(string):
    """returns num words"""
    return len(string.split())


def absolute_values(numbers):
    """returns absolute numbers"""
    absolute = []
    for i in numbers:
        absolute.append(abs(i))
    return absolute


def short_words(word_list):
    """short words"""
    return [i for i in word_list if len(i) <= 4]


def row_sums(square):
    """returns row sums"""
    rows_sum = []
    for i in square:
        asum = 0
        for j in i:
            asum += j
        rows_sum.append(asum)
    return rows_sum


def alternating_sign_sum(nums):
    """alternating"""
    alt_sum = 0
    for num, i in enumerate(nums):
        if num % 2 == 0:
            alt_sum += i
        else:
            alt_sum -= i
    return alt_sum


def twiddle(s):
    """rewritten"""
    i = 0
    num = -17
    while i < len(s):
        if ord(s[i]) > 73:
            num = num * 2 + (ord(s[i]) - 70) * 11
        else:
            num = num // 2 + ord(s[i]) * 7
        i += 1
    return num


def pivot(nums, threshold):
    """thing"""
    lower = [i for i in nums if i < threshold]
    upper = [i for i in nums if i >= threshold]
    return (lower, upper)


def count_lines_with_word(filename, word):
    """counts lines with word"""
    count = 0
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            if word in line.split():
                count += 1
    return count


def zip_lists(list1, list2):
    """zips list"""
    finished = []
    if len(list1) >= len(list2):
        for num, i in enumerate(list1):
            finished.append(i)
            try:
                finished.append(list2[num])
            except IndexError:
                pass
    else:
        for num, i in enumerate(list2):
            try:
                finished.append(list1[num])
            except IndexError:
                pass
            finished.append(i)
    return finished


def print_diamond(height):
    """prints hollow"""
    middle = round(height/2)
    for i in range(height):
        if i == height-1 or i == 0:
            print('*')
        elif i <= middle:
            print("*" + " "*(2*i-1) + "*")
        else:
            print("*" + " "*(height-1-i) + "*")

print_diamond(5)





