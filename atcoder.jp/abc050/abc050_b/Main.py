n = int(input())
t = list(map(int,input().split()))
time = sum(t) #without drining
m = int(input())
#キーに同じものがあるので辞書は使えないがメモ
#drink = dict(list(map(int,input().split())) for _ in range(m))
#print(drink.get(1)) #key1のvalueがかえる
#print(drink[1])#上と同じ。キーがないとエラー
#print(drink.get(3)) #キーがない時Noneがかえる
drink = [list(map(int,input().split())) for _ in range(m)]

for i in range(m):
    delta = drink[i][1] - t[drink[i][0]-1]
    #print(drink[i][1],t[drink[i][0]]-1)
    print(time+delta)