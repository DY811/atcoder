A,B,K=map(int,input().split())
before=[i for i in range(A,min(A+K,B+1))]
after=[i for i in range(B,max(B-K,A-1),-1)]
#print(before)
#print(after)
before.extend(after) # also works with "before+after"
ans=set(before)
for i in sorted(ans):
    print(i)