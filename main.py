"""Program that solves 8-puzzle."""

import operator
import sys


# Global value of goal state
goal_state = ['1', '2', '3', '4', '5', '6', '7', '8', '0']
curr_depth = 0
num_nodes = 0
max_queue = 0
checked_puzzles = []


class Node:
    """This class stores attributes for each node."""

    def __init__(self, puzzle):
        self.heuristic = 0  # if uniform cost search, this doesn't change (h(n))
        self.cost = 0  # Number of actions to get there (g(n))
        self.puzzle = puzzle
        self.total = 0  # g(n) + h(n)

    def set_heuristic(self, type):
        if type == 2:
            self.heuristic = heuristic_misplaced(self.puzzle)
        elif type == 3:
            self.heuristic = heuristic_distance(self.puzzle)
        self.total = self.heuristic + self.cost

    def set_cost(self):
        self.cost = curr_depth
        self.total = self.heuristic + self.cost


def search_function(root, type):
    """Search main function."""

    global num_nodes, max_queue

    # Start queue by adding root
    nodes_queue = [root]

    print('Initial state')
    print_puzzle(root.puzzle)
    print()

    while len(nodes_queue) > 0:
        max_queue = max(max_queue, len(nodes_queue))

        # Get the cheapest node
        node = nodes_queue[0]

        if node.puzzle == goal_state:
            print('Goal!!')
            print()
            print('To solve this problem the search algorithm expanded a '
                  'total of ' + str(num_nodes) + ' nodes.\nThe maximum '
                  'number of nodes in the queue at any one time was '
                  + str(max_queue) + '.\nThe depth of the goal node was ' + str(node.cost))
            return

        print('The best state to expand with a g(n) = ' + str(node.cost)
              + ' and h(n) = ' + str(node.heuristic) + ' is...')
        print_puzzle(node.puzzle)
        print('Expanding this node...\n')

        num_nodes += 1
        checked_puzzles.append(node.puzzle)
        nodes_queue = expand(node, nodes_queue, type)

    print('Did not find a solution.')
    return


def print_puzzle(puzzle):
    """Function that prints puzzle."""

    temp = []
    for spot in puzzle:
        if spot == '0':
            temp.append('b')
        else:
            temp.append(spot)

    print(temp[0] + ' ' + temp[1] + ' ' + temp[2])
    print(temp[3] + ' ' + temp[4] + ' ' + temp[5])
    print(temp[6] + ' ' + temp[7] + ' ' + temp[8])

    return


def go_up(puzzle, i, type):
    """This function moves the blank square up, then returns a new child node."""

    new_puzzle = []

    for j in range(len(puzzle)):
        if j == i:
            new_puzzle.append(puzzle[i - 3])
        elif j == (i - 3):
            new_puzzle.append(puzzle[i])
        else:
            new_puzzle.append(puzzle[j])

    new_node = Node(new_puzzle)
    new_node.set_cost()
    if type > 1:
        new_node.set_heuristic(type)

    return new_node


def go_down(puzzle, i, type):
    """This function moves the blank square down, then returns a new child node."""

    new_puzzle = []

    for j in range(len(puzzle)):
        if j == i:
            new_puzzle.append(puzzle[i+3])
        elif j == (i+3):
            new_puzzle.append(puzzle[i])
        else:
            new_puzzle.append(puzzle[j])

    new_node = Node(new_puzzle)
    new_node.set_cost()
    if type > 1:
        new_node.set_heuristic(type)

    return new_node


def go_right(puzzle, i, type):
    """This function moves the blank square right, then returns a new child node."""

    new_puzzle = []

    for j in range(len(puzzle)):
        if j == i:
            new_puzzle.append(puzzle[i + 1])
        elif j == (i + 1):
            new_puzzle.append(puzzle[i])
        else:
            new_puzzle.append(puzzle[j])

    new_node = Node(new_puzzle)
    new_node.set_cost()
    if type > 1:
        new_node.set_heuristic(type)

    return new_node


def go_left(puzzle, i, type):
    """This function moves the blank square left, then returns a new child node."""

    new_puzzle = []

    for j in range(len(puzzle)):
        if j == i:
            new_puzzle.append(puzzle[i - 1])
        elif j == (i - 1):
            new_puzzle.append(puzzle[i])
        else:
            new_puzzle.append(puzzle[j])

    new_node = Node(new_puzzle)
    new_node.set_cost()
    if type > 1:
        new_node.set_heuristic(type)

    return new_node


