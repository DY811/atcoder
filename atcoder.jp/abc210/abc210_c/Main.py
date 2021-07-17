N,K = map(int,input().split())
C = list(map(int,input().split()))
dic = {}
for i in range(K):
    if C[i] in dic:
        dic[C[i]] += 1
    else:
        dic[C[i]] = 1
ans = len(dic)

#print(dic)
for i in range(1,N-K+1):
    if C[i+K-1] in dic:
        dic[C[i+K-1]] += 1
    else:
        dic[C[i+K-1]] = 1
    if dic[C[i-1]] == 1:
        dic.pop(C[i-1])
    else: 
        dic[C[i-1]] -= 1
    #print(i,dic)
    ans = max(ans,len(dic))
print(ans)