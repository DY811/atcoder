# abc156 C Rally
n = int(input())
x = list(map(int,input().split()))
ans = float("Inf")
# print(n)
# print(len(x))

for P in range(1,101):
    #print(P)
    tmp = 0
    for j in range(n):
        tmp += (x[j]-P)**2
    ans = min(ans,tmp)
print(ans)   