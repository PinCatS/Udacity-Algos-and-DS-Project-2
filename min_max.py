def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if ints is None:
        return None
    
    if len(ints) == 1:
        return (ints[0], ints[0])

    minValue = None
    maxValue = None
    
    for e in ints:
        if minValue is None or minValue > e:
            minValue = e
        if maxValue is None or maxValue < e:
            maxValue = e
    return (minValue, maxValue)


## Example Test Case of Ten Integers
import random

print("Test case 1")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

# other test cases
print("Test case 2")
l = []              # None, None
print ("Pass" if ((None, None) == get_min_max(l)) else "Fail")

print("Test case 3")
l = [1]             # (1, 1)
print ("Pass" if ((1, 1) == get_min_max(l)) else "Fail")

print("Test case 4")
l = None            # None
print ("Pass" if (None == get_min_max(l)) else "Fail")

print("Test case 5")
l = [-1, -5]        # (-5, -1)
print ("Pass" if ((-5, -1) == get_min_max(l)) else "Fail")

print("Test case 6")
l = [1, 2, 3]       # (1, 3) 
print ("Pass" if ((1, 3) == get_min_max(l)) else "Fail")