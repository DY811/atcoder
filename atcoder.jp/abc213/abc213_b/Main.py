n = int(input())
a = list(map(int,input().split()))
b = sorted(a)
#print(b)

idx = a.index(b[-2])
print(idx+1)


