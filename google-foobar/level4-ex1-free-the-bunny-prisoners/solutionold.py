from itertools import combinations

def solution(num_buns, num_required):
    
    # num_buns = 5
    # num_required = 3

    # def comb(n, k):
    #     c = 1
    #     for i in range(1,k):
    #         c *= ((n+1-i)/i)
    #     return c

    # num_unique_keys = comb(num_buns, num_required-1)
    # keys_per_bunny = comb(num_buns-1, num_required-1)
    # bunnies_per_key = num_buns - num_buns + 1

    r = [ [] for i in xrange(num_buns) ]

    for (kn,c) in enumerate(combinations(range(num_buns), num_buns-num_required+1)):
        for g in c:
            r[g].append(kn)

    return r