array = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]


def sort_012(input_list):
    ones = []
    twos = []
    zeros = []
    
    if type(input_list) == str:
        return -1
    
    if input_list == [] or input_list == None:
        return None
        
    for element in input_list:
        if element > 2:
            return -1
        
        if element == 0:
            zeros.append(element)
        elif element == 1:
            ones.append(element)
        else:
            twos.append(element)

    newArray = zeros + ones + twos
    return newArray


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

# Will return -1
print(sort_012("ambrose"))

# Will return None
print(sort_012(None))

