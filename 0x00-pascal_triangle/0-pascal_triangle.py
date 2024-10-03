#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []

    wholeList = []

    for row in range(0, n):
        if row == 0:
            newList = [1]
            wholeList.append(newList)
        elif row == 1:
            newlist = [1, 1]
            wholeList.append(newlist)
        elif row >= 2:
            x = len(wholeList[(row - 1)])
            newlist = [1]
            for i in range(0, x - 1):
                value = wholeList[(row - 1)][i] + wholeList[(row - 1)][i +1]
                newlist.append(value)
            newlist.append(1)
            wholeList.append(newlist)

    return wholeList
