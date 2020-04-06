# That one works for sure

from __future__ import division
from math import floor, atan2
from itertools import product
from fractions import Fraction

def solution(dimensions, your_position, guard_position, distance):

    def gcd(a, b):
        """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a % b
        return a
    sign = lambda a: (a>0) - (a<0)

    dx = guard_position[0] - your_position[0]
    dy = guard_position[1] - your_position[1]
    if (dx==0) and (dy==0):
        return 0
    Lx = dimensions[0]
    Ly = dimensions[1]
    x0 = your_position[0]
    y0 = your_position[1]
    D2 = distance**2

    k0lim = int(floor((distance+x0+max(x0,guard_position[0]))/(2*Lx)))
    k1lim = int(floor((distance+y0+max(y0,guard_position[1]))/(2*Ly)))

    k0s = xrange(-k0lim, k0lim+1)
    k1s = xrange(-k1lim, k1lim+1)
    c = 0
    friendly_fire_directions = {}
    for k0, k1 in product(k0s, k1s):
        for sign0, sign1 in product([-1,+1],[-1,+1]):
            x = 2*k0*Lx + sign0*your_position[0]
            y = 2*k1*Ly + sign1*your_position[1]
            if ( ((x-x0)**2+(y-y0)**2) <= D2 ):
                if (x==x0) or y==y0:
                    continue
                gcd1 = abs(gcd(y-y0, x-x0))
                direction = ((x-x0)/gcd1, (y-y0)/gcd1)
                distance1 = (x-x0)**2+(y-y0)**2
                if not (direction in friendly_fire_directions) or (distance1<friendly_fire_directions[direction]):
                    friendly_fire_directions[direction] = distance1
    correct_directions = []
    for k0, k1 in product(k0s, k1s):
        for sign0, sign1 in product([-1,+1],[-1,+1]):
            gx = 2*k0*Lx + sign0*guard_position[0]
            gy = 2*k1*Ly + sign1*guard_position[1]
            x = 2*k0*Lx + sign0*your_position[0]
            y = 2*k1*Ly + sign1*your_position[1]
            if ( ((gx-x0)**2+(gy-y0)**2) <= D2 ):
                if gx==x0 or gy==y0: #for sure get killed if not original room
                    if (x==x0) and (y==y0): #original room
                        c += 1
                        correct_directions.append((sign(x-x0), sign(y-y0)))
                    continue
                gcd1 = abs(gcd(gy-y0, gx-x0))
                direction = ((gx-x0)/gcd1, (gy-y0)/gcd1)
                distance1 = (gx-x0)**2+(gy-y0)**2
                if (not (direction in friendly_fire_directions)) or (distance1<friendly_fire_directions[direction]):
                    if not (direction in correct_directions):
                        c += 1
                        correct_directions.append(direction)
    return c