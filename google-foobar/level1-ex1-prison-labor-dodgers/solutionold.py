from __future__ import division

#product method with numpy
def prod_np(x,y):
    ''' Returns one element which is in y but not in x (or vice-versa).
    Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    '''
    #treat special zero case
    zeros_in_x = x.count(0)
    zeros_in_y = y.count(0)
    if zeros_in_x!=zeros_in_y:
        return 0
    else:
        x = filter(lambda a: a != 0, x)
        y = filter(lambda a: a != 0, y)
    
    #special case: if all common elements were zero (equivalently if one list is empty)
    if not x:
        return y[0]
    elif not y:
        return x[0]

    import numpy as np
    #compute product of each list
    xprod = np.prod(np.array(x,dtype=np.float64))
    yprod = np.prod(np.array(y,dtype=np.float64))

    #divide
    candidate1 = xprod/yprod
    candidate2 = yprod/xprod
    if (abs(candidate1)>1):
        return int(candidate1)
    else:
        return int(candidate2)

#histogram using collections.counter
def hist_col(x,y):
    ''' Returns one element which is in y but not in x (or vice-versa).
    Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    '''
    #build histograms
    from collections import Counter
    xhist = Counter(x)
    yhist = Counter(y)

    #substract
    subhist1 = xhist-yhist
    subhist2 = yhist-xhist

    #there should remain only one item (check?)
    if len(subhist1)==0:
        return subhist2.keys()[0]
    else:
        return subhist1.keys()[0]


#histogram manually
def hist_man(x,y):
    ''' Returns one element which is in y but not in x (or vice-versa).
    Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    '''

    max_length = 99
    intlims = (-1000,1000)
    offset = intlims[0]
    #init histogram
    histogram = [0]*(intlims[1]-intlims[0]+1)
    if len(y)>len(x): #searched term is in y
        for x1 in x:
            histogram[x1-offset] += 1
        for y1 in y:
            histogram[y1-offset] -= 1
            if histogram[y1-offset]==-1:
                return y1
    else: #searched term is in x
        for y1 in y:
            histogram[y1-offset] += 1
        for x1 in x:
            histogram[x1-offset] -= 1
            if histogram[x1-offset]==-1:
                return x1

# product method with filtering on the run
def prod_nofil(x,y):
    ''' Returns one element which is in y but not in x (or vice-versa).
    Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    
    Basic idea: we multiply all values in the arrays, then divide the two results.
    Supposing the input is valid, this should give the integer which is in one array but not in the other. In the case the result is not an integer, we return the inversed division.
    Special case (0 in one of the lists) is handled separately.
    Note: this works only because Python uses "unlimited integers".
    '''
    #treat special zero case
    zeros_in_x = x.count(0)
    zeros_in_y = y.count(0)
    if zeros_in_x!=zeros_in_y:
        return 0

    #compute product of each list (and filter zeroes on the run)
    def prod(a,b):
        if a==0:
            return b
        if b==0:
            return a
        return a*b
    xprod = reduce(prod, x)
    yprod = reduce(prod, y)

    #special case: if all common elements were zero (equivalently if one list is empty)
    if xprod==0:
        return yprod
    elif yprod==0:
        return xprod

    #divide in possible orders
    candidate1 = xprod/yprod
    candidate2 = yprod/xprod

    #choose appropriate solution
    if (abs(candidate1)>1): #TODO: better condition?
        return int(candidate1)
    else:
        return int(candidate2)

# product method with lambda filter
def prod_fil(x,y):
    ''' Returns one element which is in y but not in x (or vice-versa).
    Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    '''
    #treat special zero case
    zeros_in_x = x.count(0)
    zeros_in_y = y.count(0)
    if zeros_in_x!=zeros_in_y:
        return 0
    else:
        x = filter(lambda a: a != 0, x)
        y = filter(lambda a: a != 0, y)

    #special case: if all common elements were zero (equivalently if one list is empty)
    if not x:
        return y[0]
    elif not y:
        return x[0]

    #compute product of each list
    xprod = reduce(lambda a, b: a*b, x)
    yprod = reduce(lambda a, b: a*b, y)

    #divide
    candidate1 = xprod/yprod
    candidate2 = yprod/xprod
    if (abs(candidate1)>1):
        return int(candidate1)
    else:
        return int(candidate2)

# product method by replacing zero by some other number
# def prod_rep(x,y):
#     ''' Returns one element which is in y but not in x (or vice-versa).
#     Inputs: x,y - lists of integers (1<=length<=99). Integer range: [-1000,1000]
    
#     Basic idea: we multiply all values in the arrays, then divide the two results.
#     Supposing the input is valid, this should give the integer which is in one array but not in the other. In the case the result is not an integer, we return the inversed division.
#     Special case (0 in one of the lists) is handled separately.
#     Note: this works only because Python uses "unlimited integers".
#     '''
#     #compute product of each list (and filter zeroes on the run)
#     def prod(a,b):
#         a = 1001 if a==0 else a
#         b = 1001 if b==0 else b
#         return a*b
#     xprod = reduce(prod, x)
#     yprod = reduce(prod, y)

#     #divide in possible orders
#     candidate1 = xprod/yprod
#     candidate2 = yprod/xprod

#     #if zero adapt
#     candidate1 = 0 if candidate1==1001 else candidate1
#     candidate2 = 0 if candidate2==1001 else candidate2

#     #choose appropriate solution
#     if (abs(candidate1)>1): #TODO: better condition?
#         return int(candidate1)
#     else:
#         return int(candidate2)