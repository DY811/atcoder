n,x = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
#print(a)
candy = 0
for i in range(len(a)):
    candy += a[i]
    if candy == x:
        print(i+1)
        break
    elif candy > x and i > 0:
        print(i)
        break    
    elif candy > x and i == 0:
        print(0)
        break
else:
    print(i)