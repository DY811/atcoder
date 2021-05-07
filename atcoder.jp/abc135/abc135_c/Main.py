n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

monster = 0
c = 0
for i in range(n):
    monster += min(a[i],(b[i]+c))
    if (b[i]+c)-a[i] > 0:
        if c >= a[i]:
            c = b[i]
        else :
            c = b[i] - (a[i]-c)
    else:
        c = 0
    #print(c,monster)
monster += min(c,a[-1])
print(monster)