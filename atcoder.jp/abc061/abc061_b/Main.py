n,m = map(int,input().split())
all = []
cnt = [0]*n
for i in range(m):
    all.append(list(map(int,input().split())))
    #print(all)
    for j in range(1,n+1):
        if all[i][0] == j or all[i][1] == j:
            cnt[j-1] += 1
#print(all)
#print(cnt)
for i in range(n):
    print(cnt[i])