from collections import deque
#幅優先探索
r,c = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
maze = [input() for _ in range(r)]

#行列のインデックスをリストのインデックスに合わせる
sx -= 1
sy -= 1
gx -= 1
gy -= 1

#距離行列の初期化（−1）
dist = []
for i in range(r):
    dist.append([-1]*c)

#キューに最初の点を入れる
q = deque()
q.append([sx,sy])
dist[sx][sy] = 0

while len(q) > 0:
    i,j = q.popleft()
    for i2, j2 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
        if not((0 < i2 < r) and (0 < j2 < c)):
            continue
        if maze[i2][j2] == "#":
            continue
        if dist[i2][j2] == -1:
            dist[i2][j2] = dist[i][j] + 1
            q.append([i2,j2])
print(dist[gx][gy])                        