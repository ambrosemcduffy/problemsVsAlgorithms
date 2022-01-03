nums = [4, 5, 6, 7, 0, 1, 2]


def findInterger(arr, target):
    """ Finds interger in rotated array
    Args:
        arr (list): rotated array
        target = target number
    Returns:
        (int): index array
    """
    start = 0
    end = len(arr)-1

    while (start <= end):
        middle = (start + end)//2

        if target == middle:
            return arr[middle]
        elif target > middle:
            start = middle + 1
        else:
            end = middle - 1

        return arr[middle]


print(findInterger(nums, 2))
