from __future__ import division
import numpy as np
import solution
from fractions import Fraction

import time
import sys

number_of_tests = 1000000
toolbar_width = 10
# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in xrange(number_of_tests):
    if (i+1)%(number_of_tests/toolbar_width)==0:
        sys.stdout.write("-")
        sys.stdout.flush()
    N = np.random.randint(2,21)
    pegs_np = np.sort(np.random.randint(1, 10001, size=(N,)))
    pegs = pegs_np.tolist()
    dpegs = np.diff(pegs_np)

    sol = solution.solution(pegs)
    if sol[0]==-1 and sol[1]==-1:
        if N==2:
            assert dpegs[0]<1.5
            continue
        A = np.zeros((N-1,N-1))
        A[0][0] = 2
        A[0][1] = 1
        A[N-2][0] = 1
        A[N-2][N-2] = 1
        for i in range(1,N-2):
            A[i][i] = 1
            A[i][i+1] = 1
        try:    
            x = np.linalg.solve(A, dpegs)
        except np.linalg.LinAlgError:
            continue
        assert x[0]<1.0
    else:
        r1 = Fraction(sol[0], sol[1])
        r = r1
        for d in dpegs:
            r = d - r
        assert r1/r==2