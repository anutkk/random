from sys import setrecursionlimit

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

    def matmul(A, B):
        ''' Multiply two 2*2 matrices and returns result.
        '''
        C = [[0,0],[0,0]]
        for i in range(2):
            for j in range(2):
                total = 0
                for ii in range(2):
                    total += A[i][ii] * B[ii][j]
                C[i][j] = total
        return C

    def decomposeMatrix(A, count=0):
        ''' Recursively decompose matrix to product of Cinv and CinvT (defined 
        later in the outer function) by taking all paths and refuting them recursively.
        '''
        # Base - if identity then we got to the goal
        if A == [[1,0],[0,1]]:
            return count
        # If one of the elements is negative then the path is wrong
        if (A[0][0]<0) or (A[0][1]<0) or (A[1][0]<0) or (A[1][1]<0):
            return -1
        # If we got here there is still hope
        count+=1
        # Test first option
        A0 = matmul(A,solution.Cinv)
        count0 = decomposeMatrix(A0, count=count)
        if count0<0: #if invalid go the other way
            A1 = matmul(A,solution.CinvT)
            count1 = decomposeMatrix(A1, count=count)
            if count1<0: #if invalid too then the path is wrong
                return -1
            else: #CinvT is okay
                return count1
        else: #Cinv is okay
            return count0


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

    # Furthermore, since a12 = M-a11, this means that a11<M, therefore:
    a11 = s%M if s%M>0 else M
    # We compute the other elements by substituting:
    a12 = M - a11
    a21 = (F*a11-1)/M
    a22 = F - a21
    # All elements are nonnegative
    # Build matrix:
    A = [[a11,a12],[a21,a22]]

    ## Second step : find decomposition to product of C and C.T.
    # We recursively multiply (on the right) A by the inverses of C and C.T.
    # The right possibility is the answer with nonnegative elements all the way
    # to the identity matrix.

    #Define inverse matrices and init counter
    solution.Cinv =  [[1, -1] , [0 , 1]]
    solution.CinvT = [[1,  0] , [-1, 1]]
    
    #421 is the maximum number of steps for the maximum value 10**50
    # (since the maximum values are obtained though Fibonacci and fib(421)>10**50)
    setrecursionlimit(421+100) 
    count = decomposeMatrix(A)
    
    return str(count)
