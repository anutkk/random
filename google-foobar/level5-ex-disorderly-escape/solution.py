from fractions import Fraction
from collections import Counter
from itertools import product

def solution(w, h, s):
    """
    Hellish question. Use Burnside lemma and other tricks.
    """
    class Monomial:
        def __init__(self, coeff, counter=None, indices=None, powers=None):
            self.coeff = coeff
            if counter is None:
                self.vals = Counter( dict(zip(indices, powers))) 
            else:
                self.vals = counter
        
        def __mul__(self, other):
            ncoeff = self.coeff * other.coeff
            nvals = self.vals + other.vals
            return Monomial(coeff = ncoeff, counter=nvals)
        
        def __eq__(self, other):
            return (self.vals==other.vals)
        
        def __ne__(self, other):
            return (self.vals!=other.vals)
        
        def __str__(self):
            s = str(self.coeff) if self.coeff!=1 else ''
            for idx, power in self.vals.items():
                ps = ('^'+str(power)) if power!=1 else ''
                if s=='':
                    s = 'x_'+str(idx)+ps
                else:
                    s += '*'+'x_'+str(idx)+ps
            return s
        
        def __repr__(self):
            return self.__str__()

        def __add__(self, other):
            if self!=other:
                raise ValueError('Not same exponents')
            return Monomial(coeff = self.coeff+other.coeff, counter=self.vals)
        
        def evaluate(self, value):
            prod = self.coeff
            for exp in self.vals.values():
                prod *= value**exp
            return prod

    class Polynomial:
        def __init__(self, monomials=None, const=Fraction(1)): #init to 1
            if monomials is None:
                mon = Monomial(const, counter=Counter())
                self.monomials = [mon]
            else:
                self.monomials = monomials
                
        def __mul__(self, other):
            nmons = []
            for mon1, mon2 in product(self.monomials, other.monomials):
                nmon = mon1*mon2
                if nmon.coeff==0:
                    continue
                if not nmon in nmons:
                    nmons += [nmon]
                else:
                    nmons[nmons.index(nmon)] *= nmon
            return Polynomial(nmons)
        
        def __add__(self, other):
            nmons = self.monomials
            for nmon in other.monomials:
                if not nmon in nmons:
                    nmons += [nmon]
                else:
                    nmons[nmons.index(nmon)] += nmon
            return Polynomial(nmons)

        def evaluate(self, value):
            sum = 0
            for mon in self.monomials:
                sum += mon.evaluate(value)
            return sum
        
        def __str__(self):
            s = ''
            for mon in self.monomials:
                if mon.coeff!=0:
                    if s=='':
                        s = str(mon)
                    else:
                        s+= ' + ' + str(mon)
            return s
        
        def __repr__(self):
            return self.__str__()

    def cycle_index(n):
        """Computes cycle index of symmetric group S_n
        Returns instance of Polynomial
        """
        if n==0:
            return Polynomial(const=1)
        cycle_index_n = Polynomial(const=0)
        for l in range(1, n+1):
            cycle_index_n_l = cycle_index(n-l)
            polycoeff = Polynomial([Monomial(
                                            Fraction(1,1), 
                                            indices=[l], 
                                            powers=[1])
                                    ])
            cycle_index_n += polycoeff * cycle_index_n_l
        maincoeff = Polynomial(const = Fraction(1,n))
        return maincoeff*cycle_index_n
    
    def gcd(a,b):
        """Compute the greatest common divisor of a and b"""
        while b > 0:
            a, b = b, a % b
        return a
    
    p1 = cycle_index(w)
    p2 = cycle_index(h)

    tot = 0

    for term1, term2 in product(p1.monomials, p2.monomials):
        res = term1.coeff * term2.coeff
        for (l1,p1), (l2,p2) in product(term1.vals.items(), term2.vals.items()):
            res *= (s**gcd(l1, l2))**(p1*p2)
        tot += res
    
    return str(int(tot))

# solution(2, 2, 2) == '7'
# solution(2, 3, 4) == '430'

#see:
# https://rellek.net/book/ch_polya.html
# https://math.stackexchange.com/questions/22159/how-many-n-times-m-binary-matrices-are-there-up-to-row-and-column-permutation
# https://mathworld.wolfram.com/SymmetricGroup.html
# https://mathworld.wolfram.com/CycleIndex.html

        
        
