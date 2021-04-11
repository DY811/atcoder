import math

r,x,y = map(int,input().split())
d = math.sqrt((x-0)**2+(y-0)**2)
#print(d)

if d%r == 0:
    print(int(d/r))
else:
    if d < r:
        print(int(2))
    else:
        sho = d//r
        print(int(sho+1))
