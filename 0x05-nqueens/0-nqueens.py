#!/usr/bin/env python3
'''Solves the N Queen challange'''
import sys


def solve_n_queens(n):
    '''returns the solution of N Queens challenge'''
    def is_safe(board, row, col):
        '''checks if it safe to place a queen in the row column'''
        for i in range(row):
            if board[i] == col or \
                    board[i] - i == col - row or \
                    board[i] + i == col + row:
                        return False
        return True


    def place_queens(board, row):
        '''check if its possible to place queens in that row'''
        if row == n:
            # soln is found, add it to results
            soln = [[i, board[i]] for i in range(n)]
            results.append(soln)
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col # place queen at (row, col)
                place_queens(board, row + 1)
                board[row] = -1

    results = []
    board = [-1] * n
    place_queens(board, 0)
    return results


if __name__ == '__main__':
    '''Allow module to only execute in main()'''
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)

    solutions = solve_n_queens(N)
    for soln in solutions:
        print(soln)
