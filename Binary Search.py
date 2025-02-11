#Binary Search

# A function that takes a list and target parameter
# Multiple variables: middle, start, end, steps
# Recursion or while loop
# Increase the step each time a split is done
# conditions to track target position
# We are assuming list to be sorted.

import math

def binary_search(list, element):
    middle = 0
    start = 0
    end = len(list)
    steps = 0
    frontlist = []
    backlist = []

    while(start<=end):
        for i in (0,math.ceil(len(list)/2)):
            frontlist = frontlist.append(list[i])

        for i in (math.ceil(len(list)/2),len(list)):
            backlist = backlist.append(list[i])

        if len(frontlist)<element:
            list = frontlist
        else:
            list = backlist
        steps = steps+1
        start = start+len(list)
    return list[0]

