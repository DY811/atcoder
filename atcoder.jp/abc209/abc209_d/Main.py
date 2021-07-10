from collections import deque
n,q = map(int,input().split())

g = []
for _ in range(n):
    g.append([])

for i in range(n-1):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)
    
dist = []
for _ in range(n):
    dist.append(-1)
Q = deque()
Q.append(0)
dist[0] = 0
while len(Q) > 0:
    i = Q.popleft()
    for j in g[i]:
        if dist[j] == -1:
            dist[j] = dist[i] + 1
            Q.append(j)
#print(saitan)
for i in range(q):
    c,d = map(int,input().split())
    c -= 1
    d -= 1
    if (abs(dist[c]-dist[d]))%2 == 0:
        print("Town")
    else:
        print("Road")