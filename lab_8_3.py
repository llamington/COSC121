"""Print all the perfect squares from 2 up to a given maximum.
   This version is refactored to make it more understandable
   and more maintainable."""


def read_bound(message):
    """Reads the upper bound from the standard input (keyboard).
       If the user enters something that is not a positive integer
       the function issues an error message and retries
       repeatedly - as per the original code."""

    # WHAT GOES HERE?
    bound = None
    while bound is None:
        line = input(message)
        if line.isnumeric():
            bound = int(line)
        else:
            print("You must enter a positive number.")
    return bound


def is_perfect_square(number):
    """Returns True if and only if number is a perfect square,
    otherwise returns False.
    """

    # AND WHAT GOES HERE?
    square_root = number**(1/2)
    if square_root - 1e-9 < int(square_root) < square_root + 1e-9:
        return True
    else:
        return False


def print_squares(lower_bound, upper_bound, squares):
    """Print the given list of all the squares up to the given upper bound.
    The printout should be in the same format as the original code. """

    # AND WHAT GOES HERE?
    print(f'The perfect squares from {lower_bound} to {upper_bound} are:')
    for square in squares:
        print(square, end=' ')


def main():
    """Every home should have one"""
    lower_bound = read_bound('Enter the lower bound: ')
    upper_bound = read_bound('Enter the upper bound: ')
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)

    print_squares(lower_bound, upper_bound, squares)


main()
