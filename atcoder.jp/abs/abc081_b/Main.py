#　正の整数の個数
n = int(input())
#　整数のリスト
s = list(map(int,input().split()))
#print(s)
# 2^N + 余りのリスト
a = [0] * n
#print(a)

for i in range(n):
    for j in range(0, 36): # Aは最大でも10^9なので
        #print(j)
        if s[i] % 2**j == 0:
            #print(s[i]/2**j)
            a[i] = j
print(min(a))