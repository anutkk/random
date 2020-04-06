def solution(n):
    """
    Returns minimum number of steps (divide by 2, +1,-1) to get to 1.
    Main idea: recursively divide by 2 as many steps as possible. 
    When impossible, add or substract 1  - choose the option which leads 
    faster to 1, and divide.
    """
    def factor2(x):
        """Divides x by 2 as many times as possible."""
        count = 0
        while x%2==0 :
            x = x/2
            count+=1
        return x, count

    n = int(n)
    count = 0
    while n>1:
        # print(n)
        if n%2==0: #n even, divide by 2 as long as possible
            n, c = factor2(n)
            count+=c
        else: #n odd, add and substract and compare options
            if n==3:
                n = 1
                count += 2
            else:
                count+=1
                if (n-1)%4==0:
                    n, c = factor2(n-1)
                else:
                    n, c = factor2(n+1)
                count += c
    return count