def sqrt(target, epsilon):
    """ Finds the interger of the int target
    Args:
        target (int): number to be squared
        epsilon (float): float point number
    Returns:
        (float): square root
    """

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

    return answer


print(sqrt(24, 0.01))
