n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    a[i] -= 1
cnt = 0
for i in range(n):
    if a[a[i]] == i:
        cnt += 1
print(cnt//2)