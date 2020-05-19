"""
cost
cost
cost
all
cost_of_items
"""
"""prints discount"""


def main():
    """main function"""
    # First initialise all variables
    cost_per_item = 27      # Without discount
    discount_percent = 10
    discount_threshold = 20

    # Get the number of items in this delivery
    n_items = int(input("Count of items? "))

    # Now compute the total cost
    cost = fun_function(n_items, cost_per_item, discount_percent, discount_threshold)

    # Print the results
    print('{} items delivered at a cost of ${:.2f}'.format(n_items, cost))


def fun_function(n_items, cost_per_item, discount_percent, discount_threshold):
    """fun function"""
    cost = n_items * cost_per_item  # line 1
    if n_items > discount_threshold:  # line 2
        cost = cost * (1 - discount_percent / 100)
    return cost


main()


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
