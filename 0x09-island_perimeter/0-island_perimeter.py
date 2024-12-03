#!/usr/bin/python3
'''Calculates the perimeter of the island described in a grid of a 2D array'''


def island_perimeter(grid):
    '''returns perimeter of the island in the grid'''
    count = 0  # will serve to count the distance of island perimeter
    width = len(grid)
    for i in range(width):
        length = len(grid[i])
        for j in range(length):
            if (grid[i][j] == 1):
                if (grid[i][j-1] == 0):
                    count += 1
                if (grid[i-1][j] == 0):
                    count += 1
                if (grid[i][j+1] == 0):
                    count += 1
                if (grid[i+1][j] == 0):
                    count += 1
    return count
