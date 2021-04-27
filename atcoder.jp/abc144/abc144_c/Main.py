n = int(input())
# a*b = b*aなのでa<=bとして探索
# sqrt(n)**2 = nなので、aはsqrt(n)まで探索
# a+b-2が歩数

import math
step = n-1 #a=1,b=nを仮の答えと置いておく

for i in range(1,int(math.sqrt(n))+1):
    if n%i == 0:
        a = i
        b = n//i
        step = min(step,(a+b-2))
        #print(a,b,step)
print(step)