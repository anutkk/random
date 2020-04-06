from itertools import combinations

def solution(num_buns, num_required):
    """
    Returns keys distribution among num_buns bunnies so that any subset of num_required can open the locks (but not less).
    Intuition: 
        - Each key must be given to a subset of (at least) (B-L+1) bunnies. 
        Otherwise, there would be L bunnies without the key.
        - By symmetry every key needs be given to the same number of bunnies.
        - Any subset of (B-L+1) bunnies must have a key which no-one else has.
        Otherwise, any (complemental) subset of (L-1) bunnies will have all the keys. 
        - Thus we just need to find all subsets of (B-L+1) bunnies and attribute to
        each subset a unique key.
    Combinatorical formulation: 
        - There are overall C(B,L) subsets of bunnies.
        - Giving one key to one bunny covers C(B-1,L-1) subsets, the second key
        covers C(B-2,L-1) *more* subsets, the third C(B-3,L-1) subsets and so on.
        - According to the Hockey-stick identity, this means that every key 
        (by symmetry) needs be given to (B-1)-(L-1)+1 = B-L+1 bunnies.
        - We then just need to iterate over all subsets of (B-L+1) bunnies out of B
         and give a different key to every subset.
    """
    # Initialize result array
    r = [ [] for _ in xrange(num_buns) ]

    # Per each key, how many bunnies must get it:
    bunnies_per_key = num_buns - num_required + 1

    # Loop over subsets of bunnies (which are already lexicographically sorted)
    for (kn,c) in enumerate(combinations(range(num_buns), bunnies_per_key)):
        for b in c: #for each bunny in the current distribution
            r[b].append(kn) #add the key to the bunny

    return r