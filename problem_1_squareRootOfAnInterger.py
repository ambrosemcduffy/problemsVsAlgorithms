def sqrt(target):
    """ Finds the interger of the int target
    Args:
        target (int): number to be squared
        epsilon (float): float point number
    Returns:
        (float): square root
    """
    epsilon=0.01
    
    if target is None:
        return -1
    if type(target) == str:
        return -1
    if target == 1:
        return 1
    if type(target) != int and type(epsilon) != float:
        return -1

    start = 0
    end = target
    answer = (start+end)/2.0

    while abs(answer ** 2 - target) >= epsilon:
        if target > answer**2:
            start = answer
        else:
            end = answer
        answer = (start + end)/2.0

    return int(answer)


# Test case
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# Edge Case
print(sqrt(None))
print(sqrt("Test"))
