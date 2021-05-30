a = list(map(int,input().split()))
a.sort()
#print(a)
if a[0] == a[1]:
    print(a[2])
elif a[1] == a[2]:
    print(a[0])
elif a[0] != a[1] and a[1] != a[2] and a[0] != a[2]:
    print(0)