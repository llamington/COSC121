def inches(centimetres):
    """returns cm"""
    return centimetres / 2.54


def seconds(number_of_days):
    """returns number of seconds"""
    return number_of_days * 24 * 60 ** 2


def total_cost(kilograms, litres, discount_proportion):
    """returns total"""
    return (5 * kilograms + 10 * litres) * (1 - discount_proportion) * 1.15


cost = total_cost(2, 1, 0.5)
# We round your answer to 2 decimal places before printing.
# Don't worry about why.
print(round(cost, 2))