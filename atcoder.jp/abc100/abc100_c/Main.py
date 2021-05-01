n = int(input())
a = list(map(int,input().split()))

def factorization2(n):
    arr = []
    temp = n
    if temp%2==0:
        cnt=0
        while temp%2==0:
            cnt+=1
            temp //= 2
        arr.append([2, cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr==[]:
        arr.append([n, 1])
    return arr

cnt = 0 
for ai in a:
    #print(factorization2(ai))
    if factorization2(ai)[0][0] == 2:
        cnt += factorization2(ai)[0][1]
print(cnt)