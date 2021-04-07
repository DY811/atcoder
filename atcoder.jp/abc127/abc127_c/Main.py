n,m = map(int,input().split())
cnt = 0
max_L = 1
min_R = 10**5

for i in range(1,m+1):
    L,R = map(int,input().split())
    max_L = max(max_L,L)
    min_R = min(min_R,R)
if max_L <= min_R:
    print(min_R - max_L + 1)
else:
    print(0)