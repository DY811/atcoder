n,m,x = map(int,input().split())
list_c = []

for i in range(n):
    list_c.append(list(map(int,input().split())))

#check
#print(list_c)

# read book = 1 
min_cost = float("inf")
for i in range(2**n): #本を読む読まないの組み合わせ
    book = [0]*n
    cost = 0
    understanding = [0]*m
    for j in range(n):
        if (i>>j&1):
            book[n-1-j] = 1
            cost += list_c[n-1-j][0]
            understanding = [x+y for (x,y) in zip(understanding,list_c[n-1-j][1:])]
        #ここで本を読むか読まないか、コスト、理解度が決まる
    #今の本のセットでクリアしているか判定
    if min(understanding) >= x:
        min_cost = min(min_cost,cost)
if min_cost == float("inf"):
    print(-1)
else:
    print(min_cost)
