def solution(x, y):
    ''' Returns the number of steps needed to produce the input given rules.
    Main idea: the problem is equivalent to find the series of elementary 
    row-additions, which form the matrix taking  [1,1] to [x,y] by left 
    multiplication (if it exists).
        - We compute the final transformation matrix (using Bezout coefficients)
        - We then iteratively find at each step what is the last row-addition
        - The number of iterations is the answer
        (More details inside code)
    '''

    ## Helper functions
    def extended_gcd(a, b):
        ''' Extended Euclidean algorithm. 
        Returns Bezout coefficients and GCD of integers a,b.
        '''
        s = 0
        old_s = 1
        t = 1
        old_t = 0
        r = b
        old_r = a
        
        while r != 0:
            quotient = old_r / r
            old_r, r = r, (old_r-quotient*r)
            old_s, s = s, (old_s-quotient*s)
            old_t, t = t, (old_t-quotient*t)
        
        gcd = old_r
        return old_s, old_t, gcd

    #Preprocessing
    M=int(x)
    F=int(y)

    # At each step, we have one of the two possibilities:
    # |M_{k+1}| = |M_k+F_k|   OR  |M_{k+1}| = |M_k    |
    # |F_{k+1}|   |    F_k|       |F_{k+1}|   |M_k+F_k|
    # Equivalently, if we note B_k = [M_k,B_k].T:
    # B_{k+1} = |1 1|*B_k     OR  B_{k+1} = |1 0|*B_k
    #           |0 1|                       |1 1|
    # when B_0 = [1,1].T
    # We denote the two matrices respectively C and C.T. Their determinants are 1.
    # This means that essentialy we are looking for a matrix A which is the 
    # successive multiplication, in some order, of C and C.T.
    # This matrix fulfills three conditions: 
    #       (1) A * [1,1].T = [x,y].T
    #       (2) det(A) = det(C)*det(C.T)*... = 1
    #       (3) All elements of A are nonnegative integers.
    
    ## First step : find the matrix A
    # When taking all conditions, we conclude that the first element a11 fulfills:
    #       a11 * F = 1 mod M
    # This is a linear congruence equation that can be solved using Bezout 
    # coefficients, and only if gcd(M,F)==1 (see https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
    # We compute the Bezout coefficients
    _,s,gcd = extended_gcd(M, F)

    if gcd!=1:
        return 'impossible'

    # Furthermore, since a12 = M-a11, this means that 0<a11<=M, therefore:
    a11 = s%M if s%M>0 else M
    # We compute the other elements by substituting:
    a12 = M - a11
    a21 = (F*a11-1)/M
    a22 = F - a21
    # All elements are nonnegative
    # Build matrix:
    A = [[a11,a12],[a21,a22]]

    ## Second step : find decomposition to product of C and C.T.
    # At each step we determine what step we can take - substracting the first
    # row by the second or vice-versa. We compare the two rows, choose the option
    # which will give nonnegative results, and determine how many times we can 
    # perform the operation. The number of times is added to the counter.

    #Init counter
    count = 0
    
    while A != [[1,0],[0,1]]: #so long as A!=I
        d0 = A[0][0]-A[1][0]
        d1 = A[0][1]-A[1][1]
        if (d0>=0) and (d1>=0): #first row - second row
            #floor division is implicit in python2
            k0 = A[0][0]/A[1][0] if A[1][0]>0 else float('Inf') 
            k1 = A[0][1]/A[1][1] if A[1][1]>0 else float('Inf')
            k = min(k0,k1)
            A[0][0] -= k * A[1][0]
            A[0][1] -= k * A[1][1]
            count+=k
        elif (d0<=0) and (d1<=0): #second row - first row
            k0 = A[1][0]/A[0][0] if A[0][0]>0 else float('Inf')
            k1 = A[1][1]/A[0][1] if A[0][1]>0 else float('Inf')
            k = min(k0,k1)
            A[1][0] -= k * A[0][0]
            A[1][1] -= k * A[0][1]
            count+=k
        else: #not consistent, no solution
            return 'impossible'
    
    return str(count)


# print(solution('1','10000000000000000000000000000'))