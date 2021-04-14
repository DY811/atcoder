X = int(input())

#X円まで0/1のリストつくる
dp = [0] * (X + 1 + 105)
#0円は何も選択しなくても作れる＆1円からが問題
dp[0] = 1

for i in range(X):
    if dp[i] == 1:
        for j in range(100, 106): #100 to 105まで6分岐
            dp[i + j] = 1
#print(dp)
print(dp[X])