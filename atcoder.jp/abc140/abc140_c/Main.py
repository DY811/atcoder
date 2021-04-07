n = int(input())
b = list(map(int,input().split()))
a = [0]*n
for i in range(n-1):
    if i == 0:
        a[i] = b[0]
    else:
        a[i] = min(b[i],b[i-1])
a[n-1] = b[n-2]
print(sum(a))