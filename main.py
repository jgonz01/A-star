#import

# Global variables
first_row = ''
second_row = ''
third_row = ''


def get_input():
    """This function gets user input."""
    print('Welcome to Bertie Woosters 8-puzzle solver.')
    puzzle_type = input('Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n')

    if puzzle_type == '1':
        print('Default')
    elif puzzle_type == '2':
        print('Enter your puzzle, use a zero to represent the blank')
        first_row = input('Enter the first row, use space or tabs between numbers: ')
        second_row = input('Enter the second row, use space or tabs between numbers: ')
        third_row = input('Enter the third row, use space or tabs between numbers: ')

    return


if __name__== "__main__":
    get_input()


