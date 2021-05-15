import itertools
import bisect
n = int(input())
a = list(map(int,input().split()))
length = sum(a)
half = length/2
acc = list(itertools.accumulate(a))
#print(acc)
pos = bisect.bisect(acc,half)
#print(pos)
delta_1 = abs(acc[pos-1]-half)
delta_2 = abs(acc[pos]-half)
if half in acc:
    print(0)
else:
    print(int(min(delta_1,delta_2)//0.5))
    