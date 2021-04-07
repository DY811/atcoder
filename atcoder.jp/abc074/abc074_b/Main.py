# abc 074 B Collecting Balls
n = int(input())
k = int(input())
x = list(map(int,input().split()))
d = 0

for i in range(n):
    if x[i] >= k/2:
        d += (k - x[i])*2
    else:
        d += x[i]*2
print(d)