n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]
s = 0
for a,_ in AB:
    s += a


def search(x):
    lt = 0
    cum = 0
    for a,b in AB:
        if cum+a <= x:
            lt += a/b
        else:
            lt += (x-cum)/b
            break
        cum += a

    rt = 0
    cum = 0
    for a,b in AB[::-1]:
        if cum+a <= s-x:
            rt += a/b
        else:
            rt += ((s-x)-cum)/b
            break
        cum += a
    if lt >= rt:
        return 1
    return 0
l = 0
r = s
for i in range(100):
    m = (r+l)/2
    if search(m):
        r = m
    else:
        l = m
print(l)