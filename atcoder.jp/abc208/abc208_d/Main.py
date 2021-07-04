import sys
N, M = map(int, sys.stdin.buffer.readline().split())
ABC = map(int, sys.stdin.buffer.read().split())
d = [[1<<60] * N for i in range(N)]
for i in range(N):
  d[i][i] = 0
for a, b, c in zip(ABC, ABC, ABC):
  d[a - 1][b - 1] = c
answer = 0
for k in range(N):
  nxt = [[0] * N for i in range(N)]
  for i in range(N):
    for j in range(N):
      nxt[i][j] = min(d[i][j], d[i][k] + d[k][j])
      if nxt[i][j] < 1<< 60:
        answer += nxt[i][j]
  d = nxt
print(answer)


