#!/usr/bin/python3
"""place hold
"""

def max_integer(lst=[]):
    """return max
        If the list is empty, the function returns None
    """
    
    if len(lst) == 0:
        return None
    
    maxi = lst[0]
    for i in lst[1:]:
        if i > maxi:
            maxi = i
    
    return maxi
