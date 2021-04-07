#abc160 C Traveling Salesman around Lake
k, n = map(int,input().split())
a = list(map(int,input().split()))
d = [0]*k #distance

for i in range(n):
    if i == 0:
        d[i] = k - a[n-1] + a[i]
    else:
        d[i] = a[i] - a[i-1]
max_value = max(d)
# max_index = d.index(max_value)
ans = sum(d) - max_value
print(ans)