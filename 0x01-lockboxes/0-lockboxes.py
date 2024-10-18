#!/usr/bin/python3
'''You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other
boxes.'''


def canUnlockAll(boxes):
    '''check if i can open all boxes'''
    length = len(boxes)
    new_list = []
    for i in range(1, length):
        new_list.append(i)

    for i in boxes:
        for j in i:
            if j == 0:
                continue
            elif j in new_list:
                new_list.remove(j)

    after_length = len(new_list)
    if after_length == 0:
        return True
    return False
