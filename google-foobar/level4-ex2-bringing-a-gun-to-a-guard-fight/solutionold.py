from __future__ import division
from math import ceil, atan2
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def solution(dimensions, your_position, guard_position, distance):
    dx = guard_position[0] - your_position[0]
    dy = guard_position[1] - your_position[1]
    if (dx==0) and (dy==0):
        return 0
    Lx = dimensions[0]
    Ly = dimensions[1]
    x0 = your_position[0]
    y0 = your_position[1]
    D2 = distance**2

    fig,ax = plt.subplots(1)
    rect = mpatches.Rectangle((0,0),Lx,Ly,linewidth=1,edgecolor='r',facecolor='none')
    ax.add_patch(rect)
    # ax.plot(x0,y0, 'k.')
    # ax.plot(guard_position[0], guard_position[1], 'r.')
    circle1 = plt.Circle((x0, y0), distance, ec='b', fc=None, fill=False)
    ax.add_artist(circle1)
    ax.set_aspect('equal')
    plt.xlim(x0-1.1*distance, x0+1.1*distance)
    plt.ylim(y0-1.1*distance, y0+1.1*distance)

    k0lim = int(ceil((distance-dx)/(2*Lx)))
    k1lim = int(ceil((distance-dy)/(2*Ly)))

    k0s = xrange(-k0lim, k0lim+1)
    k1s = xrange(-k1lim, k1lim+1)
    c = 0
    for k0, k1 in product(k0s, k1s):
        for sign0, sign1 in product([-1,+1],[-1,+1]):
            gx = 2*k0*Lx + sign0*guard_position[0]
            gy = 2*k1*Ly + sign1*guard_position[1]
            x = 2*k0*Lx + sign0*your_position[0]
            y = 2*k1*Ly + sign1*your_position[1]
            # print str(gx)+' '+str(gy)
            if ( ((gx-x0)**2+(gy-y0)**2) <= D2 ):
                if abs( atan2(gx-x0,gy-y0) - atan2(x-x0,y-y0)  )>1e-3:
                    ax.plot([x0,gx],[y0,gy], 'b-')
                    c += 1
                    ax.plot(x,y, 'g.')
                    ax.plot(gx,gy, 'g*')
                else:
                    # print (gx-x0)*(y-y0) - (gy-y0)*(x-x0)
                    pass
                    ax.plot(x,y, 'b.')
                    ax.plot(gx,gy, 'b*')
            else:
                pass
                ax.plot(x,y, 'r.')
                ax.plot(gx,gy, 'r*')        
                
    
    return c
# r1 = solution([3,2], [1,1], [2,1], 4)
# assert  r1== 7
# # print '-----'
# r2 = solution([300,275], [150,150], [185,100], 500)
# assert  r2== 9, str(r2)
r3 = solution([2,5], [1,2], [1,4], 11)
assert r3==27, str(r3)
r4 = solution([42,59], [34,44], [6,34], 5000)   