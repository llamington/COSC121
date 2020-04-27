def my_abs(value):
    """Returns absolute value"""
    if value >= 0:
        return value
    else:
        return -1*value


def is_odd(number):
    """Returns true if number is true"""
    num = number % 2
    if num == 0:
        return False
    else:
        return True


def silly(i, j):
    """Does something silly"""
    return i > j and i != 3 and j != 2


def x_at_either_end(string):
    """Returns true if x is at either end of string"""
    lower_string = string.lower()
    return lower_string.startswith('x') or lower_string.endswith('x')


def same_ends(string_1, string_2):
    """Returns true if strings start and end with the same letter, but are not the same"""
    if string_1[0] == string_2[0] and string_1[-1] == string_2[-1]:
        if string_1 != string_2:
            return True
        else:
            return False
    else:
        return False


def bmi_risk(bmi, age):
    """Returns risk"""
    if bmi < 22 and age < 45:
        return "Low"
    elif bmi < 22 and age >= 45:
        return "Medium"
    elif bmi >= 22 and age < 45:
        return "Medium"
    elif bmi >= 22 and age >= 45:
        return "High"


def thing(i, j):
    """Does something silly"""
    return 10 < i <= 20 and j >= 5


"""Program to determine if a person is allowed to drive, given their
   age and blood alcohol level.
"""

alcohol_level_string = input("Enter blood alcohol level (mg/100ml): ")
alcohol_level = float(alcohol_level_string)
age_string = input("Enter age in years: ")
age = float(age_string)
if (age < 20 and alcohol_level > 0) or alcohol_level >= 50:
    print("You're not allowed to drive")
elif age >= 20 and 30 <= alcohol_level < 50:
    print("You're legally allowed to drive, but please don't")
else:
    print("You're allowed to drive")


"""Program to determine if a person is allowed to drive, given their age and blood alcohol level."""
def main():
    """Main Function"""

    alcohol_level_string = input("Enter blood alcohol level (mg/100ml): ")
    alcohol_level = float(alcohol_level_string)
    age_string = input("Enter age in years: ")
    age = float(age_string)
    if (age < 20 and alcohol_level > 0) or alcohol_level >= 50:
        print("You're not allowed to drive")
    elif age >= 20 and 30 <= alcohol_level < 50:
        print("You're legally allowed to drive, but please don't")
    else:
        print("You're allowed to drive")


main()
