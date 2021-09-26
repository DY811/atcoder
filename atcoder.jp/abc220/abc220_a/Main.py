a,b,c = map(int,input().split())
d = b//c

if d*c >= a:
    print(d*c)
else:
    print(-1)