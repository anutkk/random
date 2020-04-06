from __future__ import division
import numpy as np
import solution
from fractions import Fraction

import time
import sys

def otherSolution(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]

    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])

    if (arrLength > 2):
        for index in xrange(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()

    # now that we have the radius of the first gear, we should again check the input array of pegs to verify that
    # the pegs radius' is atleast 1.
    # since for valid results, LastGearRadius >= 1 and FirstGearRadius = 2 * LastGearRadius
    # thus for valid results FirstGearRadius >= 2

    if FirstGearRadius < 2:
        return [-1,-1]

    currentRadius = FirstGearRadius
    for index in xrange(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

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
    # dpegs = np.diff(pegs_np)

    sol = solution.solution(pegs)
    other_sol = otherSolution(pegs)
    assert (sol[0]==other_sol[0] and sol[1]==other_sol[1]), str(pegs)
