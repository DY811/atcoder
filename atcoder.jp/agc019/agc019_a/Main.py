q,h,s,d = map(int,input().split())
n = int(input())

min_l = min(q*4,h*2,s)
min_2l = min(q*8,h*4,2*s,d)

if n % 2 == 0:
    print(int(n//2*min_2l))
else:
    print(int(n//2*min_2l+min_l))