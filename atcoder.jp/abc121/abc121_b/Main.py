# abc 121 B Can you solve this?
N, M, C = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0

for i in range(N):
    #print(i)
    A = list(map(int, input().split()))
    s = C
    for i in range(M):
        s += A[i] * B[i]
    #print(s)
    if s > 0:
        cnt += 1
print(cnt)