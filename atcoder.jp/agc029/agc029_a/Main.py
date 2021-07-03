S = input()
b = []

# Bを全て右に詰めるのにかかる操作回数を調べる
for i in range(len(S)):
    if S[i] == "B":
        b.append(i)

ans = 0
li = len(b)
for i, v in enumerate(b):
    ans += len(S) - li - v
    li -= 1

print(ans)