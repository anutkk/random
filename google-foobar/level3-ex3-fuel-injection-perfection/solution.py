def solution(n):
    """
    Returns minimum number of steps (divide by 2, +1,-1) to get to 1.
    Main idea:  divide by 2 as many steps as possible. 
    When impossible, add or substract 1  - choose the option which will allow to divide by 2 in the next iteration.
    Note: we could have also used bit operations, but this gives no improvement in time complexity and makes the code unreadable.
    """
    n = int(n)
    count = 0
    while n > 1:
        if n%2==0: #n even, divide by 2
            n = n>>1 #shift-left because a bit of bit operations is like okay (see what I did??)
            count += 1
        else: #n odd, add and substract and compare options
            #special case where substracting 2 times is shorter than dividing by 2 
            #(happens because ceil(log2(n))> (n-1) only for n=3)
            if n==3: 
                n = 1
                count += 2
            else:
                count+=1
                if n%4==1:
                    n -= 1
                else:
                    n += 1
    return count