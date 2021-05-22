from collections import Counter
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
c = list(map(int,input().split()))
d = Counter(c)
e = Counter(a)

ans = 0
for key,value in d.items():
    #print(b[key-1],value)
    if b[key-1] in e:
            ans += value*e.get(b[key-1])
print(ans)