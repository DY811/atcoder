# スペース区切りの整数の入力
n, k = map(int, input().split())
g1 = list(map(int, str(n)))
g2 = list(map(int, str(n)))
g1.sort()
g2.sort(reverse = True)
while 0 in g1:
    g1.remove(0)
#print(g1)
#print(g2)

f = int("".join(map(str, g2))) - int("".join(map(str, g1)))
#print(f)
if k == 0:
    print(n)
elif k == 1:
    print(f)
else:
    for i in range(k-1):
        if f == 0:
            #print(f)
            break
        g1 = list(map(int, str(f)))
        g2 = list(map(int, str(f)))
        g1.sort()
        g2.sort(reverse = True)
        while 0 in g1:
            g1.remove(0)
        f = int("".join(map(str, g2))) - int("".join(map(str, g1)))
    print(f)