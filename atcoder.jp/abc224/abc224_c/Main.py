n = int(input())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))
#print(a)
cnt = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            #print(i,j,k)
            x1 = a[j][0]-a[i][0] 
            y1 = a[j][1]-a[i][1] 
            x2 = a[k][0]-a[i][0]
            y2 = a[k][1]-a[i][1]
            if 1/2*abs(x1*y2-x2*y1) > 0:
                cnt += 1
print(cnt)