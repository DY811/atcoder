_ = int(input())
A = list(map(int, input().split()))
ans = 0
brick = 0

for a in A:
    if a == brick + 1:
        brick += 1
    else:
        ans += 1
if brick == 0:
    ans = -1
print(ans)