import itertools
import bisect

n,k = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
b = sorted(a, key = lambda x:x[0])

mura = []
yen = []
for i in range(n):
    mura.append(b[i][0])
    yen.append(b[i][1])

ac = list(itertools.accumulate(yen))
ac = ac+[0]
#print(ac)

left = 0
right = k
tmp = k
while tmp > 0:
    idx = bisect.bisect_right(mura,k)
    #print(idx)
    tmp = ac[idx-1]-ac[left-1]
    k += tmp
    left = idx
print(k)