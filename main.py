"""Program that solves 8-puzzle. FIXME"""

# Global value of goal state
goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', '0']


class Node:
    """This class stores attributes for each node."""

    def __init__(self, puzzle):
        self.heuristic = 0 # if uniform cost search, this doesn't change
        self.cost = 1 # No cost so set to 1 for all
        self.children = []
        self.parent = []
        self.puzzle = puzzle

    def set_children(self):
        pass

    def set_heuristic(self):
        pass


def uniform_cost_search(problem):
    """Uniform Cost Search main function."""

    # Start queue by adding root
    nodes_queue = [problem]

    while not nodes_queue:
        # Get the cheapest node
        node = nodes_queue[0]

        if node.puzzle == goal_state:
            pass
            #FIXME

        expand(node, nodes_queue)


    # Return failure


def expand():
    """This function expands a given node. Then it adds these nodes to the nodes queue."""


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

    return h


def heuristic_distance(puzzle):
    """This function calculates the heuristic for distance."""

    h = 0

    if puzzle[0] != '1' and puzzle[0] != '0':
        if puzzle[0] == '2':
            h += 1
        if puzzle[0] == '3':
            h += 2
        if puzzle[0] == '4':
            h += 1
        if puzzle[0] == '5':
            h += 2
        if puzzle[0] == '6':
            h += 3
        if puzzle[0] == '7':
            h += 2
        if puzzle[0] == '8':
            h += 3

    if puzzle[1] != '2' and puzzle[1] != '0':
        if puzzle[1] == '1':
            h += 1
        if puzzle[1] == '3':
            h += 1
        if puzzle[1] == '4':
            h += 2
        if puzzle[1] == '5':
            h += 1
        if puzzle[1] == '6':
            h += 2
        if puzzle[1] == '7':
            h += 3
        if puzzle[1] == '8':
            h += 2

    if puzzle[2] != '3' and puzzle[2] != '0':
        if puzzle[2] == '1':
            h += 2
        if puzzle[2] == '2':
            h += 1
        if puzzle[2] == '4':
            h += 3
        if puzzle[2] == '5':
            h += 2
        if puzzle[2] == '6':
            h += 1
        if puzzle[2] == '7':
            h += 4
        if puzzle[2] == '8':
            h += 3

    if puzzle[3] != '4' and puzzle[3] != '0':
        if puzzle[3] == '1':
            h += 1
        if puzzle[3] == '2':
            h += 2
        if puzzle[3] == '3':
            h += 3
        if puzzle[3] == '5':
            h += 1
        if puzzle[3] == '6':
            h += 2
        if puzzle[3] == '7':
            h += 1
        if puzzle[3] == '8':
            h += 2

    if puzzle[4] != '5' and puzzle[4] != '0':
        if puzzle[4] == '1':
            h += 2
        if puzzle[4] == '2':
            h += 1
        if puzzle[4] == '3':
            h += 2
        if puzzle[4] == '4':
            h += 1
        if puzzle[4] == '6':
            h += 1
        if puzzle[4] == '7':
            h += 2
        if puzzle[4] == '8':
            h += 1

    if puzzle[5] != '6' and puzzle[5] != '0':
        if puzzle[5] == '1':
            h += 3
        if puzzle[5] == '2':
            h += 2
        if puzzle[5] == '3':
            h += 1
        if puzzle[5] == '4':
            h += 2
        if puzzle[5] == '5':
            h += 1
        if puzzle[5] == '7':
            h += 3
        if puzzle[5] == '8':
            h += 2

    if puzzle[6] != '7' and puzzle[6] != '0':
        if puzzle[6] == '1':
            h += 2
        if puzzle[6] == '2':
            h += 3
        if puzzle[6] == '3':
            h += 4
        if puzzle[6] == '4':
            h += 1
        if puzzle[6] == '5':
            h += 2
        if puzzle[6] == '6':
            h += 3
        if puzzle[6] == '8':
            h += 1

    if puzzle[7] != '8' and puzzle[7] != '0':
        if puzzle[7] == '1':
            h += 3
        if puzzle[7] == '2':
            h += 2
        if puzzle[7] == '3':
            h += 3
        if puzzle[7] == '4':
            h += 2
        if puzzle[7] == '5':
            h += 1
        if puzzle[7] == '6':
            h += 2
        if puzzle[7] == '7':
            h += 1

    if puzzle[8] != '0':
        if puzzle[8] == '1':
            h += 4
        if puzzle[8] == '2':
            h += 3
        if puzzle[8] == '3':
            h += 2
        if puzzle[8] == '4':
            h += 3
        if puzzle[8] == '5':
            h += 2
        if puzzle[8] == '6':
            h += 1
        if puzzle[8] == '7':
            h += 2
        if puzzle[8] == '8':
            h += 1

    return h


if __name__ == "__main__":

    # Intro
    print('Welcome to Jessica Gonzalez 8-puzzle solver.')
    puzzle_type = input('Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n')
    print()

    # Get puzzle
    if puzzle_type == '1':
        print('Default:')
        puzzle_arr = ['1', '2', '3', '4', '5', '0', '7', '8', '6']
        print('1 2 3\n'
              '4 5 0\n'
              '7 8 6\n')
        #FIXME
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

    # Create root node object
    root = Node(puzzle_arr)

    # Call appropriate search function
    if search_type == '1':
        uniform_cost_search(root, 0)
    elif search_type == '2':
        #heuristic = heuristic_misplaced(puzzle_arr)
    elif search_type == '3':
        #heuristic = heuristic_distance(puzzle_arr)
    else:
        print('Invalid search type.')
