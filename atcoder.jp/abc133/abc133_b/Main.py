import math
n,d = map(int,input().split())
x = [list(map(int,input().split())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        #print(i,j)
        s = 0
        for k in range(d):
            s += (x[i][k]-x[j][k])**2
        s = s**(1/2)
        if s.is_integer():
            cnt += 1
print(cnt)
#y = 1.00
#print(y.is_integer())