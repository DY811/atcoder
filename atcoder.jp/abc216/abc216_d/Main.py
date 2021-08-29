n,m=map(int,input().split())
dict=[[] for _ in range(n+1)]
#真後ろにある色の羅列
num=[0 for _ in range(n+1)]
#直前の色が何回取られたら次取れるようになるか。0になればつぎとれる。
#2は2つとも隠れている状態で、1は1つは上に来ている。０ならすぐ取れる。

for i in range(m):
    k=int(input())
    a=list(map(int,input().split()))
    for i in range(k-1):
        dict[a[i]].append(a[i+1])
        num[a[i+1]]+=1

#print(dict,num)

from collections import deque
q=deque()

for i in range(1,n+1):
    if(num[i]==0):
        q.append(i)
        #print(q)

while q:
    #print(num)
    now=q.popleft()
    for i in dict[now]:
        num[i]-=1
        if(num[i]==0):
            q.append(i)

if(sum(num)==0):
    print("Yes")
else:
    print("No")


