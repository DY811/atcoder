#参考https://ebisuke33.hatenablog.com/entry/abc215d?_ga=2.159895614.2056046895.1629609188-774016634.1628407057

N, M = map(int,input().split())
A = list(map(int, input().split()))

# 約数をdivに加える
def make_divisors(n):
    i = 1
    while i*i <= n:
        if n % i == 0:
            div.add(i)
            if i != n // i:
                div.add(n//i)
        i += 1
    return

# 約数列挙
div = set()

# Aiの約数を求める
for i in range(N):
    make_divisors(A[i])

#print(div)
Div = list(div)

# 答えの配列(1~M) 約数なら除いていく。
res = [True for i in range(M)]

# 約数の倍数をFalseに
for i in range(len(Div)):
    # Div[i]が1ならスキップ
    if Div[i] == 1:
        continue
    k = 1
    while Div[i] * k <= M:
        res[Div[i] * k - 1] = False 
        #M以下でdiv[i]の倍数は全てfalseに
        #print(Div[i]*k)
        k += 1

# 解答の配列(1は加えておく)
ans = [1]
for k in range(1,M):
    # resがTrueならINDEXをansに追加
    if res[k]:
        ans.append(k+1)

#答えの数と値を出力
print(len(ans))
for i in range(len(ans)):
    print(ans[i])