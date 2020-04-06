import numpy as np
import solution
reload(solution)
import time
import sys

from itertools import combinations
# Trivial solution - backtracking
def trivial_solution(l):
    candidates = combinations(l, 3)
    def is_lucky((x,y,z)):
        return (y%x==0) and (z%y==0)
    count = 0
    for c in candidates:
        count += is_lucky(c)
    return count

number_of_tests = 10000
toolbar_width = 10
# setup toolbar
sys.stdout.write("[%s]" % (" " * toolbar_width))
sys.stdout.flush()
sys.stdout.write("\b" * (toolbar_width+1))

for i in xrange(number_of_tests):
    if (i+1)%(number_of_tests/toolbar_width)==0:
        sys.stdout.write("-")
        sys.stdout.flush()
    N = np.random.randint(2,25)
    l_np = np.sort(np.random.randint(1, 1e6, size=(N,)))
    l = l_np.tolist()
    sol = solution.solution(l)
    ref = trivial_solution(l)
    assert sol==ref

