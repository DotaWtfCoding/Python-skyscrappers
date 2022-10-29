#file: skyscrapers.py
#descripition: solving city blocks of skyscrapers.
#Language: python 3.9
#Author : Neeraj Reddy Bandi

import sys
"""
main function for solving the puzzle and checking the rules violated.
"""
def main():
    # check if there are too many or insufficient arguments for file handling.
    if len(sys.argv[1:]) != 1:
        print("Usage: python3 skyscrapers.py filename, 'r'")
        sys.exit(1)
    filename = sys.argv[1]


    f = open(filename, 'r')
    n = int(f.readline())  # grid size

    # storing the clues in each direction.
    top = [int(x) for x in f.readline().strip().split()]
    right = [int(x) for x in f.readline().strip().split()]
    bottom = [int(x) for x in f.readline().strip().split()]
    left = [int(x) for x in f.readline().strip().split()]

    # define matrix
    grid = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        grid[i] = [int(x) for x in f.readline().strip().split()]
    f.close()

    # print the puzzle
    print('', end="  ")
    for i in range(n):
        print(top[i], end=" ")
    print('')
    print('', end="  ")
    for i in range(n):
        print('-', end=" ")
    print('')
    for i in range(n):
        print(left[i], end='|')
        for j in range(n - 1):
            print(grid[i][j], end=' ')
        print(grid[i][n - 1], end='|')
        print(right[i])
    print('', end="  ")
    for i in range(n):
        print('-', end=" ")
    print('')
    print('', end="  ")
    for i in range(n):
        print(bottom[i], end=" ")
    print('')

    # flag for clean exit

    # check rule 1: every row and column must contain 1 to n
    # check rule 2: each row and column contains each number only once
    # both the rules are equivalent
    for i in range(n):
        s = []

        for num in grid[i]:
            if num > n or num <= 0:
                print('Invalid value {} in row {}'.format(num, i))
                return
            elif num in s:
                # violation
                print('Duplicate value {} in row {}'.format(num, i))
                return
            else:
                s.append(num)
    for j in range(n):
        col = [row[j] for row in grid]
        s = []
        for num in col:
            if num > n or num <= 0:
                print('Invalid value {} in column {}'.format(num, i))
                return
            elif num in s:
                # violation
                print('Duplicate value {} in column {}'.format(num, j))
                return
            else:
                s.append(num)

    # check rule 3: clues
    # left to right
    for i in range(n):
        count = 1
        prev_max = grid[i][0]
        for j in range(1, n):
            if grid[i][j] > prev_max:
                prev_max = grid[i][j]
                count += 1
        if count != left[i]:
            print('Left clue at position {} violated'.format((i)))
            return

    # right to left
    for i in range(n):
        count = 1
        prev_max = grid[i][n - 1]
        for j in range(n - 2, -1, -1):
            if grid[i][j] > prev_max:
                prev_max = grid[i][j]
                count += 1
        if count != right[i]:
            print('Right clue at position {} violated'.format((i)))
            return

    # top to bottom
    for i in range(n):
        col = [row[i] for row in grid]
        count = 1
        prev_max = col[0]
        for j in range(1, n):
            if col[j] > prev_max:
                prev_max = col[j]
                count += 1
        if count != top[i]:
            print('Top clue at position {} violated'.format((i)))
            return

    # bottom to top
    for i in range(n):
        count = 1
        col = [row[i] for row in grid]
        prev_max = col[n - 1]
        for j in range(n - 2, -1, -1):
            if col[j] > prev_max:
                prev_max = col[j]
                count += 1
        if count != bottom[i]:
            print('Bottom clue at position {} violated'.format((i)))
            return
    print('\nThe puzzle is valid!')


if __name__ == '__main__':
    main()

























