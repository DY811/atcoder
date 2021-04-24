n = int(input())
s = input()
q = int(input())
ans = list(range(1,2*n+1))
#print(len(ans))
flip = 0

for i in range(q):
    t,a,b = map(int,input().split())
    if t == 1 and flip%2 == 0:
        aa = ans[a-1]
        bb = ans[b-1]
        ans[a-1] = bb 
        ans[b-1] = aa
        #print(ans)
    elif t == 1 and flip%2 != 0:
        if (a - 1) < n and (b - 1) < n:
            aa = ans[a-1+n]
            bb = ans[b-1+n]
            ans[a-1+n] = bb
            ans[b-1+n] = aa
            #print(ans)
        elif (a - 1) < n and (b - 1) >= n:
            aa = ans[a-1+n]
            bb = ans[b-1-n]
            ans[a-1+n] = bb
            ans[b-1-n] = aa
            #print(ans)
        elif (a - 1) >= n and (b - 1) >= n:
            aa = ans[a-1-n]
            bb = ans[b-1-n]
            ans[a-1-n] = bb
            ans[b-1-n] = aa
            #print(ans)
    else:
        flip += 1
if flip %2 == 0:
    for i in range(2*n):
        print(s[ans[i]-1],end="")
else:
    ans = ans[n:]+ans[:n]
    for i in range(2*n):
        print(s[ans[i]-1],end="")
    