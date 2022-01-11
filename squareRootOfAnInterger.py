def sqrt(target, epsilon=0.01):
    """ Finds the interger of the int target
    Args:
        target (int): number to be squared
        epsilon (float): float point number
    Returns:
        (float): square root
    """
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


print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
