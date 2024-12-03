#!/usr/bin/python3
'''Calculates the perimeter of the island described in a grid of a 2D array'''


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.
    :param grid: List[List[int]], a 2D grid
    :return: int, the perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:  # Land cell
                # Assume each land cell initially contributes 4 sides
                perimeter += 4
                # Check above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2  # Remove 2 sides for the shared edge
                # Check left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2  # Remove 2 sides for the shared edge
    return perimeter
