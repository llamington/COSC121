"""
enumerate(items)
133
"""


def print_squares_to_number(number):
    """Prints squares to a number"""
    if number < 1:
        print("ERROR: number must be at least 1")
    else:
        for i in range(1, number + 1):
            print("{0} * {0} = {1}".format(i, i*i))


def set_lowercase(strings):
    """Sets a string to lowercase"""
    for i, word in enumerate(strings):
        strings[i] = word.lower()
    return strings


def my_enumerate(items):
    """enumerates list"""
    counter = 0
    enumerated_items = []
    for i in items:
        enumerated_items.append((counter, i))
        counter += 1
    return enumerated_items


def get_column(game, col_num):
    """returns column of board"""
    column = []
    for i in range(3):
        column.append(game[i][col_num])
    return column


def diagonals(game):
    """returns diagonal"""
    diagonal_1 = []
    diagonal_2 = []
    for i in range(3):
        diagonal_1.append(game[i][i])
        diagonal_2.append(game[i][-1-i])
    return diagonal_1, diagonal_2


def row_sums(square):
    """returns sum of row"""
    result = []
    for num, row in enumerate(square):
        sums = 0
        for column in row:
            sums += column
        result.append(sums)
    return result


def column_sums(square):
    """Returns sum of columns"""
    sums = [0] * len(square)
    for num, rows in enumerate(square):
        for nums, column in enumerate(square[num]):
            sums[nums] += column
    return sums


def print_daily_totals(rainfalls):
    """prints daily rainfall"""
    for num, row in enumerate(rainfalls):
        sums = 0
        for column in row:
            sums += column
        print("Day {} total: {}".format(num, sums))


def months_to_reach_target(principal, interest_percentage_per_annum, target):
    """returns months to reach target"""
    months = 0
    while principal < target:
        principal *= (1+interest_percentage_per_annum/1200)
        months += 1
    return months


def print_names(names):
    """prints names"""
    i = 0
    while i < len(names):
        print(names[i])
        i += 1


def print_names2(people):
    """prints names"""
    i = 0
    while i < len(people):
        k = 0
        string = ""
        while k < len(people[i]):
            string += people[i][k] + " "
            k += 1
        print(string)
        i += 1


def guess_a_number(target_number, lower_bound, upper_bound):
    """Guesses a number"""
    print("I'm thinking of a number between {} and {}.".format(lower_bound, upper_bound))
    guess = int(input("What do you think it is? "))
    while guess != target_number:
        print("That's not my number. Try again.")
        guess = int(input("What do you think it is? "))
    print("Congratulations! You guessed my number!")


def num_rushes(slope_height, rush_height_gain, back_sliding):
    """Calculates the number of rushes required to get up scree slope"""
    current_height = 0
    rushes = 1
    current_height += rush_height_gain
    while current_height < slope_height:
        current_height -= back_sliding
        rushes += 1
        current_height += rush_height_gain
    return rushes


def num_rushes2(slope_height, rush_height_gain, back_sliding):
    """Calculates second number of rushes"""
    current_height = 0
    rushes = 1
    current_height += rush_height_gain
    while current_height < slope_height:
        rushes += 1
        current_height -= back_sliding*0.95**rushes
        current_height += rush_height_gain*0.95**rushes
    return rushes


ans = num_rushes2(10, 10, 9)
print(ans)

