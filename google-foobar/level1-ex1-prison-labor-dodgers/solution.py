def solution(x,y):
    ''' Returns one element which is in y but not in x (or vice-versa).
    Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    
    Basic idea: we compute the product of each array's elements, then divide 
    the longer list's product by the shorter list's product.
    This gives the integer which is in one array but not in the other. 
    Special case (0 in one of the lists) is handled separately.
    Note: this works only because Python uses "unlimited integers", but we 
    checked the edge case 1000**99
    '''
    # input validation
    assert isinstance(x, list) and isinstance(y, list), 'Inputs must be lists.'
    assert abs(len(x)-len(y))==1, 'One list should be longer than the other by 1.'
    assert all([isinstance(e, int) for e in x]), 'All elements must be integers.'
    assert all([isinstance(e, int) for e in y]), 'All elements must be integers.'

    # treat special zero case
    zeros_in_x = x.count(0)
    zeros_in_y = y.count(0)
    if zeros_in_x!=zeros_in_y: # in case the searched integer is zeo
        return 0
    else: # otherwise filter out the zeroes
        x = filter(lambda a: a != 0, x)
        y = filter(lambda a: a != 0, y)

    # special case: if all common integers were zero and one list is empty
    if not x:
        return y[0]
    elif not y:
        return x[0]

    # compute product of each list
    xprod = reduce(lambda a, b: a*b, x)
    yprod = reduce(lambda a, b: a*b, y)

    # perform division in the correct order and return result 
    if len(x)>len(y): # O(1) operation
        return int(xprod/yprod)
    else:
        return int(yprod/xprod)

# This solution was benchmarked againt the following other options:
#   - Same but with filtering on the run in reduce
#   - Same but with replacing zeros by 1001 on the run
#   - Same but using numpy.prod()
#   - Histogram using collections.Counter
#   - Histogram manual implementation
# This solution was chosen because it is the most elegant and readable and 
# because other methods gave similar or worst results (at best - slight 
# speedup in special cases).
# Moreover, it is less memory intensive than an histogram (~100B to store 
# product vs. ~2000B for an histogram).