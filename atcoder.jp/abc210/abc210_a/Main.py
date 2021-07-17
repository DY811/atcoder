n,a,x,y = map(int,input().split())

if n>=a:
    print((n-a)*y+a*x)
else:
    print(n*x)