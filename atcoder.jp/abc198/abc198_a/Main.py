import itertools

n = int(input())
cc = tuple(range(n))
#print(cc)
cnt = 0
for i in range(1,n): #1 to n-1
    d = list(itertools.combinations(cc, n))
    cnt += len(d)
print(cnt)