n,m = map(int,input().split())
list_k = []

for i in range(m):
    list_k.append(list(map(int,input().split())))
p = list(map(int,input().split()))

#confirmation of input
#print(list_k)
#print(p)

ans = 0
for i in range(2**n):
    switch = [0]*n
    for j in range(n):
        if ((i>>j)&1):
            switch[n-1-j] += 1
    #ここまででスイッチが１通り決まる
    lamp = [0]*m
    #ここからm個の電球を調べていく
    for k in range(m):
        on_num = 0
        for l in range(1,list_k[k][0]+1):#switch number
            if switch[list_k[k][l]-1] == 1:#switchがonかどうか
                on_num += 1  
        #mの電球がついているか        
        if on_num%2 == p[k]:
            lamp[k] += 1
    #print(lamp)        
    if sum(lamp) == m:
        ans += 1
print(ans)
