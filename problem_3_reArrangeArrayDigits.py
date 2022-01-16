array1 = [1, 2, 3, 4, 5]
array2 = [4, 6, 2, 5, 9, 8]


def merge(left_array, right_array):
    """ Merges left and right arrays after sorting
    Args:
        left_array (list): array with elements
        right_array (list): array with elements
    Returns:
        list: merged sorted array 
    """
    merged_array = []
    left_index = 0
    right_index = 0

    while len(left_array) > left_index and len(right_array) > right_index:
        if left_array[left_index] < right_array[right_index]:
            merged_array.append(right_array[right_index])
            right_index += 1
        else:
            merged_array.append(left_array[left_index])
            left_index += 1

    merged_array += left_array[left_index:]
    merged_array += right_array[right_index:]
    return merged_array


def mergeSort(array):
    """ recursively sorts array
    Args:
        array (list): array elements
    Return:
        list: sorted array
    """
        
    if len(array) <= 1:
        return array

    middle = len(array)//2
    left_array = array[:middle]
    right_array = array[middle:]
    left_array = mergeSort(left_array)
    right_array = mergeSort(right_array)
    return merge(left_array, right_array)


def rearrange_digits(array):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if array is None or array == []:
        return None

    if type(array) == str and type(array) != list:
        return -1
    
    sorted_array = mergeSort(array)
    left = ""
    right = ""
    for i in range(len(sorted_array)):
        if (i % 2) == 0:
            left += "{}".format(sorted_array[i])
        else:
            right += "{}".format(sorted_array[i])
    return [int(left), int(right)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[1, 100, 8], [1001, 8]])


# Edge cases

print(rearrange_digits(None))
print(rearrange_digits([]))
print(rearrange_digits(""))

