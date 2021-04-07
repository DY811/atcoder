# タップの個数と必要な数
a, b = map(int, input().split())

import math

if b == 1:
    print(0)
elif a >= b:
    print(1)    
else:
    print(math.ceil((b-1)/(a-1)))