n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(2**(n-1)):
    separation = [0]*(n-1)
    for j in range(n-1):
        if (i>>j&1):
            separation[(n-1)-1-j] = 1
        #ここまでで区切りを入れるかどうかのリストが完成   
    #print(separation)
    ored = 0  # x | 0 = xだから
    xored = 0 # x ^ 0 = xだから
    #区切りがくるまでorを計算し、区切りが来たらxorを計算しorを0に戻す
    for idx,k in enumerate(separation):
        ored |= a[idx]
        #print(ored)
        if separation[idx]&1:
            xored ^= ored
            ored = 0
    #separationより１つ長い最後を計算
    ored |= a[n-1]
    xored ^= ored
    ans.append(xored)
print(min(ans))