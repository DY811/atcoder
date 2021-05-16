H,W = map(int,input().split())

point = []
for i in range(H):
    p = [0]*W
    point.append(p)

S = []
for i in range(H):
    s = input()
    for j in range(W):
        if s[j] == "+":
            point[i][j] = 1
        else:
            point[i][j] = -1
    
dp = []
for i in range(H):
    d = [-float("Inf")]*W
    dp.append(d)

#「ここからスタートした時の最大値」を右下のゴールから求めていく
dp[H-1][W-1] = 0#ゴールからスタートすると動かせないのでゼロ
for i in reversed(range(H)):
    for j in reversed(range(W)):
        if j+1 <W:
            #一つ手前からスタートした時を考えた場合（分かりやすくゴールの1歩手前とする）、
            #青木の点数はゴールからスタートした場合に等しい。
            #移動先が１つ増えるので１つ分の点数を足し、青木の点数を引く。
            dp[i][j] = max(dp[i][j],point[i][j+1]-dp[i][j+1])
        if i+1 <H:
            dp[i][j] = max(dp[i][j],point[i+1][j]-dp[i+1][j])
#print(dp)
if dp[0][0]>0:
    ans = "Takahashi"
elif dp[0][0]<0:
    ans = "Aoki"
else:
    ans = "Draw"
print(ans)