def rectangle_area(width, height):
    """ Return the area of a rectangle with the given width and height """
    return width*height


def full_name(first_name, last_name):
    """Return a string consisting of the first name, a space
       and the last name.
    """
    return first_name + " " + last_name

def date_string(day_num, month_name, year_num):
    """ Turn the date into a string of the form
            day month, year
    """
    return str(day_num) + " " + month_name + ", " + str(year_num)


def print_date(year, month, day):
    """ Print out the date, formatted as
            year-month-day
    """
    print("{0}-{1}-{2}".format(year, month, day))
print_date(3, 12, 28)


def print_time(hour, minute, second):
    """ Print out the time, formatted as
            hour:minute:second
    """
    print(str(hour) + ":" + str(minute) + ":" + str(second))
print_time(3,7,12)


def get_and_print_rectangle():
    """ Input a rectangle's width and height then print its area """
    width = input("Rectangle width? ")
    height = input("Rectangle height? ")
    width = float(width)
    height = float(height)
    print("The area of the rectangle is: " + str(width*height))


def say_hi():
    """Question 20"""
    name = input("What is your name? ")
    print("Hi " + name.capitalize())


def print_pair(x_coord, y_coord):
    """Question 24"""
    template = "(x, y) = ({0:.1f}, {1:.1f})".format(x_coord, y_coord)
    print(template)

print_pair(1.72356, -22.1111)