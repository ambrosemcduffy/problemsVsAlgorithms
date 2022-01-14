# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 19:04:07 2021

@author: ambro
"""

def get_min_max(array):
    max_ = 0
    min_ = 0
    
    for index in range(1, len(array)):
        current_element = array[index]
        previous_element = array[index-1]
        if current_element > previous_element:
            inmax = current_element
            if inmax > max_:
                max_ = inmax
                min_ = inmax
        if current_element < previous_element:
            inmin = current_element
        else:
            inmin = previous_element
        
        if inmin < min_:
            min_ = inmin
    print(min_, max_)
    return (min_, max_)


import random

l = [i for i in range(60, 500)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((60, 499) == get_min_max(l)) else "Fail")
