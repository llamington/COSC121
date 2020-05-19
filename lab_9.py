"""
len(myset1.intersection(myset2)) == 0
myset1.intersection(myset2) == set()
myset1.isdisjoint(myset2)
myset1.symmetric_difference(myset2) == myset1.union(myset2)
engr101.intersection(cosc121)
fake101 | joke112 | haha102
Sets were over 1000 times faster
The dictionary has to have IRD numbers as the keys, and names as the values, because IRD numbers are unique and names aren't.
A dictionary to map from student ID number, represented by an int, to student name.
A dictionary to map from student ID number, represented by a string, to student name.
A dictionary that maps each point on an integer grid, represented as a 2-element tuple of ints, to the height value at that unique grid location.
A dictionary to map from a given first name to a list of the last names of all students in COSC121 with that first name.
No error, but the value associated with key "John Zoq Virmillion" is now "7478593"
inventory.get(product, 0)
"""


def character_set_counts(string_1, string_2, string_3):
    """counts chars"""
    common = set(string_1) & set(string_2)
    absent = common - set(string_3)
    return len(absent)


def get_name(name_dict, id_num):
    """gets name"""
    return name_dict.get(id_num, None)


def find_key(input_dict, value):
    """finds key"""
    for item in input_dict.items():
        if item[1] == value:
            return item[0]


def word_counter(input_str):
    """counts words"""
    words = input_str.lower().split()
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    return freq_dict


def produce_dictionary(filename):
    """produces dictionary from filename"""
    freq_dict = {}
    with open(filename) as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    for line in lines:
        if line != '':
            freq_dict[line] = freq_dict.get(line, 0) + 1
    return freq_dict


import re


def print_word_counts(filename):
    """prints word counts"""
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    for key, value in sorted(freq_dict.items()):
        print(f'{key}: {value}')


def isbn_dictionary(filename):
    """gets isbn"""
    isbn_dict = {}
    try:
        with open(filename) as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f'The file {filename} was not found.')
    else:
        for line in lines:
            words = line.split(',')
            isbn_dict[words[2].strip()] = (words[0], words[1])
        return isbn_dict


def generate_index(words_on_page):
    """generates index"""
    words_dict = {}
    for key, value in words_on_page.items():
        for svalue in value:
            try:
                words_dict[svalue].append(key)
            except KeyError:
                words_dict[svalue] = [key]
    return words_dict


input_dict = {
   1: ['hi', 'there', 'fred'],
   2: ['there', 'we', 'go'],
   3: ['fred', 'was', 'there']}
print(generate_index(input_dict))








