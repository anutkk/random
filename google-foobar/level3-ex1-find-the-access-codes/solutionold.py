from sys import setrecursionlimit
def solution(l):
    ''' Returns number of "lucky triples" in l. l is a list of positive integers.
    Main idea: for each element E in the list:
        - compute by recursion how many elements before E divide E
        - loop over E's own divisors
        - if one of them has itself X divisors, we found X new lucky triples
        - We add X to the total count
    Note: the recursion depth is (approx.) the length of the input. 
        This is reasonable since len(l)<=2000 and since the recursion is tailless (although Python generally does not optimize it)
    '''
    # Set as needed the maximum recursion limit
    setrecursionlimit(len(l)+100)

    # Recursion function
    def compute(subl,count=0):
        ''' Computes each element's number of divisors before itself 
        and the count of lucky triples.
        '''
        # Base case - first element of list
        if len(subl)==1:
            return [0], 0
        
        # Compute results for the list minus the last element
        pivot = subl[-1]
        new_number_of_divisors = 0
        divisors_before, count = compute(subl[:-1], count=count)

        # Compute number of divisors of last element and update count
        for c,number_of_divisors in zip(subl[:-1], divisors_before):
            if pivot%c==0:
                new_number_of_divisors+=1
                count+=number_of_divisors
        return divisors_before+[new_number_of_divisors] , count

    _, final_count = compute(l, count=0)
    return(final_count)
