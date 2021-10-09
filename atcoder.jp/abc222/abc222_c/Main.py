import numpy as np
n,m = map(int,input().split())
a = []
for _ in range(2*n):
    tmp = list(input())
    a.append(tmp)
#print(a)

    
def gcp(f,s,c):
    if a[f][c] == 'G' and a[s][c] == 'C':
        return 0
    elif a[f][c] == 'G' and a[s][c] == 'G':
        return -1
    elif a[f][c] == 'G' and a[s][c] == 'P':
        return 1
    elif a[f][c] == 'C' and a[s][c] == 'C':
        return -1
    elif a[f][c] == 'C' and a[s][c] == 'G':
        return 1
    elif a[f][c] == 'C' and a[s][c] == 'P':
        return 0
    elif a[f][c] == 'P' and a[s][c] == 'C':
        return 1
    elif a[f][c] == 'P' and a[s][c] == 'G':
        return 0
    else:
        return -1

rank = [[0,i] for i in range(2*n)]

for j in range(m):
    for i in range(n):
        tmp = gcp(rank[2*i][1],rank[2*i+1][1],j)
        #print(rank[2*i][1],rank[2*i+1][1])
        if tmp == -1:
            continue
        else:
            rank[2*i+tmp][0] -= 1
    rank.sort()
    #print(rank)
#print(score)

#print(r)
for _,i in rank:
    print(i+1)



