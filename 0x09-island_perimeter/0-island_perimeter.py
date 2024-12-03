#!/usr/bin/python3
'''Calculates the perimeter of the island described in a grid of a 2D array'''


def island_perimeter(grid):
    '''returns perimeter of the island in the grid'''
    # handle empty grid
    if not grid or not grid[0]:
        return 0

    count = 0  # will serve to count the distance of island perimeter
    width = len(grid)
    length = len(grid[0])
    for i in range(width):
        for j in range(length):
            if (grid[i][j] == 1):
                if (grid[i][j-1] == 0 or j == 0):
                    count += 1
                if (grid[i-1][j] == 0 or i == 0):
                    count += 1
                if (grid[i][j+1] == 0 or j == length-1):
                    count += 1
                if (grid[i+1][j] == 0 or i == width-1):
                    count += 1
    return count
