


def linear_search(array: list, target):
    """
    Returns the index position of the target if fount, else returns None
    """
    for i in range(len(array)):
        if array[i] == target:
            return i
    return None
