n,x = map(int,input().split())
a = list(map(int,input().split()))

jpy = 0
for i in range(n):
    jpy += a[i]
    
discount = n//2

if jpy-discount <= x:
    print("Yes")
else:
    print("No")

