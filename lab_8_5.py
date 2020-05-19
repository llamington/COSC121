"""A program to read a CSV file of rainfalls and print the totals
   for each month.
"""

from os.path import isfile as is_valid_file


def sum_rainfall(month, num_days, columns):
    """sums rainfall"""
    total_rainfall = 0
    for col in columns[2:2 + num_days]:
        total_rainfall += float(col)
    return month, total_rainfall


def process_data(data):
    """processes data"""
    results = []  # A list of (month, rainfall) tuples
    for line in data:
        columns = line.split(',')
        month = int(columns[0])
        num_days = int(columns[1])
        results.append(sum_rainfall(month, num_days, columns))
    return results


def print_rainfalls(results):
    """prints total rainfalls"""
    print('Monthly total rainfalls')
    for (month, total_rainfall) in results:
        print('Month {:2}: {:.1f}'.format(month, total_rainfall))


def get_filename():
    """receives filename"""
    filename = input('Input csv file name? ')
    while not is_valid_file(filename):
        filename = input('Input csv file name? ')
        print('File does not exist.')
    return filename


def data_list(filename):
    """processes data into list"""
    datafile = open(filename)
    data = datafile.read().splitlines()
    datafile.close()
    return data


def main():
    """Prompt the user to provide a csv file of rainfall data, process the
       given file's data, and print the monthly rainfall totals.
       The file is assumed to have the month number in column 1, the number
       of days in the month in column 2, and the floating point rainfalls
       (in mm) for that month in the remaining columns of the row.
    """
    filename = get_filename()
    data = data_list(filename)
    results = process_data(data)
    print_rainfalls(results)


main()
