nums = [4, 5, 6, 7, 0, 1, 2]

def rotated_array_search(arr, target):
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

        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

