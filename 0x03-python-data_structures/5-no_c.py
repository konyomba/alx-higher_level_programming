#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for elements in my_string:
        if elements != "c" and elements != "C":
            string += elements
    return string
