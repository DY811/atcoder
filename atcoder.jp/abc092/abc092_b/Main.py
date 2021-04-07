n = int(input())
d,x = map(int,input().split())
a = list(int(input()) for _ in range(n))
#print(a)
cnt = 0
for j in range(len(a)):
    for i in range(0,d):
        day = 0
        day += i*a[j] + 1
        if day > d:
            break
        else: 
            cnt += 1
print(cnt+x)    