"""Prints student report"""


def invigilated_percent(test_percent, exam_percent):
    """Calculates invigilated percent"""
    return (test_percent * 0.15 + exam_percent * 0.60) / 0.75


def course_total(labs, superquiz, test, exam):
    """Calculates total percentage"""
    return labs * 0.1 + superquiz * 0.15 + test * 0.15 + exam * 0.6


def minimum_exam_mark(labs_mark, superquiz_mark, test_mark):
    """calculate minimum exam mark"""
    return (50 - labs_mark*0.1 - superquiz_mark*0.15 - test_mark*0.15)/0.6


def minimum_exam_mark_comprehensive(labs_mark, superquiz_mark, test_mark):
    """calculate minimum comprehensive mark"""
    required_invigilated_mark = (45*0.75 - test_mark*0.15)/0.60
    required_combined_mark = (50 - labs_mark*0.1 - superquiz_mark*0.15 - test_mark*0.15)/0.6
    if required_combined_mark >= required_invigilated_mark:
        return required_combined_mark
    else:
        return required_invigilated_mark


def main():
    """main function"""
    given_name = input("Given name: ")
    family_name = input("Family name: ")
    lab_score = float(input("Weekly lab total: "))
    assignment_score = float(input("Superquiz total: "))
    test_score = float(input("Test total: "))
    exam_score = float(input("Exam total: "))
    print()
    print("-" * 31)
    print("COSC121 Report ({0})".format(family_name.upper()))
    print("-" * 31)
    invigilated_pass = "yes" if invigilated_percent(test_score, exam_score) >= 45 else "no"
    print("Invigilated pass: {} ({:.2f}%)".format(invigilated_pass, invigilated_percent(test_score, exam_score)))
    total_pass = "yes" if course_total(lab_score, assignment_score, test_score, exam_score) >= 50 else "no"
    print("Course total pass: {} ({:.2f}%)".format(total_pass,
                                                   course_total(lab_score, assignment_score, test_score, exam_score)))
    overall_pass = "yes" if invigilated_pass == "yes" and total_pass == "yes" else "no"
    print("Overall pass: {}".format(overall_pass))
    print("-" * 31)
    if overall_pass == "yes":
        print()
        print("Congratulations {}!".format(given_name.capitalize()))


needed_mark = minimum_exam_mark_comprehensive(100.0, 100.0, 92.0)
print("Needed exam mark: {:.2f}".format(needed_mark))