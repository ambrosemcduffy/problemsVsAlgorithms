array1 = [1, 2, 3, 4, 5]
array2 = [4, 6, 2, 5, 9, 8]


def merge(left_array, right_array):
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
    if len(array) <= 1:
        return array

    middle = len(array)//2
    left_array = array[:middle]
    right_array = array[middle:]
    left_array = mergeSort(left_array)
    right_array = mergeSort(right_array)
    return merge(left_array, right_array)


def rearrange_digits(array):
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


arrangedDigits1 = rearrange_digits(array1)
test_function([array1, arrangedDigits1])

arrangedDigits2 = rearrange_digits(array2)
test_function([array2, arrangedDigits2])
