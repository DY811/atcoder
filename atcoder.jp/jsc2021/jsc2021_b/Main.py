n,m = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
#print(a,b)
c = list(set(a)^set(b))
c.sort()

if len(c) > 0:
    for i in range(len(c)):
        print(c[i], end = " ")
else:
    print("")