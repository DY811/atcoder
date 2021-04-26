import math
n = int(input())
ans = 0

for i in range(1, n+1, 2):#1からnまで２個飛ばして奇数を探索
    cnt = 0
    for j in range(1, n+1, 2):
        if i % j == 0:
            #print(j)
            cnt += 1
    #print(cnt)
    if cnt == 8:
        ans += 1
print(ans)

