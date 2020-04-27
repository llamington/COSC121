"""
len(items)
list1 + list2
my_list * n
Because there is no item with an index of 4
items[1]
items[-1]
items[n]
items[1:4]
items[1:-2]
items[::2]
items[1::3]
items[::-1]
items.reverse()
items.sort()
items.insert(2, value)
items.remove(target)
items.pop(-1)
string[2]
string[2:5]
string[::-1]
number, street, post_code = location
8364751
"""


def nth_member(data, n):
    """Returns nth member of a list"""
    return data[n]


def num_words(string):
    """Returns number of words in a string"""
    words = string.split()
    return len(words)


def repeat_last(data):
    """Repeats final data"""
    return data + [data[-1]]


def concatenate(strings):
    """concatenates strings"""
    concatenation = ""
    for string in strings:
        concatenation = concatenation + string
    return concatenation


def my_max(data):
    """finds max data"""
    current_max = data[0]
    for datum in data:
        if datum > current_max:
            current_max = datum
        else:
            pass
    return current_max


def cubes(data):
    """return cubes of data"""
    data_cubes = [x ** 3 for x in data]
    return data_cubes


def abs_nums(numbers):
    """returns list of abs numbers"""
    abs_numbers = []
    for number in numbers:
        if number < 0:
            abs_numbers.append(-1 * number)
        else:
            abs_numbers.append(number)
    return abs_numbers


def lower_case(strings):
    """returns lower case strings"""
    lower_strings = []
    for string in strings:
        lower_strings.append(string.lower())
    return lower_strings


def  evens(numbers):
    """returns only even numbers"""
    even_numbers = [x for x in numbers if x % 2 == 0]
    return even_numbers


def long_enough(strings, min_length):
    """return string if > min length"""
    long_strings = [x for x in strings if len(x) >= min_length]
    return long_strings


def top_and_tail(string):
    """removes head and tail"""
    return string[1:-1]


def vertical_strings(string):
    """prints vertical strings"""
    length_word = len(string)
    for letter in string:
        print(letter*length_word)


def are_anagrams(word1, word2):
    """returns true if words are anagrams"""
    if word1 == word2:
        return False
    else:
        word1_list = list(word1)
        word2_list = list(word2)
        word1_list.sort()
        word2_list.sort()
        if word1_list == word2_list:
            return True
        else:
            return False


def cubed_tuple(number):
    """cubes tuple"""
    return (number, number ** 3)


def trouble(a, b):
    z = 21740696
    x = z - a
    y = z - b
    x += 687
    (x, y) = (y, x)
    if x >= y:
        z = x - y
    else:
        z = x // y
    z = z * y
    return z


trouble(21741383, 100000000)