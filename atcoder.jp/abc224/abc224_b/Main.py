h,w = map(int,input().split())
a = []
for i in range(h):
    tmp = list(map(int,input().split()))
    a.append(tmp)
#print(a)
for i in range(h):
    for j in range(i+1):
        for k in range(w):
            for l in range(k+1):
                if a[i][k] + a[j][l] <= a[j][k] + a[i][l]:
                    continue
                else:
                    print('No')
                    exit()
else:
    print('Yes')