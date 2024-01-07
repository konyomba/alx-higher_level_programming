#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    my_list1 = []
    if my_list:
        for element in my_list:
            my_list1.append(False if element % 2 else True)
        return my_list1
