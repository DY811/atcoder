n, a, b = map(int, input().split())
s = 0

for i in range(1, n + 1):
    keta = sum(list(map(int,str(i))))
    if a <= keta <= b:
        s += i
print(s)