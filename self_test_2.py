def office_id(building_name, room_number):
    """office ID"""
    return f'{building_name} {str(room_number)}'


def print_time(hour, minute, second):
    """prints time"""
    print(f'{hour}:{minute}:{second}')


def input_and_print_rectangle():
    """prints rec"""
    width = float(input('Width? '))
    height = float(input('Height? '))
    print(f'Area: {height*width:.2f}')


def say_big_hi():
    """says hi"""
    name = input('Who are you? ')
    print(f'Hello there {name.upper()}.')