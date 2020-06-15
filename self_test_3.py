def divisible_by_9(number):
    """div by 9"""
    if number % 9 == 0:
        return True
    else:
        return False


def ro_at_either_end(string):
    """ro at other end"""
    try:
        if string[-2:] == 'ro' or string[:2] == 'ro':
            return True
        else:
            return False
    except IndexError:
        return False


def silly(i, j):
    """returns"""
    return bool(7 != i < j < 10)


def is_ok(angle):
    """is angle ok"""
    if angle >= 98.074:
        return True
    else:
        return False


def is_fashionable(socks_colour, tie_colour):
    """is fashionable"""
    if tie_colour == 'beige' and socks_colour in ['red', 'linen']:
        return True
    else:
        return False


def level_of_risk(weight, age):
    """level of risk"""
    if age >= 64:
        if weight > 80:
            return 10
        else:
            return 4
    else:
        if weight > 80:
            return 4
        else:
            return 2

