n = int(input())
p = list(map(int,input().split()))
q = [0]*n
#print(q)

for i in range(n):
    #print(p[i])
    q[p[i]-1] = i+1
print(*q)