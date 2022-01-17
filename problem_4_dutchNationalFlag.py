def sort_012(array):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if array == [] or array == None:
        return None
    
    if type(array) == str:
        return -1
    front_index = 0
    element_2_index = len(array)-1
    element_0_index = 0
    
    while front_index <= element_2_index:
        if array[front_index] > 2:
            return -1 
        if array[front_index] == 0:
            array[front_index] = array[element_0_index]
            array[element_0_index] = 0
            front_index += 1
            element_0_index += 1
        
        elif array[front_index] == 2:
            array[front_index] = array[element_2_index]
            array[element_2_index] = 2
            element_2_index -= 1
        else:
            front_index += 1
    return array



def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# Test Cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# Edge Cases

# Will return None
print(sort_012([]))

# Should return -1
print(sort_012([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 3]))
# Will return -1
print(sort_012("ambrose"))

# Will return None
print(sort_012(None))

