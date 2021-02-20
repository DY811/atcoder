# 整数の入力、スペース区切り
n, y = map(int, input().split())
cnt = 0

for ai in range(n + 1):
    for bi in range(n + 1 - ai):
        ci = n - ai - bi
        #print(ai,bi,ci)
        #print(ai*10000 + bi*5000 + ci*1000)
        if ai*10000 + bi*5000 + ci*1000 == y:
            print(ai, bi, ci)
            cnt += 1
            break
    if ai*10000 + bi*5000 + ci*1000 == y:
        break    
if cnt == 0:
    print("-1 -1 -1")