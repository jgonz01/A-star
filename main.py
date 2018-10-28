#import


def heuristic_misplaced(puzzle):
    """This functions calculates the heuristic for misplaced tiles."""

    h = 0

    if puzzle[0] != '1':
        h += 1
    if puzzle[1] != '2':
        h += 1
    if puzzle[2] != '3':
        h += 1
    if puzzle[3] != '4':
        h += 1
    if puzzle[4] != '5':
        h += 1
    if puzzle[5] != '6':
        h += 1
    if puzzle[6] != '7':
        h += 1
    if puzzle[7] != '8':
        h += 1
    if puzzle[8] != '0':
        h += 1

    return h


def heuristic_distance(puzzle):
    """This function calculates the heuristic for distance."""


if __name__== "__main__":

    # Intro
    print('Welcome to Bertie Woosters 8-puzzle solver.')
    puzzle_type = input('Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n')
    print()

    # Get puzzle
    if puzzle_type == '1':
        print('Default:')
        puzzle_arr = ['1', '2', '3', '4', '5', '0', '7', '8', '6']
        print('1 2 3\n'
              '4 5 0\n'
              '7 8 6\n')
    elif puzzle_type == '2':
        print('Enter your puzzle, use a zero to represent the blank')
        first_row = input('Enter the first row, use space or tabs between numbers: ').replace('\t', ' ')
        second_row = input('Enter the second row, use space or tabs between numbers: ').replace('\t', ' ')
        third_row = input('Enter the third row, use space or tabs between numbers: ').replace('\t', ' ')
        print()

        puzzle_arr = first_row.split(' ') + second_row.split(' ') + third_row.split(' ')

    # Get search algorithm
    print('Enter your choice of algorithm\n'
          '1. Uniform Cost Search.\n'
          '2. A* with the Misplaced Tile heuristic.\n'
          '3. A* with the Manhattan distance heuristic.')
    search_type = input()
    print()

    if search_type == '1':
        heuristic = 0
    elif search_type == '2':
        heuristic = heuristic_misplaced(puzzle_arr)
    elif search_type == '3':
        heuristic = heuristic_distance(puzzle_arr)
    else:
        print('Invalid search type.')
    print(heuristic)




