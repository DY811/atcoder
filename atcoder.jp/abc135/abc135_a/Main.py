a,b  = map(int, input().split())
k = (a+b)/2
if k % 1 == 0:        
    print(int(k))
else:
    print("IMPOSSIBLE")