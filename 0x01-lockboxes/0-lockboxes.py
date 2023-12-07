#!/usr/bin/python3
""" module that solve lockboxes interview question """


def canUnlockAll(boxes):
    """ function check if all boxes is open or not
        params:
            boxes list of list
        return:
            true or false
    """
    boxesList = boxes[:]
    keys = []
    keys += boxesList[0]
    boxesList[0] = 0
    for key in keys:
        if key < len(boxesList) and boxesList[key] != 0:
            keys += boxesList[key]
            boxesList[key] = 0
    if all(val == 0 for val in boxesList):
        return True
    return False
