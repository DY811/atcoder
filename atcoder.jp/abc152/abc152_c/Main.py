n = int(input())
p = list(map(int,input().split()))

m = p[0]
cnt = 1 # at least one

for i in range(1,len(p)):
    if p[i] <= m:
        cnt += 1
        m = p[i]
print(cnt)