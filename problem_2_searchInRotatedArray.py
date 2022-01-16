nums = [4, 5, 6, 7, 0, 1, 2]


def binarySearch(arr, target, start, end):
    """ Finds interger in rotated array
    Args:
        arr (list): rotated array
        target = target number
    Returns:
        (int): index array
    """

    while (start <= end):
        middle = (start + end)//2

        if target == arr[middle]:
            return middle
        elif target > arr[middle]:
            start = middle + 1
        else:
            end = middle - 1
    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if input_list is None or number is None:
        return None
    
    if input_list == [] or number == []:
        return None
    
    if type(input_list) == str or type(number) == str:
        return -1
    numberOfElements = len(input_list)
    mid = len(input_list)//2
    
    if input_list[mid] == number:
        return mid
    
    if input_list[0] <= number and input_list[mid - 1] >= number :
        return binarySearch(input_list, number, 0, mid - 1)
    elif input_list[mid + 1] <= number  and input_list[numberOfElements - 1] >= number:
        return binarySearch(input_list, number, mid + 1, numberOfElements - 1)
    else:
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

# Test cases
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([nums, 2])

# Edge cases

# Will return None
print(rotated_array_search(None, 1))

# Will return -1
print(rotated_array_search("", ""))

# Will return None
print(rotated_array_search([], []))
