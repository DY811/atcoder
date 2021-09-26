n = int(input())
a = list(map(int,input().split()))
x = int(input())
suma = sum(a)
tmp = x//suma

#tmp*n項目まで足している
kei = suma*tmp
cnt = tmp*n

for i in range(n+1):
    if kei> x:
        print(cnt)
        exit()
    else:
        cnt += 1
        kei += a[i]
    