def expand(node, queue, search_type):
    """This function expands a given node. Then it adds these nodes to the nodes queue."""

    global curr_depth
    curr_depth = node.cost + 1
    for i in range(len(node.puzzle)):
        if node.puzzle[i] == '0':
            if i == 0:
                node1 = go_down(node.puzzle, i, search_type)
                node2 = go_right(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 1:
                node1 = go_down(node.puzzle, i, search_type)
                node2 = go_right(node.puzzle, i, search_type)
                node3 = go_left(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)
                if node3.puzzle not in checked_puzzles:
                    queue.append(node3)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 2:
                node1 = go_down(node.puzzle, i, search_type)
                node2 = go_left(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 3:
                node1 = go_up(node.puzzle, i, search_type)
                node2 = go_down(node.puzzle, i, search_type)
                node3 = go_right(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)
                if node3.puzzle not in checked_puzzles:
                    queue.append(node3)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 4:
                node1 = go_up(node.puzzle, i, search_type)
                node2 = go_down(node.puzzle, i, search_type)
                node3 = go_right(node.puzzle, i, search_type)
                node4 = go_left(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)
                if node3.puzzle not in checked_puzzles:
                    queue.append(node3)
                if node4.puzzle not in checked_puzzles:
                    queue.append(node4)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 5:
                node1 = go_up(node.puzzle, i, search_type)
                node2 = go_down(node.puzzle, i, search_type)
                node3 = go_left(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)
                if node3.puzzle not in checked_puzzles:
                    queue.append(node3)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 6:
                node1 = go_up(node.puzzle, i, search_type)
                node2 = go_right(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 7:
                node1 = go_up(node.puzzle, i, search_type)
                node2 = go_right(node.puzzle, i, search_type)
                node3 = go_left(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)
                if node3.puzzle not in checked_puzzles:
                    queue.append(node3)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue
            if i == 8:
                node1 = go_up(node.puzzle, i, search_type)
                node2 = go_left(node.puzzle, i, search_type)

                del queue[0]
                if node1.puzzle not in checked_puzzles:
                    queue.append(node1)
                if node2.puzzle not in checked_puzzles:
                    queue.append(node2)

                if search_type > 1:
                    queue.sort(key=operator.attrgetter('total'))

                return queue


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


def default_puzzles():
    """This function selects one of the default puzzles."""

    print('Select a default puzzle difficulty level\n'
          '1. Trivial\n'
          '2. Very Easy\n'
          '3. Easy\n'
          '4. Doable\n'
          '5. Oh Boy\n'
          '6. Impossible\n'
          '7. Report problem')
    chosen_puzzle = input()
    print()

    if chosen_puzzle == '1':
        return ['1', '2', '3', '4', '5', '6', '7', '8', '0']
    elif chosen_puzzle == '2':
        return ['1', '2', '3', '4', '5', '6', '7', '0', '8']
    elif chosen_puzzle == '3':
        return ['1', '2', '0', '4', '5', '3', '7', '8', '6']
    elif chosen_puzzle == '4':
        return ['0', '1', '2', '4', '5', '3', '7', '8', '6']
    elif chosen_puzzle == '5':
        return ['8', '7', '1', '6', '0', '2', '5', '4', '3']
    elif chosen_puzzle == '6':
        return ['1', '2', '3', '4', '5', '6', '8', '7', '0']
    elif chosen_puzzle == '7':
        return ['1', '2', '3', '4', '0', '6', '7', '5', '8']
    else:
        print('Invalid default puzzle.')
        sys.exit()


if __name__ == "__main__":

    # Intro
    print('Welcome to Jessica Gonzalez 8-puzzle solver.')
    puzzle_type = input('Type “1” to use a default puzzle, or “2” to enter your own puzzle.\n')
    print()

    puzzle_arr = []

    # Get puzzle
    if puzzle_type == '1':
        puzzle_arr = default_puzzles()
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
        search_function(root, 1)
    elif search_type == '2':
        root.set_heuristic(2)
        search_function(root, 2)
    elif search_type == '3':
        root.set_heuristic(3)
        search_function(root, 3)
    else:
        print('Invalid search type.')
