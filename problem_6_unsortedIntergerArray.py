import random


def get_min_max(array):
    """ Obtains min and max of an array
    Args:
        array (list): list of elements
    Returns:
        tuple: min and max elements
    """
    max_element = None
    min_element = None
    
    if array == None:
        return None
    if type(array) == int or type(array) == float:
        return -1
    
    for index in range(1, len(array)):
        current_element = array[index]
        previous_element = array[index-1]
        
        if previous_element > current_element:
            inmax = previous_element
            inmin = current_element
        else:
            inmax = current_element
            inmin = previous_element
        
        if max_element is None:
            max_element = inmax
        
        if min_element is None:
            min_element = inmin
            
        if inmin < min_element:
            min_element = inmin
        if inmax > max_element:
            max_element = inmax
    return (min_element, max_element)


# Test Cases
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [i for i in range(500, 867)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((500, 866) == get_min_max(l)) else "Fail")


l = [i for i in range(2, 365)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((2, 364) == get_min_max(l)) else "Fail")


# Edge Cases

# Will return None
print(get_min_max(None))

# Will return -1
print(get_min_max(3))

