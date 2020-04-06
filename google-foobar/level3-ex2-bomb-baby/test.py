#%%
# from itertools import product
# from math import sqrt, floor, ceil, log
# def trivial_solution(x, y):
#     def extended_gcd(a, b):
#         s = 0
#         old_s = 1
#         t = 1
#         old_t = 0
#         r = b
#         old_r = a
        
#         while r != 0:
#             quotient = old_r / r
#             old_r, r = r, (old_r-quotient*r)
#             old_s, s = s, (old_s-quotient*s)
#             old_t, t = t, (old_t-quotient*t)
        
#         gcd = old_r
#         return old_s, old_t, gcd


#     def matmul(A, B): #multiply two 2*2 matrices
#         C = [[0,0],[0,0]]
#         for i in range(2):
#             for j in range(2):
#                 total = 0
#                 for ii in range(2):
#                     total += A[i][ii] * B[ii][j]
#                 C[i][j] = total
#         return C
    

#     M=int(x)
#     F=int(y)

#     _,_,gcd = extended_gcd(M, F)
#     if gcd!=1:
#         return 'impossible'

#     C0 = [[1,1], [0,1]]
#     C1 = [[1,0], [1,1]]

#     #compute maximum number of steps (result is constant = 241)
#     PHI = 0.5*(1+sqrt(5))
#     MAXX = 10**50
#     MAXN = int(ceil(log(sqrt(5)*MAXX)/log(PHI))) # gives 241, since fib(241)>10**50

#     # #compute minimum number of steps, supposing we got to the minimum number by the fastest way, alternating the methods of reproduction
#     minx = min(M,F)
#     minn = int(floor(log(sqrt(5)*minx)/log(PHI)))

#     #TRIVIAL SOLUTION
#     for n in range(minn,MAXN):
#         for p in product([C0, C1], repeat=n): 
#             r = reduce( lambda a,b: matmul(a,b) ,  p)
#             if (r[0][0]+r[0][1])==M and (r[1][0]+r[1][1])==F:
#                 return str(n)
    
#     return 'impossible'

import numpy as np
import solution
reload(solution)
import time
import sys
import random
import solutionoverkill


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


C0 = np.matrix([[1,1], [0,1]])
C1 = C0.T.tolist()
C0 = C0.tolist()
Cinv = np.matrix([[1,-1],[0,1]])


number_of_tests = 100000
toolbar_width = 100
# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))
for i in xrange(number_of_tests):
    if (i+1)%(number_of_tests/toolbar_width)==0:
        sys.stdout.write("-")
        sys.stdout.flush()
    N = random.randint(1, 10**50)
    Nbin = bin(N)[2:]
    ref = len(Nbin)
    A = [[1,0],[0,1]]
    for b in Nbin:
        if b=='0':
            A = matmul(A,C0)
        else:
            A = matmul(A,C1)

    x = str(A[0][0]+A[0][1])
    y = str(A[1][0]+A[1][1])
    sol = solution.solution(x,y)
    # sol = solutionoverkill.solution(x,y)
    if sol=='impossible':
        raise ValueError(Nbin)
    assert int(sol)==ref, Nbin