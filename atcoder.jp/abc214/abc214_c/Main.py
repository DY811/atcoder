N = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

first = T.index(min(T))#最初にもらう
tmp = T[first]
ans = [0]*N
ans[first] = tmp#確定
i = first
for _ in range(N-1):
    i = (i+1) % N#まわることがあるのでNのあまり
    tmp = min(tmp+S[i-1], T[i])
    ans[i] = tmp

for a in ans:
    print(a)


