n = int(input())
c = list(map(int,input().split()))
c.sort()
#print(c)
cnt = 1
for i in range(n):
    tmp = c[i]-i
    multi = tmp%(10**9+7)
    cnt *= multi
    cnt = cnt%(10**9+7)
print(cnt)