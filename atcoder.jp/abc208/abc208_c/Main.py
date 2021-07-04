from sys import stdin
n,k = map(int,input().split())
a = list(map(int,input().split()))
narabi = a
#print(a)
common = k//n
amari = k%n
#print(common,amari)
narabi = sorted(a)
#print(narabi)
#print(a)
cnt = amari
#print(cnt)
threshold = narabi[cnt-1]
#print(threshold)
for i in range(int(n)):
    if cnt > 0:
        if a[i] <= threshold:
            #print(a[i],threshold)
            cnt -= 1
            print(common+1)
        else:
            print(common)
    else:
        print(common)