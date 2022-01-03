# -*- coding: utf-8 -*-
"""
Created on Sun Dec 19 19:04:07 2021

@author: ambro
"""

def get_min_max(array):
    max_ = 0
    min_ = 0
    for index in range(len(array)):
        current_element = array[index]
        previous_element = array[index-1]
        print(current_element)

        if current_element > previous_element:
            max_ = current_element
        if current_element < previous_element:
            min_ = current_element
    return (min_, max_)



import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")