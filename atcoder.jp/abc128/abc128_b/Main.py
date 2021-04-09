n = int(input())
res = [list(input().split()) for _ in range(n)]

for i in range(n):
    res[i].insert(0,i+1)
  
ans = sorted(res, key = lambda x: (x[1],-int(x[2]))) #マイナスをつけると降順
#print(ans[5])
for i in range(n):
    #print(i,n)
    print(ans[i][0])