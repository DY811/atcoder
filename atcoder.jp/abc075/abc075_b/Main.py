H, W = map(int, input().split())
S = list(input() for _ in range(H))
ans = []
for _ in range(H):
    ans.append([100]*W)
#print(ans)
for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            ans[y][x] = "#"
            continue
        bomb = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= y + i <= H - 1 and 0 <= x + j <= W - 1:
                    if S[y + i][x + j] == "#":
                        bomb += 1
        ans[y][x] = bomb
for k in ans:
    #print(str(k))
    print(''.join(map(str,k)))


