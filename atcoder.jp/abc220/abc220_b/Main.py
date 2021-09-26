k = int(input())
a,b = map(str,input().split())
ans1 = 0
ans2 = 0
for i in range(len(a))[::-1]:
    ans1 += int(a[len(a)-i-1])*k**i
for i in range(len(b))[::-1]:
    ans2 += int(b[len(b)-i-1])*k**i
print(ans1*ans2)