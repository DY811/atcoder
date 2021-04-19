n=str(input())

ans=0

for i in range(len(n)):
    ans+=int(n[i])

print(max(ans,int(n[0])-1+(9*(len(n)-1))))

