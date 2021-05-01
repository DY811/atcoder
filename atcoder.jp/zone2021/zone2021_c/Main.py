N = int(input())
A = [tuple(map(int, input().split())) for i in range(N)]
#転置行列
tA = []
for i in range(5):
    tmp = []
    for vector in A:
        tmp.append(vector[i])
    tA.append(tmp)
#3人ではなく全員の時を算出
max_scores = []
for i in range(5):
    max_scores.append(max(tA[i]))
#最大のスコアが決まる
ideal_score = min(max_scores)
    
def check(x):
    s = set()
    for a in A:
        #基準をクリアしているかをバイナリで管理（１１１１１なら全部クリア）
        s.add(sum(1 << i for i in range(5) if a[i] >= x))
    #print(s)
    for x in s:
        for y in s:
            for z in s:
                if x | y | z == 31:#11111 = bin(31)だから
                    return True
    return False

#２分探索
ok = 0
ng = ideal_score+1
while ng - ok > 1:
    cen = (ok + ng) // 2
    if check(cen):
        ok = cen
    else:
        ng = cen
print(ok)

