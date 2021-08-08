from bisect import bisect_left
h,w,n = map(int,input().split())
row = []
col = []
card = []
for i in range(n):
    a,b = list(map(int,input().split()))
    row.append(a)
    col.append(b)
    card.append([a,b])
#print(row,col,card)
yoko = len(set(row))
tate = len(set(col))
r = list(set(row))
c = list(set(col))
r.sort()
c.sort()
for i in range(n):
    print(bisect_left(r,card[i][0])+1,bisect_left(c,card[i][1])+1)
    