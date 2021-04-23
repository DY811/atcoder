n = int(input())
h = list(map(int,input().split()))
before = h[0]-1
for i in range(1,n):
    if before > h[i]:
        print("No")
        break
    elif before == h[i]:
        before = h[i]
    else:
        before = h[i]-1
else:        
    print("Yes")