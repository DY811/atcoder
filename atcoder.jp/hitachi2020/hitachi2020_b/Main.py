A,B,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = [list(map(int,input().split())) for _ in range(M)]
#print(A, B, M)
#print(a)
#print(b)
#print(m)
mina = min(a)
minb = min(b)
mina_index = [i for i,x in enumerate(a) if x == mina]
minb_index = [i for i,x in enumerate(b) if x == minb]
cost = mina + minb # if not applied a coupon
for i in range(M):
    cost_tmp = a[m[i][0]-1] + b[m[i][1]-1] - m[i][2]
    cost = min(cost, cost_tmp)
print(cost)