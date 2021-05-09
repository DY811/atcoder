n= int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

l = 1
for i in a:
    l = lcm(l, i)

#f(l) = 0
#f(l-1) = sum(ai -1)になる
f = 0
for i in a:
    f += i - 1
print(f)
