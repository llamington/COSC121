"""
18
0, [1, 1]
0, [0, 2, 0]
0, [0, 2, 0], 1
raise ValueError(f'{num} is not even!')
[5,2,-1,-2], [1,5,-3]
[0,0], [2,2], -3
"""
"""Demo of importing and using a module.
   To be modified for this question as explained in the instructions.
"""
import statistics

FILENAME = "data.txt"   # Name of file containing numbers, one per line

def main():
    """Read some numbers from a file and print their median"""
    in_file = open(FILENAME)
    lines = in_file.read().splitlines()
    in_file.close()

    # Now convert all the lines of text (strings) to numeric values
    numbers = []
    for line in lines:  # Process each line, which must be a number
        numbers.append(float(line))  # Convert string to a number

    # Print the count and the median
    median_value = statistics.stdev(numbers)  # Call the median function
    print("Standard deviation is {:.2f}".format(median_value))



def print_quiz_mark(mark_gained, max_mark=20.0):
    """computes maximum mark"""
    mark_percentage = (mark_gained / max_mark) * 100
    print(f'Your mark: {mark_gained:.1f}/{max_mark:.1f} ({mark_percentage:.1f}%)')


def print_game_score(points, maximum_points=1000.0):
    """computes maximum mark"""
    mark_percentage = (points / maximum_points) * 100
    print(f'Your points: {points:.1f}/{maximum_points:.1f} ({mark_percentage:.1f}%)')


def describe(name='Unknown name', species='unknown creature', location='unknown'):
    """describes an animal"""
    print(f'{name} is a {species}, location: {location}.')


def print_nth_value(data, n):
    """prints nth value"""
    try:
        print(data[n])
    except:
        print('Invalid position provided.')


def print_nth_item_divided(data, n, divisor):
    """divides nth number"""
    try:
        print(data[n] / divisor)
    except IndexError:
        print('Invalid position provided.')
    except ZeroDivisionError:
        print('Cannot divide by zero.')
    except TypeError:
        print('Parameters must be numbers.')
