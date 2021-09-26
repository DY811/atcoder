n = int(input())
a = list(map(int, input().split())) 

x = [[0]*10 for _ in range(n)] 

mod = 998244353

x[0][a[0]] = 1

for i in range(1,n):
    for j in range(10):
        x[i][(j+a[i])%10] += x[i-1][j]%mod
        x[i][(j*a[i])%10] += x[i-1][j]%mod
    

for i in range(10):
    print((x[n-1][i])%mod)