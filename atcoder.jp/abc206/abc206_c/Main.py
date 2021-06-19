import collections
n = int(input())
a = list(map(int,input().split()))
c = collections.Counter(a)
l = list(c.values())
ans = 0
for i in range(len(l)):
    ans += l[i]*(l[i]-1)//2
print(int(n*(n-1)//2-ans))

