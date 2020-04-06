from fractions import Fraction

def solution(pegs):
    ''' pegs is a list of distinct positive integers.
    Main idea: model the problem as linear system, and use Cramer's rule.
    '''
    N = len(pegs)-1
    # Compute determinants (taking advange of bidiagonal matrices and confluant simplification - see https://en.wikipedia.org/wiki/Bidiagonal_matrix)
    detA = 1 if (N%2==0) else 3

    dpegs = [x1-x for x,x1 in zip (pegs[:-1], pegs[1:])]
    detAi = 0
    for i in range(len(dpegs)):
        detAi += ((-1)**i) * dpegs[i]
    
    result = Fraction(numerator=2*detAi, denominator=detA)
    if result.numerator < result.denominator:
        return [-1, -1]

    # ensure the following gears are valid
    r = Fraction(numerator=2*detAi, denominator=detA)
    for d in dpegs:
        r = d - r
        if r.numerator < r.denominator:
            return [-1, -1]

    return [result.numerator, result.denominator]
