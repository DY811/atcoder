n=int(input())
p=list(map(int,input().split()))
p2=sorted(p)
cnt=0
for x,y in zip(p,p2):
    if x!=y:
        cnt+=1
if cnt==2 or cnt==0:
    print('YES')
else:
    print('NO')