from fractions import Fraction

def solution(pegs):
    ''' pegs is a list of distinct positive integers.
    Main idea: model the problem as linear system, and use Cramer's rule.
    '''
    #Determinant helper function - m is list of lists
    #slightly optimized for sparse matrices
    def det(m):
        #base case for 2x2 matrix
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            if m[0][c]==0:
                continue
            minor = [row[:c] + row[c+1:] for row in (m[:0]+m[1:])]
            determinant += ((-1)**c)*m[0][c]*det(minor)
        return determinant

    #Build matrix
    N = len(pegs)-1
    A = [ [0]*N for _ in range(N) ]
    A[0][0] = 2
    A[0][1] = 1
    A[N-1][0] = 1
    A[N-1][N-1] = 1
    for i in range(1,N-1):
        A[i][i] = 1
        A[i][i+1] = 1

    Ai = A
    for j in range(N):
        Ai[j][0] = pegs[j+1] - pegs[j]

    detA = 1 if (N%2==0) else 3

    dpegs = [x1-x for x,x1 in zip (pegs[:-1], pegs[1:])]
    detAi = 0
    for i in range(len(dpegs)):
        detAi += ((-1)**i) * dpegs[i]

    result = Fraction(numerator=2*detAi, denominator=detA)
    if result.numerator < result.denominator:
        return [-1, -1]

    return [result.numerator, result.denominator]

#%%
#Build matrix
import numpy as np
pegs = np.random.randint(10001, size=(15,))
N = len(pegs)-1
A = np.zeros((N,N))
A[0][0] = 2
A[0][1] = 1
A[N-1][0] = 1
A[N-1][N-1] = 1
for i in range(1,N-1):
    A[i][i] = 1
    A[i][i+1] = 1

Ai = A.copy()
for j in range(N):
    Ai[j][0] = pegs[j+1] - pegs[j]

detA = 1 if (N%2==0) else 3
dpegs = [x1-x for x,x1 in zip (pegs[:-1], pegs[1:])]
detAi = 0
for i in range(len(dpegs)):
    detAi += ((-1)**i) * dpegs[i]

print(str(detA) +' ' + str(np.round(np.linalg.det(A))))
print(str(detAi) +' ' + str(np.round(np.linalg.det(Ai))))

# %%
