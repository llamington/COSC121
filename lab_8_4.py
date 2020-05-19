"""Read and process a file of student names and marks.
   Written for COSC121S2.
   Author: Angus McGurkinshaw
   Date: 29 July 2017.
"""


def get_filename():
    """Return the name of the student data file to be processed.
       This is a so-called 'stub' implementation which always returns
       the same filename. A fuller implementation would prompt the user
       for the filename.
    """
    return "data.csv"


def read_data(filename):
    """Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    """
    # ****** YOUR CODE HERE ******
    formatted_data = []
    with open(filename) as file:
        lines = file.readlines()
        for line in lines:
            words = line.split(',')
            formatted_data.append((words[0], float(words[-1])))
    return formatted_data


def statistics(student_data):
    """Given a list of (name, mark) pairs, returns a tuple containing
       statistics extracted from the list. The components of the returned tuple
       are minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    """
    # ****** YOUR CODE HERE ******
    minimum_mark = min(student_data, key=lambda x: x[1])[1]
    maximum_mark = max(student_data, key=lambda x: x[1])[1]
    highest = max(student_data, key=lambda x: int(x[1]))
    top_students = sorted([i[0] for i in student_data if i[-1] == highest[-1]])
    average_mark = sum([float(i[1]) for i in student_data])/len(student_data)
    return minimum_mark, maximum_mark, average_mark, top_students


def print_results(stats_tuple):
    """Print the statistics given. The parameters 'stats_tuple' is a
       tuple of the form returned by the 'statistics' function
       above. The required output is shown in the example output table.
    """
    (minimum, maximum, average, top_students) = stats_tuple
    print("Minimum mark is: {:.1f}".format(minimum))
    print("Maximum mark is: {:.1f}".format(maximum))
    print("Average mark is: {:.1f}".format(average))

    if len(top_students) == 1:
        print("The top student: {}".format(top_students[0]))
    else:
        print("The top-equal students:\n  {}".format(", ".join(top_students)))


def main():
    """The main function (see module docstring)"""
    filename = get_filename()
    data = read_data(filename)
    stats = statistics(data)
    print_results(stats)


main()
