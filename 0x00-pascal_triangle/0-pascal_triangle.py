#!/usr/bin/python3

def pascal_triangle(n):
    '''
    function to return a list of a given number of rows of the pascal tringle
    '''
    if n <= 0:
        return []
    
    # Start with the first row
    row = [1]
    wholeList = [row]  # Optionally store the rows if needed, remove if you only care about the last row.

    for _ in range(1, n):
        # Create the next row from the previous one
        new_row = [1]  # Every row starts with a 1
        for i in range(1, len(row)):
            # Add elements by summing the two elements above it
            new_row.append(row[i - 1] + row[i])
        new_row.append(1)  # Every row ends with a 1
        row = new_row
        wholeList.append(row)  # Optional, remove to optimize space further

    return wholeList
