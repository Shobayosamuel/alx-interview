#!/usr/bin/python3
"""Interview question on canUnlockAll"""


def canUnlockAll(boxes):
    """Return True if the bos=xes has a key, return false if otherwise"""
    keys = [0]  # Start with the key to the first box

    for box_index in keys:
        for key in boxes[box_index]:
            if key < len(boxes) and key not in keys:
                keys.append(key)

    for box_index in range(1, len(boxes)):
        if box_index not in keys:
            return False

    return True
