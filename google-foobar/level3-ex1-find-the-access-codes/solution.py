from sys import setrecursionlimit
def solution(l):
    ''' Returns number of "lucky triples" in l. l is a list of positive integers.
    Main idea: for each element E in the list:
        - compute by tailless recursion how many elements before E divide E
        - loop over E's own divisors
        - if one of them has itself X divisors, we found X new lucky triples
        - We add X to the total count
    Note: the recursion depth is (approx.) the length of the input. 
        This is reasonable since len(l)<=2000 and since the recursion is tailless 
        (although Python generally does not optimize tailless recursion).
    '''
    # Set as needed the maximum recursion limit
    setrecursionlimit(len(l)+100)

    #Initialize nonlocal array which will store the number of preceding divisors
    solution.divisors_before = [0]*len(l)

    # Recursion function
    def compute(subl, idx, count=0):
        ''' Computes each element's number of divisors before itself 
        and the count of lucky triples.
        '''
        # Base case - first element of list
        if len(subl)==1:
            solution.divisors_before[idx] = 0
            return 0
        
        # Compute results for the list minus the last element
        pivot = subl[-1]
        count = compute(subl[:-1], idx=idx-1, count=count)
        
        # Compute number of divisors of last element and update count
        new_number_of_divisors = 0
        for c, number_of_divisors in zip(subl[:-1], solution.divisors_before[:idx]):
            if pivot%c==0:
                new_number_of_divisors+=1
                count+=number_of_divisors
        
        solution.divisors_before[idx] = new_number_of_divisors 
        return count

    return compute(l, count=0, idx=len(l)-1)