# Floyd's algorithm
def solution(n, b):
    ''' Returns length of ending cycle of algorithm beginning with n in base b.
    Inputs: n - string representing initial number (2<=len(n)<=9)
            b - base of number (2<=b<=10)
    
    Main idea: we find some point inside the cycle using Floyd's cycle 
    detection algorithm.
    Then we count how many steps are needed to return to the same point.
    Memory complexity is O(1), time complexity is linear in the number of 
        possible ID values in the specific instance (and potentially sub-linear)
    Note: we implement the algorithm and base-b arithmetic with OOP. '''
    
    # Input validation
    assert isinstance(n,str) , 'n must be an integer.'
    assert isinstance(b,int) , 'n must be an integer.'

    # Class representing integer in arbitrary base
    # Implements needed operations: sort, substraction and non-equality
    class Integer:
        digits = ''
        base = 10
        def __init__(self, digits='0', base=10):
            self.base = base
            self.digits = digits
        
        # Returns instance with digits sorted (in desc/ascending order)
        def asc(self):
            asc_str = ''.join(sorted(self.digits))
            return Integer(asc_str, self.base)
        def desc(self):
            desc_str = ''.join(sorted(self.digits))[::-1]
            return Integer(desc_str, self.base)
        
        # Operators
        def __sub__(self, other): #substraction
            length = len(self.digits)
            self_base10 = int(self.digits, self.base)
            other_base10 = int(other.digits, self.base)
            result_base10 = self_base10 - other_base10
            result_str = Integer.numberToBase(result_base10, self.base)
            result = result_str.zfill(length)
            return Integer(result, self.base)
        def __ne__(self, other): #non-equality (!=)
            return (self.digits != other.digits)

        # Helper function to convert base10 number into arbitrary base
        @staticmethod
        def numberToBase(number, b):
            if number == 0:
                return '0'
            digits_str = ''
            while number:
                digits_str += str(int(number % b))
                number /= b
            return digits_str[::-1]

    def next_id(num):
        ''' Given an Integer instance, returns the next ID according to algorithm.
        '''
        x = num.desc()
        y = num.asc()
        z = x-y
        return z

    # Find a point in the cycle using Floyd's cycle detection algorithm
    # For reference on the algorithm: (https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
    n = Integer(n, b)
    p1 = next_id(n)
    p2 = next_id(p1)
    while p1 != p2:
        p1 = next_id(p1)
        p2 = next_id(next_id(p2)) 
    # p1 and p2 now contain a point in the cycle
    
    # Count how many steps are needed to return to the same point
    p2 = next_id(p1)
    cycle_length = 1
    while p2 != p1:
        p2 = next_id(p2)
        cycle_length += 1
    
    #Return result
    return cycle_length


# solution('210022', 3)