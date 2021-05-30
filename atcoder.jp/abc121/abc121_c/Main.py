n,m = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]

b = sorted(a, key = lambda x:x[0])#安い順にソート

cnt = 0
cost = 0
for i in range(n):
    if m - cnt > 0: #bottle in need
        if b[i][1] <=  m - cnt: #max purchase
            cost += b[i][0]*b[i][1]
            cnt += b[i][1]
        else:
            cost += b[i][0]*(m-cnt)
            cnt += m-cnt
    else:
        break
print(cost)